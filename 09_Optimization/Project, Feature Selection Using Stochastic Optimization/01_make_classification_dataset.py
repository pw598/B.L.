# define a small classification dataset
from sklearn.datasets import make_classification
# define dataset
X, y = make_classification(n_samples=1000, n_features=5, n_informative=2, n_redundant=3, random_state=1)
# summarize the shape of the dataset
print(X.shape, y.shape)
