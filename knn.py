import pandas
import math
import numpy as np

rawTrain = pandas.read_excel("dataset.xlsx", sheetname=0)
rawTest = pandas.read_excel("dataset.xlsx", sheetname=1)
train = pandas.DataFrame(rawTrain, columns=['Like','Provokasi','Komentar', 'Emosi'])
classTrain = pandas.DataFrame(rawTrain, columns=['Hoax'])
test = pandas.DataFrame(rawTest, columns=['Like','Provokasi','Komentar', 'Emosi'])

def normalization(t):
    col = t.keys()
    returnT = {}
    for i in range(len(col)):
        data = [d[0] for d in pandas.DataFrame(t, columns=[col[i]]).values]
        maxVal = max(data)
        minVal = min(data)
        normData = []
        for d in data:
            normData.append(round(float(d-minVal)/(maxVal-minVal),2))
        returnT[col[i]] = normData
    return pandas.DataFrame(returnT)

# euclidean distance method
# p and q are an array
# example input of p: [ 0.67 0.24 0.63 0.57]
# example input of q: [ 0.29 0.56 0.13 0.44]
# output from that example: 0.716728679488
def euclDist(p, q):
    lenCol = len(p)
    val = 0
    for i in range(lenCol):
        val += (q[i] - p[i]) ** 2
    return math.sqrt(val)


# to predict each test data
# it only works when you normalized all the data
# if you won't to normalize the data, adjust 'compare' variable
def classify(train, test, classTrain, numberOfK):
    tempTrain = train[:len(train) - 1]
    numer = numberOfK

    kindClass = []
    for c in classTrain:
        if c not in kindClass:
            kindClass.append(c)

    # 'ID' is an index of training data which states
    # that the index has the smallest euclidean
    # distance value of a test data
    # 'Pred' is a class of training data
    resultPred = {
        'ID': [],
        'pred': []
    }

    compare = 1  # change this value if you dont use normalization function
    pred = 0
    id = 0
    for i, data in enumerate(tempTrain):
        if i < numer:
            # every euclDist has a value smaller
            # than var compare, then var compare will
            # save the value of euclDist
            if euclDist(tempTrain[i], test) < compare:
                compare = euclDist(tempTrain[i], test)
                pred = classTrain[i][0]
                id = i

            # if iteration reaches maximum value of var numer or K,
            # var resultPred will add an index and a class of train data
            if i == numer - 1 or i == len(tempTrain) - 1:
                resultPred['ID'].append(id)
                resultPred['pred'].append(pred)
                numer += numberOfK

                # reset variable
                compare = 1
                pred = 0
                id = 0

    # to know how many classes on the data train as a key
    # and split by each key
    # example:
    # {
    #  '0':25
    #  '1':30
    # }
    countClass = {}
    for i, c in enumerate(kindClass):
        c = c[0]
        if c not in countClass.keys():
            countClass[c] = 0
        for pred in resultPred['pred']:
            if c == pred:
                countClass[c] += 1

    # choose a class that has more value
    predClass = 0
    compareClass = 0
    for i, c in enumerate(countClass.keys()):
        if i == 0:
            compareClass = countClass.get(c)
            predClass = c

        if countClass.get(c) > compareClass:
            compareClass = countClass.get(c)
            predClass = c

    return predClass

# train is an input for train data
# classTrain is an input for actual class of train data
# test is an input for test data
# K is a number of K in K-Neasrest Neighbor
def classification(train, classTrain, test, K):
    prediction = []
    for i, d in enumerate(test):
        prediction.append(classify(train, d, classTrain, K))
    return prediction

# to check the distributon of data
def fold(data, classdata, iter, kFold):
    train, test = [], []
    cTrain, cTest = [], []
    for i, t in enumerate(data.values):
        if (i >= round(float(len(data.values)) / kFold, 0) * (iter-1)) and (i < round(float(len(data.values)) / kFold, 0) * iter):
            test.append(t)
            cTest.append(classdata.values[i])
        else:
            train.append(t)
            cTrain.append(classdata.values[i])
    return np.asarray(train), np.asarray(test), np.asarray(cTrain), np.asarray(cTest)

# TEST TRAINING DATA WITH ITS TRAINING DATA TO CHECK DISTRIBUTION OF DATA
normTrain = normalization(train)
normTest = normalization(test)

kFold = 10
k = 7
for i in range(kFold):
    i += 1
    trytrain, trytest, cTrain, cTest = fold(normTrain, classTrain, i, kFold)
    predictions = classification(trytrain, cTrain, trytest, k)

    # t means prediction and actual class are same
    # f menas prediction and actual class are different
    t, f = 0, 0
    for j in range(len(cTest)):
        if cTest[j] == predictions[j]:
            t += 1
        else:
            f += 1
    print 'Fold', i, 'Accuracy', (float(t)/(t+f)*100), '%'

# TRY TO CLASSIFY THE TESTING DATA
# BECAUSE I DON'T HAVE AN ACTUAL CLASS FOR THIS TESTING DATA
# SO I CAN'T COMPARE THE PREDICTIONS AND ITS ACTUAL CLASSES.
k = 7
predictions = classification(normTrain.values, classTrain.values, normTest.values, k)

# plotting data
# for i, ii in enumerate(normTrain.values[::len(normTrain.values)-3900]):
#     color = 100
#     if classtampung[i] == 0:
#        color = 200
#     plt.scatter(ii[0], ii[1], s=100, c=color)
# plt.scatter(normTest.values[0][0], normTest.values[0][1], s=500)
# plt.show()

# JUST TRY TO MERGE REQUEST