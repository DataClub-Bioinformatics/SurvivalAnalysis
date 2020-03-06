#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

def get(censorInDays, status, years):

    data = pd.DataFrame(censorInDays)
    data['status']=status

    def revalueStatus(row):
        if (row.censorInDays/365>years and int(row.status) == 0):
            return 1
        else:
            return row.status
    
    return(data.apply(revalueStatus, axis=1))

#    print(test)


    
    
