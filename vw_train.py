import csv

train0_file = open('data/vw/train0.dat', 'w')
train1_file = open('data/vw/train1.dat', 'w')
train2_file = open('data/vw/train2.dat', 'w')	
train3_file = open('data/vw/train3.dat', 'w')
train4_file = open('data/vw/train4.dat', 'w')
train_file = open('data/vw/train.dat', 'w')

test_file = open('data/vw/test.dat', 'w')

with open('data/train.tsv') as f:
	next(f)
	reader = csv.reader(f, delimiter='\t')
	for phrase_id, sentence_id, phrase, sentiment in reader:
		phrase = phrase.replace(':', '')
		line_pos = '1 1.0 \'' + str(phrase_id) + '|Words ' + phrase + '\n'
		line_neg = '-1 1.0 \'' + str(phrase_id) + '|Words ' + phrase + '\n'
		line = str(int(sentiment)+1) + ' 1.0 \'' + str(phrase_id) + '|Words ' + phrase + '\n'
		
		train_file.write(line)
		if(sentiment == '0'):
			train0_file.write(line_pos)
			train1_file.write(line_neg)
			train2_file.write(line_neg)
			train3_file.write(line_neg)
			train4_file.write(line_neg)
		elif(sentiment == '1'):
			train0_file.write(line_neg)
			train1_file.write(line_pos)
			train2_file.write(line_neg)
			train3_file.write(line_neg)
			train4_file.write(line_neg)
		elif(sentiment == '2'):
			train0_file.write(line_neg)
			train1_file.write(line_neg)
			train2_file.write(line_pos)
			train3_file.write(line_neg)
			train4_file.write(line_neg)
		elif(sentiment == '3'):
			train0_file.write(line_neg)
			train1_file.write(line_neg)
			train2_file.write(line_neg)
			train3_file.write(line_pos)
			train4_file.write(line_neg)
		elif(sentiment == '4'):
			train0_file.write(line_neg)
			train1_file.write(line_neg)
			train2_file.write(line_neg)
			train3_file.write(line_neg)
			train4_file.write(line_pos)

with open('data/test.tsv') as f:
	next(f)
	reader = csv.reader(f, delimiter='\t')
	for phrase_id, sentence_id, phrase in reader:
		phrase = phrase.replace(':', '')
		line =  '\'' + str(phrase_id) + '|Words ' + phrase + '\n'
		test_file.write(line)

train0_file.close()
train1_file.close()
train2_file.close()
train3_file.close()
train4_file.close()
train_file.close()
test_file.close()
