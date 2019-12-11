## NLP - Scraping GitHub for Programming Languages
##### By Fred & Misty - Super Fantastic Team 

#CHANGE 1

predictons = run_the_model(X_train, train.actual) 

pickle.dump(model, open(filename, 'wb'))

def run_the_model(X,y):
    """
    We'll have to pick some classification models to use on the train-test sets.
    """
    tree = DecisionTreeClassifier(max_depth=7).fit(X, y)
    predictions = tree.predict(X)
    return predictions
