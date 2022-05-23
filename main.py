from turtle import mode

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

#from keras import layers
#from keras import models
#from keras import optimizers
#from keras import losses
#from keras import metrics


#def NN():
    # split an additional validation dataset
    #x_partial_train, x_validation ,y_partial_train ,y_validation= train_test_split(x_train, y_train, test_size=0.3, random_state=0)
    #model = models.Sequential()
    #model.add(layers.Dense(16, activation='relu', input_shape=(490,)))
    #model.add(layers.Dense(16, activation='relu'))
    #model.add(layers.Dense(1, activation='sigmoid'))
    #model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
    #model.fit(x_partial_train, y_partial_train, epochs=4, batch_size=10, validation_data=(x_validation, y_validation))
    #print("score on test: " + str(model.evaluate(x_test, y_test)[1]))
    #print("score on train: " + str(model.evaluate(x_train, y_train)[1]))


def RandomForestClassifier_Model():
    # n_estimators = number of decision trees
    LR_model = RandomForestClassifier(n_estimators=35, max_depth=7)
    LR_model.fit(x_train, y_train)
    print("RandomForest Score: ", LR_model.score(x_test, y_test))
    LR_model.predict(new_data)


def Decision_Tree_Classifier_Model():
    DT_model = DecisionTreeClassifier()
    DT_model.fit(x_train, y_train)
    print("Decision_Tree Score: ", DT_model.score(x_test, y_test))


def KNN_Classifier_Model():
    KNN_model = KNeighborsClassifier(n_neighbors=31)
    KNN_model.fit(x_train, y_train)
    print("KNN Score: ", KNN_model.score(x_test, y_test))


def GaussianNB_Classifier_Model():
    NB_model = GaussianNB()
    NB_model.fit(x_train, y_train)
    print("GaussianNB Score: ", NB_model.score(x_test, y_test))


def LogisticRegression_Model():
    LR_model = LogisticRegression(max_iter=1000)
    LR_model.fit(x_train, y_train)
    print("LogisticRegression Score: ", LR_model.score(x_test, y_test))


def SVM():
    SVM_model = LinearSVC(C=0.0001, dual=False)
    SVM_model.fit(x_train, y_train)
    print("SVM Score: ", SVM_model.score(x_test, y_test))


def BaggingClassifier_Model():
    # max_samples: maximum size 0.5=50% of each sample taken from the full dataset
    # max_features: maximum of features 1=100% taken here all 10K
    # n_estimators: number of decision trees
    bagging_model = BaggingClassifier(DecisionTreeClassifier(), max_samples=0.5, max_features=1.0, n_estimators=7)
    bagging_model.fit(x_train, y_train)
    print("Bagging Score: ", bagging_model.score(x_test, y_test))


def VotingClassifier_Model():
    # 1) naive bias = NB_model
    # 2) logistic regression =LR_model
    # 3) random forest =LR_model
    # 4) support vector machine = SVM_model
    evc = VotingClassifier(estimators=[('mnb', GaussianNB()), ('lr', LogisticRegression(max_iter=1000)),
                                       ('rf', RandomForestClassifier(n_estimators=35, max_depth=7))], voting='hard')
    evc.fit(x_train, y_train)
    print("voting score: " + str(evc.score(x_test, y_test)))

# read data
data = pd.read_csv('Train data.csv')

# read new customers
new_data = pd.read_csv('New Customer.csv')


# preprocessing
# # Handle  Missing values

# ##Gender
# --> remove non values
data.dropna(subset=['Gender'], inplace=True)

# --> replace with most repeated value
# val = data['Gender'].mode()[0]
# data['Gender'].fillna(val, inplace=True)


# ##Married
# --> remove non values
data.dropna(subset=['Married'], inplace=True)

# --> replace with most repeated value
# val = data['Married'].mode()[0]
# data['Married'].fillna(val, inplace=True)


# ##Dependents
# --> replace with 0
data['Dependents'].fillna(0, inplace=True)

# --> replace with most repeated value
# val = data['Dependents'].mode()[0]
# data['Dependents'].fillna(val, inplace=True)


