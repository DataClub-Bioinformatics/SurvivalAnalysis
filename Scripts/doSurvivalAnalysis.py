#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#TODO: we need to take the dataframe from importClinData and devide in two
#and make it fit into the kaplanMeier plot. Lets start by doing age and 3yearSurv

#1. calculate the median age
#2. split clinData or just new dataframe with only censor and status by median age
#3. make data frame fit to function or modify plot function
#4. test to see if it works

#seudo dataframe1 = clin[medianAge>clin.age]
#code  dataframe2 = clin[~medianAge>clin.age]
#      dataframefitted = dataframes #modify stuff
#      plot.kaplanMeier(dataframeFitted)

