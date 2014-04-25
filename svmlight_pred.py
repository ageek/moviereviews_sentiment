import math
import csv
import sys


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def main():
    test_pred = csv.reader(open(sys.argv[1]), delimiter=" ")

    print "PhraseId,Sentiment"
    for (phrase_id, pred0, pred1, pred2, pred3, pred4) in test_pred:
        prob = [sigmoid(float(pred0)), sigmoid(float(pred1)), sigmoid(float(pred2)), \
                sigmoid(float(pred3)), sigmoid(float(pred4))]
        print phrase_id + "," + str(prob.index(max(prob)))


main()