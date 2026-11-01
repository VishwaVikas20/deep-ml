import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X=np.array(X)
	a=X.T@X
	b=X.T@y
	theta=np.linalg.inv(a)@b
	return theta