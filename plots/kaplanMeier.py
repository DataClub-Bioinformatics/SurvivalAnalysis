#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt
import Scripts.getCensorForXNrOfYears as censor
from numpy import linspace

def plotKaplanMeier(dataFrame1, dataFrame2, label1, label2, years):
    
  # input censor and status for x years and return current status
    time = linspace(0,years)
    d1=censor.getStatusForXYears(dataFrame1.censorInDays, dataFrame1.Status, 3)
    d2=censor.getStatusForXYears(dataFrame2.censorInDays, dataFrame2.Status, 3)
    T=d1.censorInDays/365
    E=d1.status
    T1=d2.censorInDays/365
    E1=d2.status
    kmf = KaplanMeierFitter()

    ax = plt.subplot(111)
    ax = kmf.fit(T, E, timeline = time, label = label1).plot(ax=ax)
    ax = kmf.fit(T1, E1, timeline =time, label = label2).plot(ax=ax)
    

