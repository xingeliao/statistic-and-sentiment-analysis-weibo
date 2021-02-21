import csv
import pandas as pd
import numpy as np
import glob
import time
import difflib

def change_date(s):
    if '年' in s:
        s = time.strptime(s, "%Y年%m月%d日 %H:%M")
        year = time.strftime("%Y", s)
        month = time.strftime("%m", s)
        day = time.strftime("%d", s)
        time_value = time.strftime("%H:%M", s)
    elif '月' in s:
        s = time.strptime('2020'+s, "%Y%m月%d日 %H:%M")
        year = time.strftime("%Y", s)
        month = time.strftime("%m", s)
        day = time.strftime("%d", s)
        time_value = time.strftime("%H:%M", s)
    else:
        year = None
        month = None
        day = None
        time_value = None

    return year,month,day, time_value

def change_date_form_and_drop_duplicates(dataset):
    dataset['YEAR'],dataset['MONTH'],dataset['DAY'],dataset['TIME'] = zip(*dataset['DATE & TIME'].apply(change_date))
    dataset = dataset.drop_duplicates(['CONTENT'],keep= 'last')
    dataset = dataset.dropna(subset = ['YEAR'])
    dataset['YEARMONTH'] = dataset['YEAR'] + dataset['MONTH']
    return dataset

def drop_duplicates_more_than_80_percent(alldata):
    thr = 0.8
    alldata['Flag'] = 0
    month = alldata['YEARMONTH'].unique().tolist()
    alldata_no_duplicated = pd.DataFrame()

    for m in month:
        dataonemonth = alldata[alldata['YEARMONTH']== m]

        for text in dataonemonth['CONTENT'].tolist():
            dataonemonth['temp'] = [difflib.SequenceMatcher(None, str(text1),str(text)).ratio() for text1 in dataonemonth['CONTENT'].tolist()]
            dataonemonth.loc[dataonemonth['temp'].gt(thr),['Flag']] = dataonemonth['Flag'].max()+1

        dataonemonth.drop('temp',1)
        dataonemonth= dataonemonth.loc[~dataonemonth['Flag'].duplicated(keep='first')]
        alldata_no_duplicated =  pd.concat([alldata_no_duplicated, dataonemonth])

    return alldata_no_duplicated
