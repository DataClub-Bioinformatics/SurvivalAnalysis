#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

def plotKaplanMeier(dataFrame, label1, label2) :
    
    #TODO: We want to make this generic so we dont need t and status
    # but instead of one dataframe we want to send in two groups a
    group1=dataFrame[dataFrame['Treatment']==1]
    group2=dataFrame[dataFrame['Treatment']==0]
    T=group1['t']
    print(T)
    E=group1['status']
    print(E)
    T1=group2['t']
    E1=group2['status']

    kmf = KaplanMeierFitter()

    ax = plt.subplot(111)
    ax = kmf.fit(T, E, label = label1).plot(ax=ax)
    ax = kmf.fit(T1, E1, label = label2).plot(ax=ax)
    

