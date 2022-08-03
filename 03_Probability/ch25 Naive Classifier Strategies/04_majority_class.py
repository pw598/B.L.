# example of a majority class naive classifier
from scipy.stats import mode
from sklearn.metrics import accuracy_score

# predict the majority class
def majority_class(y):
	return mode(y)[0]

# define dataset
class0 = [0 for _ in range(25)]
class1 = [1 for _ in range(75)]
y = class0 + class1
# make predictions
yhat = [majority_class(y) for _ in range(len(y))]
# calculate accuracy
accuracy = accuracy_score(y, yhat)
print('Accuracy: %.3f' % accuracy)