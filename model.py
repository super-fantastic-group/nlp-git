from pprint import pprint

import pandas as pd
import numpy as np
import re

%matplotlib inline
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score


def create_tfidf_feature_matrix(series):
    tfidf = TfidfVectorizer() 
    tfidfs = tfidf.fit_transform(series.values)
    feature_matrix = pd.DataFrame(tfidfs.todense(), columns=tfidf.get_feature_names())
    return feature_matrix

def make_model_components(feature_variable, target_variable):
    X = tfidf.fit_transform(feature_variable)
    y = target_variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=.2)
    train = pd.DataFrame(dict(actual=y_train))
    test = pd.DataFrame(dict(actual=y_test))

def run_the_model():
    """
    We'll have to pick some classification models to use on the train-test sets.
    """
    pass


def score_your_model(acutal, predicted):
    print('Accuracy: {:.2%}'.format(accuracy_score(actual, predicted)))
    print('---')
    #A matrix that shows where the prediction compare to what they should acutally be
    print('Confusion Matrix')
    print(pd.crosstab(predicted, actual))
    print('---')
    #A readout of precision and recall.
    print(classification_report(actual, predicted))