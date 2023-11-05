import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier





df = pd.read_csv("D://BE//dataset//emails.csv")



df.head()



df.isnull().sum()


X = df.iloc[:,1:3001]
X



Y = df.iloc[:,-1].values
Y

train_x,test_x,train_y,test_y = train_test_split(X,Y,test_size = 0.25)


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=42)



knn = KNeighborsClassifier(n_neighbors=7)


knn.fit(X_train, y_train)


print(knn.predict(X_test))

print(knn.score(X_test, y_test))



from sklearn.metrics import confusion_matrix
y_pred = knn.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)














