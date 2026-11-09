import numpy as np

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
	"""
	Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
	"""
	# Your code here
	samples=X.shape[0]
	y=np.reshape(y,(-1,1))
	def sigmoid(y):
		return 1/(1+np.exp(-y))
	X_c = np.concatenate((np.ones((X.shape[0], 1)), X), axis=1)
	w=np.zeros((X_c.shape[1],1))
	losses=[]
	for _ in range(iterations):
		y_hat=sigmoid(X_c@w)
		grad=X_c.T@(y_hat-y)
		loss = -np.sum(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))
		losses.append(round(float(loss), 4))
		w=w-learning_rate*grad
	w = [round(float(v), 4) for v in w.flatten()]
	return w, losses
	