import csv
import pandas as pd
import numpy as np
import glob
import time
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

def count_post(dataset):
    dataset['YEAR'] = dataset['YEAR'].apply(str)
    dataset['MONTH'] = dataset['MONTH'].apply(str)
    dataset['YEARMONTH'] = dataset['YEARMONTH'].apply(str)

    countyear = dataset['YEAR'].value_counts()
    countyear = countyear.sort_index()
    countyear = countyear['2017': '2020']

    dataset2 = dataset[(dataset['YEAR'] == '2017') | (dataset['YEAR'] =='2018') | (dataset['YEAR'] =='2019') | (dataset['YEAR'] =='2020')]
    countmonth = dataset2['MONTH'].value_counts()
    countmonth.index = countmonth.index.astype(int)
    countmonth =countmonth.sort_index()
    countmonth = countmonth/4

    dataset2017_2019 = dataset[(dataset['YEAR'] == '2017') | (dataset['YEAR'] =='2018') | (dataset['YEAR'] =='2019')]
    countmonth2017_2019 = dataset2017_2019['MONTH'].value_counts()
    countmonth2017_2019.index = countmonth2017_2019.index.astype(int)
    countmonth2017_2019 =countmonth2017_2019.sort_index()
    countmonth2017_2019 = countmonth2017_2019/3

    countyearmonth = dataset['YEARMONTH'].value_counts()
    countyearmonth =countyearmonth.sort_index()
    countyearmonth = countyearmonth['201701': '202012']

    return countyear, countmonth, countmonth2017_2019, countyearmonth

def draw_countyear(countyear, title = 'Número de Post mentionado a \'Sagrada Familia\' (2017 - 2020) \n', y_lim = 8000):
    plt.style.use('seaborn-paper')
    ax = countyear.plot(linestyle='-', marker = 'o')
    ax.set_title(title)
    ax.set_ylim([0,y_lim])
    ax.set_ylabel('Número de Post')
    ax.set_xlabel('Año')
    ax.plot()
    plt.show()

def draw_countmonth(countmonth, title = 'Número de Post mentionado a \'Sagrada Familia\' (Promedio de 4 años desde 2017 hasta 2020) \n', y_lim = 800):
    plt.style.use('seaborn-paper')
    ax = countmonth.plot(linestyle='-', marker = 'o')
    ax.set_title(title)
#month = ['Jan.','Feb.','Mar.','Apr.','May','June','July','Aug.','Sept.','Oct.','Nov.','Dec.']
    month = ['','JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
    ax.set_xticks(range(0,13,1))
    ax.set_xticklabels(month, rotation = 0)
    ax.set_ylim([0,y_lim])
    ax.set_ylabel('Número de Post')
    ax.set_xlabel('Mes')
    plt.show()

def draw_countyearmonth(countyearmonth, title = 'Número de Post mentionado a \'Sagrada Familia\' (desde 2017 hasta 2020) \n'):
    plt.style.use('seaborn-paper')
    ax = countyearmonth.plot(linestyle='-', marker = 'o')
    ax.set_title(title)
    loc = plticker.MultipleLocator(base=3.0) # this locator puts ticks at regular intervals
    ax.xaxis.set_major_locator(loc)
    xlable = [''] + list(countyearmonth.index.values)[::3]
    ax.set_xticklabels(xlable, rotation = 45)
    ax.set_ylabel('Número de Post')
    ax.set_xlabel('Mes')
    plt.show()
