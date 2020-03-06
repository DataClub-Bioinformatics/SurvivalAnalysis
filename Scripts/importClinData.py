#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd 
from datetime import date  
import getCensorForXNrOfYears as censor
import math

# Path to file change where your clin data file is
path = "/Users/VictorPonten/code/Bioinf/data/bomiClin.csv"

# Read file with separator ;
clinData = pd.read_csv(path,sep=';') 

# Remove exessive rows and columns
clinData.columns = clinData.astype(str).columns.str.replace(':','')
clinData = clinData.loc[:, ~clinData.columns.str.contains('^Unnamed')]
clinData = clinData.loc[:, ~clinData.columns.str.contains('Kommentar')]
clinData = clinData[clinData.Projektnr.notna()]

# return NaN or inf
def isNaN(num):
    return num != num

# calculates days from surgery to death or censor
def getCensorDays(row):
    if (isNaN(row['Vital date']) or isNaN(row['Surgery date'])):
         return math.nan
    else:
     #    print(clinData['Vital date:'])
        return (date.fromisoformat(row['Vital date']) - date.fromisoformat(row['Surgery date'])).days

# this function returns opposite status
def invertStatus(num):
    return abs(num-1)

# get censor and status columns and merge into one dataframe
clinData['censorInDays']=clinData.apply(getCensorDays, axis=1)

# remove if censor in days is NaN for some reason
clinData = clinData[clinData.censorInDays.notna()]

# I think its more inutitive when dead is 0 and alive is 1
clinData.Status=clinData.Status.apply(invertStatus).astype(int)

#remove less than 10(?) in days because cause of death is uncertain
clinData = clinData[clinData.censorInDays>10]

# input censor and status for x years and return current status
clinData['3yrSurvival'] = censor.getStatusForXYears(clinData.censorInDays, clinData.Status, 3)

