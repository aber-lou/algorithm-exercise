
def maxSatisfied(self, customers, grumpy,X):
    res = 0
    sumSat, sumWindow = 0, 0
    for i in range(len(customers)):
        if grumpy[i] == 0:
            sumSat += customers[i]
    
    for j in range(X):
        if grumpy[j] == 1:
            sumWindow += customers[j]

    maxWindow = sumWindow

    for k in range(X, len(customers)):
            if grumpy[k] == 1:
                sumWindow += customers[k]
            
            if grumpy[k - X] == 1:
                sumWindow -= customers[k - X]
            
            maxWindow = max(maxWindow, sumWindow)
    res = sumSat + maxWindow
    return res
