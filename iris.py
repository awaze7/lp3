import numpy as np 
import pandas as pd 
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

#loading dataset 
df= pd.read_csv('iris.csv')

#visualizing dataset
df.head(n=10)

np.unique(df['Species'])

df.shape

df.info()

correl=df.corr()
sns.heatmap(correl,annot=True)


ax = df[df.Species=='Iris-setosa'].plot.scatter(x='SepalLengthCm', y='SepalWidthCm', 
                                                    color='red', label='Iris - Setosa')
df[df.Species=='Iris-versicolor'].plot.scatter(x='SepalLengthCm', y='SepalWidthCm', 
                                                color='green', label='Iris - Versicolor', ax=ax)
df[df.Species=='Iris-virginica'].plot.scatter(x='SepalLengthCm', y='SepalWidthCm', 
                                                color='blue', label='Iris - Virginica', ax=ax)
ax.set_title("Scatter Plot")


df.isnull().sum()

encoder = LabelEncoder()
df['Species'] = encoder.fit_transform(df['Species'])

df

np.unique(df['Species'])

df= df.drop(['Id'], axis = 1)

data = df.values 

X=data [:, 0:5]
Y= data [: , -1]

print(X.shape)
print(Y.shape)

#train-test split = 3:1 

train_x = X[: 112, ]
train_y = Y[:112, ]

test_x = X[112:150, ]
test_y = Y[112:150, ]

print(train_x.shape)
print(train_y.shape)
print(test_x.shape)
print(test_y.shape)



kmeans = KMeans(n_clusters=3)
kmeans.fit(train_x, train_y)

# training predictions
train_labels= kmeans.predict(train_x)

#testing predictions
test_labels = kmeans.predict(test_x)


print(accuracy_score(train_y, train_labels)*100)

print(accuracy_score(test_labels, test_y)*100)


print(classification_report(train_y, train_labels))



#Precision: Precision measures the accuracy of positive predictions.
#It's the ratio of true positives to the sum of true positives and false positives. 
#A high precision indicates that when the model predicts a positive class, it's likely to be correct.
#  TP/(TP+FP)

#Recall: Recall (or sensitivity) measures the ability of the model to identify all relevant instances. 
#It's the ratio of true positives to the sum of true positives and false negatives. 
#A high recall indicates that the model can find most of the positive instances.
#TP/(TP+FN)


#F1-Score: The F1-Score is the harmonic mean of precision and recall.
#It provides a balance between precision and recall. 
#It's useful when you want to consider both false positives and false negatives.
# (2×precision×recall) / (precision+recall)

#Support: Support is the number of actual occurrences of each class in the dataset.
#It's the number of samples for each class.
















