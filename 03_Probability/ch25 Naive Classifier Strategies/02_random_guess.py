# example of a random guess naive classifier
from numpy import mean
from numpy.random import random
from sklearn.metrics import accuracy_score

# guess random class
def random_guess():
	if random() < 0.5:
		return 0
	return 1

# define dataset
class0 = [0 for _ in range(25)]
class1 = [1 for _ in range(75)]
y = class0 + class1
# average performance over many repeats
results = list()
for _ in range(1000):
	yhat = [random_guess() for _ in range(len(y))]
	acc = accuracy_score(y, yhat)
	results.append(acc)
print('Mean: %.3f' % mean(results))