#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd 
from datetime import *  

# Path to file change where your clin data file is
path = "/Users/VictorPonten/code/Bioinf/data/bomiClin.csv"

# Read file with separator ;
clinData = pd.read_csv(path,sep=';') 

# Remove exessive rows and columns
clinData = clinData.loc[:, ~clinData.columns.str.contains('^Unnamed')]
clinData = clinData.loc[:, ~clinData.columns.str.contains('Kommentar')]
clinData = clinData[clinData['Projektnr:'].notna()]

def isNaN(num):
    return num != num

def getCensorDays(row):
    if (isNaN(row['Vital date:']) or isNaN(row['Surgery date:'])):
        return 'nan'
    else:
    #    print(clinData['Vital date:'])
        return (date.fromisoformat(row['Vital date:']) - date.fromisoformat(row['Surgery date:'])).days


# get censor and status columns and merge into one dataframe
clinData['censorDay']=clinData.apply(getCensorDays, axis=1)



