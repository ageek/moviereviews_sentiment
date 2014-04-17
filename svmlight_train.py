import csv, hashlib, math, random

train = open('data/svmlight/train.dat', 'w')
train0 = open('data/svmlight/train0.dat', 'w')
train1 = open('data/svmlight/train1.dat', 'w')
train2 = open('data/svmlight/train2.dat', 'w')
train3 = open('data/svmlight/train3.dat', 'w')
train4 = open('data/svmlight/train4.dat', 'w')

val = open('data/svmlight/val_train.dat','w')
val_test =open('data/svmlight/val_test.dat', 'w')

test = open('data/svmlight/test.dat', 'w')

val_size = 0.2 
with open('data/train.tsv') as f:
	next(f)
	reader = csv.reader(f, delimiter='\t')
	for phrase_id, sentence_id, phrase, sentiment in reader:
		features = {}
		line = str(int(sentiment)+1)
		line_pos = '+1'
		line_neg = '-1'

		tokens = phrase.split(" ")
		for t in tokens:
			h = int(hashlib.sha1(t).hexdigest(),16) % (10 ** 8)
			features[h] = 1
		
		l = math.sqrt(1/float(len(tokens)))
		for h in sorted(features):
			line = line + " " + str(h) + ":" + str(l)
			line_pos = line_pos + " " + str(h) + ":" + str(l)
			line_neg = line_neg + " " + str(h) + ":" + str(l)

		if(random.random() <= val_size):
			val.write(line + '\n')
			val_test.write(phrase_id + " " + sentiment + '\n')
			continue

		train.write(line + '\n')
		if(sentiment == '0'):
			train0.write(line_pos + '\n')
			train1.write(line_neg + '\n')
			train2.write(line_neg + '\n')
			train3.write(line_neg + '\n')
			train4.write(line_neg + '\n')
		elif(sentiment == '1'):
			train0.write(line_neg + '\n')
			train1.write(line_pos + '\n')
			train2.write(line_neg + '\n')
			train3.write(line_neg + '\n')
			train4.write(line_neg + '\n')
		elif(sentiment == '2'):
			train0.write(line_neg + '\n')
			train1.write(line_neg + '\n')
			train2.write(line_pos + '\n')
			train3.write(line_neg + '\n')
			train4.write(line_neg + '\n')
		elif(sentiment == '3'):
			train0.write(line_neg + '\n')
			train1.write(line_neg + '\n')
			train2.write(line_neg + '\n')
			train3.write(line_pos + '\n')
			train4.write(line_neg + '\n')
		elif(sentiment == '4'):
			train0.write(line_neg + '\n')
			train1.write(line_neg + '\n')
			train2.write(line_neg + '\n')
			train3.write(line_neg + '\n')
			train4.write(line_pos + '\n')

with open('data/test.tsv') as f:
	next(f)
	reader = csv.reader(f, delimiter='\t')

	for phrase_id, sentence_id, phrase in reader:
		features = {}
		line = "0"

		tokens = phrase.split(" ")
		for t in tokens:
			h = int(hashlib.sha1(t).hexdigest(),16) % (10 ** 8)
			features[h] = 1

		l = math.sqrt(1/float(len(tokens)))
		for h in sorted(features):
			line = line + " " + str(h) + ":" + str(l)

		test.write(line + '\n')

val.close()
val_test.close()

train.close()
train1.close()
train2.close()
train3.close()
train4.close()
test.close()
