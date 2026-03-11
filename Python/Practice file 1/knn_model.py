'''
k-nearest neighbours(knn model)

Steps for machine learning:-
1) Data gathering
2) Data preprocessing
3) Choose an algorithm
4) Training
5) Testing

'''

from sklearn.datasets import load_iris 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data=load_iris()
print(data) #prints the data
print(data['DESCR']) #description
X=data['data']#input data
Y=data['target']#output data

print(type(X), X.shape, X.ndim) #class, shape and dimensions
knn=KNeighborsClassifier(n_neighbors=9) #default is 5
#splitting the data into training and testing

x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)

print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
#===================
knn.fit(x_train,y_train) #training the model
#predict=knn.predict([[5,4,3,4]])
#print(data['target_names'][predict])
predict=knn.predict(x_test)
print(knn.score(x_train,y_train))
print(accuracy_score(y_test,predict))