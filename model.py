from pprint import pprint

import pandas as pd
import numpy as np
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn import preprocessing

def encode_categories(column):
    """
    Takes a Pandas series of string variables and turns them into a number that represents each unique string. 
    """
    le = preprocessing.LabelEncoder()
    return le.fit_transform(column)

def make_one_hot_encoding(column):
    return pd.get_dummies(column,prefix=['Catergory:'])

def create_tfidf_feature_matrix(series):
    """
    Accepts a column, finds the tf-idf of all the terms in each row/document. The values are made into
    a DataFrame that is as wide as there are words in all the documents.
    """
    tfidf = TfidfVectorizer() 
    tfidfs = tfidf.fit_transform(series.values)
    feature_matrix = pd.DataFrame(tfidfs.todense(), columns=tfidf.get_feature_names())
    return feature_matrix

def make_model_components(feature_variable, target_variable):
    """
    Takes the one column as the feature matrix, one column as target variable. Splits them into test-train.
    Creates a dataframe for the Test and Train of the target variables (y_train, y_test)
    """
    tfidf = TfidfVectorizer()
    tfidfs = tfidf.fit_transform(feature_variable.values)
    X = pd.DataFrame(tfidfs.todense(), columns=tfidf.get_feature_names())
    y = target_variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2)
    train = pd.DataFrame(dict(actual=y_train))
    test = pd.DataFrame(dict(actual=y_test))
    return X_train, X_test, train, test

def run_the_model(X,y,depth=7):
    """
    We'll have to pick some classification models to use on the train-test sets.
    """
    tree = DecisionTreeClassifier(max_depth=depth).fit(X, y)
    predictions = tree.predict(X)
    return predictions


def score_your_model(actual, predicted):
    """
    A bunch of the sklearn metrics functions that show how well our model's predictions compare to their
    actual values. Returns nothing. Just prints out a nicely formatted block of classification scores.
    """
    print('Accuracy: {:.2%}'.format(accuracy_score(actual, predicted)))
    print('---')
    #A matrix that shows where the prediction compare to what they should acutally be
    print('Confusion Matrix')
    print(pd.crosstab(predicted, actual))
    print('---')
    #A readout of precision and recall.
    print(classification_report(actual, predicted))