# ##Education
# --> remove non values
data.dropna(subset=['Education'], inplace=True)

# --> replace with most repeated value
# val = data['Education'].mode()[0]
# data['Education'].fillna(val, inplace=True)


# ##Self_Employed
# --> remove non values
data.dropna(subset=['Self_Employed'], inplace=True)

# --> replace with most repeated value
# val = data['Self_Employed'].mode()[0]
# data['Self_Employed'].fillna(val, inplace=True)

# --> replace with zero
# data['Self_Employed'].fillna(0, inplace=True)


# ##ApplicantIncome
# --> remove non values
data.dropna(subset=['ApplicantIncome'], inplace=True)

# --> replace with median
# val = data['ApplicantIncome'].median()
# data['ApplicantIncome'].fillna(val, inplace=True)


# ##CoapplicantIncome
# --> replace with zero
data['CoapplicantIncome'].fillna(0, inplace=True)

# --> replace with median
# val = data['CoapplicantIncome'].median()
# data['CoapplicantIncome'].fillna(val, inplace=True)


# ##LoanAmount
# --> remove non values
data.dropna(subset=['LoanAmount'], inplace=True)

# ##Loan_Amount_Term
# --> remove non values
data.dropna(subset=['Loan_Amount_Term'], inplace=True)

# ##Credit_History
# --> remove non values
data.dropna(subset=['Credit_History'], inplace=True)

# ##Property_Area
# --> remove non values
data.dropna(subset=['Property_Area'], inplace=True)

# --> replace with most repeated value
# val = data['Property_Area'].mode()[0]
# data['Property_Area'].fillna(val, inplace=True)


# calculate lift score
# from mlxtend.evaluate import lift_score
# print(data.to_string())
# lift = lift_score(data.iloc[:, 1], data.iloc[:, -1])
# lift


# # Handle  Wrong format
# --> Encoding

categorical_columns = [data['Gender'], data['Married'], data['Education'], data['Property_Area'], data['Self_Employed'], data['Loan_Status']]
df=pd.DataFrame(categorical_columns,columns=['Gender','Married','Education', 'Property_Area', 'Self_Employed', 'Loan_Status'])

#labelEncoder = LabelEncoder()
labelEncoder=OneHotEncoder(categories = "auto", handle_unknown = "ignore",sparse=False)
labelEncoder.fit_transform(df)

data['Gender'] = labelEncoder.transform(data['Gender'])

#labelEncoder.fit(data['Married'])
data['Married'] = labelEncoder.transform(data['Married'])

#labelEncoder.fit(data['Education'])
data['Education'] = labelEncoder.transform(data['Education'])

#labelEncoder.fit(data['Property_Area'])
data['Property_Area'] = labelEncoder.transform(data['Property_Area'])

#labelEncoder.fit_transform(data['Self_Employed'])
data['Self_Employed'] = labelEncoder.transform(data['Self_Employed'])

#labelEncoder.fit(data['Loan_Status'])
data['Loan_Status'] = labelEncoder.transform(data['Loan_Status'])

# --> Handle Dependents +3 category
Dependents_list = list(data.iloc[:, 3])
# print(Dependents_list)
for i in range(len(Dependents_list)):
    if Dependents_list[i] != '0' and Dependents_list[i] != '1' and Dependents_list[i] != '2':
        Dependents_list[i] = '3'

data['Dependents'] = Dependents_list

# split data into train data and test data
x = data.iloc[:, 1: -1]
y = data.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

# new customers encoding
#new_data['Gender'] = labelEncoder.transform(new_data['Gender'])
new_data['Married'] = labelEncoder.transform(new_data['Married'])
new_data['Education'] = labelEncoder.transform(new_data['Education'])
new_data['Self_Employed'] = labelEncoder.transform(new_data['Self_Employed'])
new_data['Property_Area'] = labelEncoder.transform(new_data['Property_Area'])


Decision_Tree_Classifier_Model()
KNN_Classifier_Model()
GaussianNB_Classifier_Model()
LogisticRegression_Model()
SVM()
BaggingClassifier_Model()
RandomForestClassifier_Model()
VotingClassifier_Model()
#NN()
