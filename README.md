
### Try to learn about KNN, dataset comes from my friend that use this dataset for college assignment
### The result not too bad, but i think it can be improve to get the higher accuracy


```python
import pandas
import math
import numpy as np
rawTrain = pandas.read_excel("dataset.xlsx", sheetname=0)
rawTest = pandas.read_excel("dataset.xlsx", sheetname=1)
```


```python
print rawTrain
```

         Berita  Like  Provokasi  Komentar  Emosi  Hoax
    0     B0001    29         66        52     70     1
    1     B0002    27         23        74     52     1
    2     B0003    19         43        54     33     0
    3     B0004    21         90        90     85     1
    4     B0005    27         56        49     53     0
    5     B0006    13         34        80     30     0
    6     B0007    40         69        47     70     1
    7     B0008    22         21        79     64     0
    8     B0009    30         97        45     82     0
    9     B0010    27         66        43     45     0
    10    B0011    12         34        56     49     0
    11    B0012    12         28        82     44     0
    12    B0013    10         22        70     54     0
    13    B0014    20         38        82     47     1
    14    B0015    14         50        75     63     0
    15    B0016    23         48        57     48     1
    16    B0017    39         67        48     70     0
    17    B0018    18         50        66     67     0
    18    B0019    13         45        54     47     0
    19    B0020    21         51        87     69     0
    20    B0021    33         90        55     85     1
    21    B0022    28         32        89     66     0
    22    B0023    24         57        84     40     0
    23    B0024    32         78        90     84     1
    24    B0025    40         68        63     80     1
    25    B0026    39         55        63     79     1
    26    B0027    13         42        75     65     0
    27    B0028    21         71        55     84     1
    28    B0029    26         54        75     66     1
    29    B0030    16         67        52     54     1
    ...     ...   ...        ...       ...    ...   ...
    3970  B3971    23         57        55     78     1
    3971  B3972    28         68        50     64     0
    3972  B3973    18         69        61     60     0
    3973  B3974    39         51        57     60     1
    3974  B3975    13         50        62     53     0
    3975  B3976    20         55        57     65     0
    3976  B3977    28         87        73     89     0
    3977  B3978    36         50        68     61     0
    3978  B3979    28         51        41     48     0
    3979  B3980    29         94        86     84     1
    3980  B3981    23         80        59     63     0
    3981  B3982    32         82        52     55     1
    3982  B3983    22         23        47     40     0
    3983  B3984    31         89        81     84     1
    3984  B3985    40         88        49     54     1
    3985  B3986    20         88        80     82     1
    3986  B3987    20         43        71     66     0
    3987  B3988    16         29        87     42     0
    3988  B3989    26         56        43     68     1
    3989  B3990    30         61        63     60     1
    3990  B3991    20         31        82     48     0
    3991  B3992    28         26        65     31     0
    3992  B3993    23         63        72     55     0
    3993  B3994    12         64        60     44     0
    3994  B3995    23         47        59     38     1
    3995  B3996    16         38        80     66     0
    3996  B3997    20         69        42     56     0
    3997  B3998    26         88        75     69     1
    3998  B3999    20         54        82     55     0
    3999  B4000    21         76        84     50     0
    
    [4000 rows x 6 columns]



