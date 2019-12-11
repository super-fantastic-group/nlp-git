import pandas as pd 
import numpy as np 


def count_percent(df):
    labels = pd.concat([df.language.value_counts(), df.language.value_counts(normalize=True)], axis=1)
    labels.columns = ['n', 'percent']
    return labels