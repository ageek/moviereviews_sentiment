import csv
import random
import string

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from nltk.stem.porter import *



# Parameters
validation_size = 0.2  # values: decimal between 0-1
model = 'svm'  # values: logistic, naivebayes, svm
predict_test = True  # generate test predictions?
ngram_max = 2  # largest n-gram size for building train_features


# Load Training Data
train_data = []
train_sentiment = []
counter = 0
with open('data/train.tsv') as f:
    next(f)
    reader = csv.reader(f, delimiter='\t')
    stemmer = PorterStemmer()
    for phrase_id, sentence_id, phrase, sentiment in reader:
        counter += 1
        string.join([stemmer.stem(w) for w in phrase.split(' ')])
        train_data.append(phrase)
        train_sentiment.append(sentiment)

# Build training & validation sets
train_data, val_data, train_sentiment, val_sentiment = \
    cross_validation.train_test_split(train_data, train_sentiment, \
                                      test_size=validation_size, random_state=random.randint(1, 100))

# Build feature vectors
vectorizer = CountVectorizer(ngram_range=(1, ngram_max))
train_features = vectorizer.fit_transform(train_data)

# Select Training Algorithm
if model == 'logistic':
    clf = LogisticRegression()
elif model == 'naivebayes':
    clf = MultinomialNB()
elif model == 'svm':
    clf = LinearSVC(C=10)

clf_model = clf.fit(train_features, train_sentiment)

# Validation
val_features = vectorizer.transform(val_data)
print clf.score(val_features, val_sentiment)

# Generate Test Predictions
if predict_test:
    test_data = []
    phrase_id_list = []
    with open('data/test.tsv') as f:
        next(f)
        reader = csv.reader(f, delimiter='\t')
        for phrase_id, sentence_id, phrase in reader:
            test_data.append(phrase)
            phrase_id_list.append(phrase_id)

    test_features = vectorizer.transform(test_data)
    sentimend_pred = clf.predict(test_features)

    for (id, s) in zip(phrase_id_list, sentimend_pred):
        print str(id) + "," + str(s)

