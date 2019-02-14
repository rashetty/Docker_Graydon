#!/usr/bin/env python

import sys

'''
Usage: company_probability.py model filename
'''

def predict_company_probability(model, filename):
    '''
    Function to produce probability that one or more companies will move, given the features.
    '''
    import numpy 
    import pandas as pd
    from sklearn import tree
    from sklearn import metrics
    import pickle
    
    clf = pickle.load(open(model, 'rb'))

    company_df = pd.read_csv(filename)
    probability_of_move = clf.predict_proba(company_df)[:, 1]
    return probability_of_move


if __name__ == '__main__':

    print(predict_company_probability(model="model.sav", filename="company.csv"))
