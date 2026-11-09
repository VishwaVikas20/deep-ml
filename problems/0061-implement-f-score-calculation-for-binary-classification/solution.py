import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""
	TP=0
	TN=0
	FP=0
	FN=0
	for idx,v in enumerate(y_true):
		if v==0:
			if y_pred[idx]==0:
				TN+=1
			elif y_pred[idx]==1:
				FP+=1
		elif v==1:
			if y_pred[idx]==1:
				TP+=1
			elif y_pred[idx]==0:
				FN+=1
	if TP==0:
		return 0.0
	precision=TP/(TP+FP)
	recall=TP/(TP+FN)
	f_score=(1+beta**2)*precision*recall/((beta**2 * precision)+recall)
	return round(f_score,3)
