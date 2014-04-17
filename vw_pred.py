import csv

pred0_reader = csv.reader(open('data/vw/test0.pred'), delimiter=' ')
pred1_reader = csv.reader(open('data/vw/test1.pred'), delimiter=' ')
pred2_reader = csv.reader(open('data/vw/test2.pred'), delimiter=' ')
pred3_reader = csv.reader(open('data/vw/test3.pred'), delimiter=' ')
pred4_reader = csv.reader(open('data/vw/test4.pred'), delimiter=' ')

print "PhraseId,Sentiment"
for (row0, row1, row2, row3, row4) in zip(pred0_reader, pred1_reader, pred2_reader, pred3_reader, pred4_reader):
	pred = [row0[0], row1[0], row2[0], row3[0], row4[0]]
	# print pred
	print str(row0[1]) + "," + str(pred.index(max(pred)))