#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#In this script we want to collect different ways to split the clinical data
#for survival analysis. for now, we only have Median for a clin value
#But in the future, we want new functions for a 
# - specific cutoff value for a clinical parameter
# - combination of several parameters
# - other useful discriminators than median. (quartiles, mean, etc..)

#We might want to move these functions into the kaplanMeier script directly
#Later

import statistics
import plots.kaplanMeier as km

def forMedianClinParameter(clinData, parameterStr, years, group1Name='default', group2Name='default'):
    medianForParameter = statistics.median(clinData[parameterStr])
    
    group1 = clinData[medianForParameter>clinData[parameterStr]]
    group2 = clinData[medianForParameter<=clinData[parameterStr]]
    
    name1 = group1Name if group1Name != 'default' else parameterStr+"_low"
    name2 = group2Name if group2Name != 'default' else parameterStr+"_high"
    
    km.plotKaplanMeier(group1, group2, name1, name2, years)

#TODO:S
#def forCutoffClinParameter(clinData, parameterStr, cutoff, years, **nameArgs):
    #needs to return print ("given cutoff is outside of range")
    #do same as Median but other value




