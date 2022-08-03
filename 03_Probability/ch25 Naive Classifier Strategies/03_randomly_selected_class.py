# example of selecting a random class naive classifier
from numpy import mean
from numpy.random import randint
from sklearn.metrics import accuracy_score

# predict a randomly selected class
def random_class(y):
	return y[randint(len(y))]

# define dataset
class0 = [0 for _ in range(25)]
class1 = [1 for _ in range(75)]
y = class0 + class1
# average over many repeats
results = list()
for _ in range(1000):
	yhat = [random_class(y) for _ in range(len(y))]
	acc = accuracy_score(y, yhat)
	results.append(acc)
print('Mean: %.3f' % mean(results))