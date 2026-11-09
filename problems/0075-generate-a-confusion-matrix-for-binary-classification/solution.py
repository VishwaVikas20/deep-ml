
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	TP=0
	TN=0
	FP=0
	FN=0
	for s in data:
		if s[0]==s[1]==1:
			TP+=1
		elif s[0]==s[1]==0:
			TN+=1
		elif s[0]==1 and s[1]==0:
			FN+=1
		else:
			FP+=1
	matrix=[[TP,FN],[FP,TN]]
	return matrix
