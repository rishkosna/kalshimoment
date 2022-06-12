import json
import requests
import pandas
pandas.options.mode.chained_assignment = None  # default='warn'
import numpy
from datetime import *

def simplify_date (str) :
    y = int(str[:4])
    m = int(str[5:7])
    d = int(str[8:10])
    new = date(y,m,d)
    return new

def simplify_time (str) :
    h = int(str[11:13])
    m = int(str[14:16])
    s = int(str[17:19])
    new = time(h,m,s)
    return new

def simple_df (df) :
    now = datetime.now()
    df['create_time'] = df['create_date'].apply(simplify_time)
    df['close_time'] = df['close_date'].apply(simplify_time)
    df['create_date'] = df['create_date'].apply(simplify_date)
    df['close_date'] = df['close_date'].apply(simplify_date)
    df.drop(df.index[df['close_date'] < date.today()], inplace=True)
    