import numpy as np

def precision_recall_at_threshold(y_true, y_scores, threshold):
    """
    Compute precision and recall at a given decision threshold.

    Args:
        y_true: list/array of true binary labels (0 or 1)
        y_scores: list/array of predicted scores in [0, 1]
        threshold: float, classification threshold (predict positive if score >= threshold)

    Returns:
        [precision, recall] as a list of two floats rounded to 4 decimals.
    """
    # Your code here
    TP=0
    TN=0
    FP=0
    FN=0
    y_pred=[1 if x>threshold else 0 for x in y_scores]
    for i,e in enumerate(y_true):
        if e==1:
            if y_pred[i]==1:
                TP+=1
            elif y_pred[i]==0:
                FN+=1
        elif e==0:
            if y_pred[i]==1:
                FP+=1
            elif y_pred[i]==0:
                TN+=1 
    if TP+FP==0 or TP+FN==0:
        return [0.,0.]
    precision=(TP)/(TP+FP)
    recall=TP/(TP+FN)
    return [precision,recall]