```python
print rawTest
```

        Berita  Like  Provokasi  Komentar  Emosi Hoax
    0    B4001    14         55        68     45    ?
    1    B4002    18         76        72     74    ?
    2    B4003    36         68        68     69    ?
    3    B4004    18         43        45     56    ?
    4    B4005    18         62        71     45    ?
    5    B4006    36         67        56     61    ?
    6    B4007    10         55        71     61    ?
    7    B4008    13         40        51     72    ?
    8    B4009    35         36        73     61    ?
    9    B4010    10         62        64     71    ?
    10   B4011    34         85        54     72    ?
    11   B4012    11         76        74     70    ?
    12   B4013    18         31        53     77    ?
    13   B4014    17         53        62     64    ?
    14   B4015    12         55        54     62    ?
    15   B4016    36         85        74     73    ?
    16   B4017    31         81        44     62    ?
    17   B4018    11         40        75     70    ?
    18   B4019    18         57        58     64    ?
    19   B4020    12         22        70     79    ?
    20   B4021    32         47        44     70    ?
    21   B4022    32         84        58     70    ?
    22   B4023    11         65        66     50    ?
    23   B4024    14         57        49     42    ?
    24   B4025    20         54        51     67    ?
    25   B4026    24         32        69     54    ?
    26   B4027    36         96        54     80    ?
    27   B4028    35         30        62     72    ?
    28   B4029    11         25        58     66    ?
    29   B4030    30         97        59     80    ?
    ..     ...   ...        ...       ...    ...  ...
    970  B4971    17         22        51     65    ?
    971  B4972    37         71        78     65    ?
    972  B4973    18         29        67     70    ?
    973  B4974    17         65        52     60    ?
    974  B4975    10         57        59     79    ?
    975  B4976    13         74        47     44    ?
    976  B4977    12         70        72     75    ?
    977  B4978    38         88        66     70    ?
    978  B4979    36         66        66     61    ?
    979  B4980    19         56        73     48    ?
    980  B4981    14         79        72     52    ?
    981  B4982    30         43        72     73    ?
    982  B4983    32         36        68     76    ?
    983  B4984    10         49        65     64    ?
    984  B4985    36         32        46     74    ?
    985  B4986    37         53        65     67    ?
    986  B4987    19         41        44     42    ?
    987  B4988    16         29        79     55    ?
    988  B4989    13         35        71     60    ?
    989  B4990    11         29        74     56    ?
    990  B4991    30         39        47     72    ?
    991  B4992    38         47        58     72    ?
    992  B4993    39         49        52     64    ?
    993  B4994    36         76        40     68    ?
    994  B4995    16         42        72     47    ?
    995  B4996    33         63        68     72    ?
    996  B4997    34         68        56     76    ?
    997  B4998    10         29        40     52    ?
    998  B4999    34         52        74     75    ?
    999  B5000    40         74        80     78    ?
    
    [1000 rows x 6 columns]



```python
train = pandas.DataFrame(rawTrain, columns=['Like','Provokasi','Komentar','Emosi'])
print train
```

          Like  Provokasi  Komentar  Emosi
    0       29         66        52     70
    1       27         23        74     52
    2       19         43        54     33
    3       21         90        90     85
    4       27         56        49     53
    5       13         34        80     30
    6       40         69        47     70
    7       22         21        79     64
    8       30         97        45     82
    9       27         66        43     45
    10      12         34        56     49
    11      12         28        82     44
    12      10         22        70     54
    13      20         38        82     47
    14      14         50        75     63
    15      23         48        57     48
    16      39         67        48     70
    17      18         50        66     67
    18      13         45        54     47
    19      21         51        87     69
    20      33         90        55     85
    21      28         32        89     66
    22      24         57        84     40
    23      32         78        90     84
    24      40         68        63     80
    25      39         55        63     79
    26      13         42        75     65
    27      21         71        55     84
    28      26         54        75     66
    29      16         67        52     54
    ...    ...        ...       ...    ...
    3970    23         57        55     78
    3971    28         68        50     64
    3972    18         69        61     60
    3973    39         51        57     60
    3974    13         50        62     53
    3975    20         55        57     65
    3976    28         87        73     89
    3977    36         50        68     61
    3978    28         51        41     48
    3979    29         94        86     84
    3980    23         80        59     63
    3981    32         82        52     55
    3982    22         23        47     40
    3983    31         89        81     84
    3984    40         88        49     54
    3985    20         88        80     82
    3986    20         43        71     66
    3987    16         29        87     42
    3988    26         56        43     68
    3989    30         61        63     60
    3990    20         31        82     48
    3991    28         26        65     31
    3992    23         63        72     55
    3993    12         64        60     44
    3994    23         47        59     38
    3995    16         38        80     66
    3996    20         69        42     56
    3997    26         88        75     69
    3998    20         54        82     55
    3999    21         76        84     50
    
    [4000 rows x 4 columns]



```python
classTrain = pandas.DataFrame(rawTrain, columns=['Hoax'])
print classTrain
```

          Hoax
    0        1
    1        1
    2        0
    3        1
    4        0
    5        0
    6        1
    7        0
    8        0
    9        0
    10       0
    11       0
    12       0
    13       1
    14       0
    15       1
    16       0
    17       0
    18       0
    19       0
    20       1
    21       0
    22       0
    23       1
    24       1
    25       1
    26       0
    27       1
    28       1
    29       1
    ...    ...
    3970     1
    3971     0
    3972     0
    3973     1
    3974     0
    3975     0
    3976     0
    3977     0
    3978     0
    3979     1
    3980     0
    3981     1
    3982     0
    3983     1
    3984     1
    3985     1
    3986     0
    3987     0
    3988     1
    3989     1
    3990     0
    3991     0
    3992     0
    3993     0
    3994     1
    3995     0
    3996     0
    3997     1
    3998     0
    3999     0
    
    [4000 rows x 1 columns]



