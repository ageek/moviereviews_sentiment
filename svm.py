import csv

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC


train_data = []
train_sentiment = []
counter = 0
with open('data/train.tsv') as f:
    next(f)
    reader = csv.reader(f, delimiter='\t')
    for phrase_id, sentence_id, phrase, sentiment in reader:
        counter += 1
        train_data.append(phrase)
        train_sentiment.append(sentiment)

count_vect = CountVectorizer()
train_counts = count_vect.fit_transform(train_data)

clf = SVC(kernel='linear')
clf_model = clf.fit(train_counts, train_sentiment)

test_data = []
phrase_id_list = []
with open('data/test.tsv') as f:
    next(f)
    reader = csv.reader(f, delimiter='\t')
    for phrase_id, sentence_id, phrase in reader:
        test_data.append(phrase)
        phrase_id_list.append(phrase_id)

test_counts = count_vect.transform(test_data)

sentimend_pred = clf.predict(test_counts)

for (id, s) in zip(phrase_id_list, sentimend_pred):
    print str(id) + "," + str(s)