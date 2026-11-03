import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	# Your code here
	sigmoid=lambda x: 1/(1+np.exp(-x))
	z=X@weights+bias
	p=sigmoid(z)
	p[p>=0.5]=1
	p[p<0.5]=0
	p=p.astype(int)
	return p