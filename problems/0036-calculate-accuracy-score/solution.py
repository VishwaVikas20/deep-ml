import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	total_pred=y_pred.shape[0]
	e=y_true-y_pred
	s=0
	for i in e:
		s+=abs(i)
	correct_preds=total_pred-s
	return correct_preds/total_pred