```python
test = pandas.DataFrame(rawTest, columns=['Like','Provokasi','Komentar','Emosi'])
print test
```

         Like  Provokasi  Komentar  Emosi
    0      14         55        68     45
    1      18         76        72     74
    2      36         68        68     69
    3      18         43        45     56
    4      18         62        71     45
    5      36         67        56     61
    6      10         55        71     61
    7      13         40        51     72
    8      35         36        73     61
    9      10         62        64     71
    10     34         85        54     72
    11     11         76        74     70
    12     18         31        53     77
    13     17         53        62     64
    14     12         55        54     62
    15     36         85        74     73
    16     31         81        44     62
    17     11         40        75     70
    18     18         57        58     64
    19     12         22        70     79
    20     32         47        44     70
    21     32         84        58     70
    22     11         65        66     50
    23     14         57        49     42
    24     20         54        51     67
    25     24         32        69     54
    26     36         96        54     80
    27     35         30        62     72
    28     11         25        58     66
    29     30         97        59     80
    ..    ...        ...       ...    ...
    970    17         22        51     65
    971    37         71        78     65
    972    18         29        67     70
    973    17         65        52     60
    974    10         57        59     79
    975    13         74        47     44
    976    12         70        72     75
    977    38         88        66     70
    978    36         66        66     61
    979    19         56        73     48
    980    14         79        72     52
    981    30         43        72     73
    982    32         36        68     76
    983    10         49        65     64
    984    36         32        46     74
    985    37         53        65     67
    986    19         41        44     42
    987    16         29        79     55
    988    13         35        71     60
    989    11         29        74     56
    990    30         39        47     72
    991    38         47        58     72
    992    39         49        52     64
    993    36         76        40     68
    994    16         42        72     47
    995    33         63        68     72
    996    34         68        56     76
    997    10         29        40     52
    998    34         52        74     75
    999    40         74        80     78
    
    [1000 rows x 4 columns]



```python
def normalization(t):
    col = t.keys()
    returnT = {}
    for i in range(len(col)):
        data = [d[0] for d in pandas.DataFrame(t, columns=[col[i]]).values]
        maxVal = max(data)
        minVal = min(data)
        normData = []
        for d in data:
            normData.append(float(d-minVal)/(maxVal-minVal))
        returnT[col[i]] = normData
    return pandas.DataFrame(returnT)
```


```python
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
```


```python
# to predict each test data
# it only works when you normalized all the data
# if you won't to normalize the data, adjust 'compare' variable
def classify(train, test, classTrain, numberOfK):
    tempTrain = train[:len(train)-1]
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
        'ID':[],
        'pred':[]
    }

    compare = 1 # change this value if you dont use normalization function
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
            if i == numer-1 or i == len(tempTrain)-1:
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
```


```python
# train is an input for train data
# classTrain is an input for actual class of train data
# test is an input for test data
# K is a number of K in K-Neasrest Neighbor
def classification(train, classTrain, test, K):
    prediction = []
    for i, d in enumerate(test):
        prediction.append(classify(train, d, classTrain, K))
    return prediction
```


```python
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
```


```python
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
```

    Fold 1 Accuracy 68.75 %
    Fold 2 Accuracy 72.75 %
    Fold 3 Accuracy 70.0 %
    Fold 4 Accuracy 67.75 %
    Fold 5 Accuracy 67.75 %
    Fold 6 Accuracy 71.0 %
    Fold 7 Accuracy 73.0 %
    Fold 8 Accuracy 67.75 %
    Fold 9 Accuracy 73.0 %
    Fold 10 Accuracy 69.25 %



```python
# TRY TO CLASSIFY THE TESTING DATA
# BECAUSE I DON'T HAVE AN ACTUAL CLASS FOR THIS TESTING DATA
# SO I CAN'T COMPARE THE PREDICTIONS AND ITS ACTUAL CLASSES.
k = 7
predictions = classification(normTrain.values, classTrain.values, normTest.values, k)
```
