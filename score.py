import sys

gold_file = sys.argv[1]
pred_file = sys.argv[2]

# Load the gold standard
gold = {}
for line in open(gold_file):
    record, string, entity = line.strip().split('\t', 2)
    gold[(record, string)] = entity
n_gold = len(gold)
print('gold: %s' % n_gold)

# Load the predictions
pred = {}
for line in open(pred_file):
    record, string, entity = line.strip().split('\t', 2)
    pred[(record, string)] = entity
n_predicted = len(pred)
print('predicted: %s' % n_predicted)

# Evaluate predictions
n_correct = sum( int(pred[i]==gold[i]) for i in set(gold) & set(pred) )
print('correct: %s' % n_correct)

# Calculate scores
precision = float(n_correct) / float(n_predicted)
print('precision: %s' % precision )
recall = float(n_correct) / float(n_gold)
print('recall: %s' % recall )
f1 = 2 * ( (precision * recall) / (precision + recall) )
print('f1: %s' % f1 )