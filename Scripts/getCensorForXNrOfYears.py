#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

# I prefer to see what the function wants in input parameters clearly
def getStatusForXYears(censorInDays, status, years):

    #creates a data frame for simplicity again probably a simple way to do in one row but works as is
    data=pd.DataFrame(censorInDays)
    data['status']=status

    #this func checks if patient has lived for more than given years but has died
    #after if so, change status for patient else return status
    def revalueStatus(row):
        if (row.censorInDays/365>years):
           # row.censorInDays=years*365
            if (int(row.status) == 0):
                row.status=1
    
    #call and return revalued status for all patients
    data.apply(revalueStatus, axis=1)
    return data


    
    
