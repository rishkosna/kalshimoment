# Kalshi API: https://kalshi-public-docs.s3.amazonaws.com/KalshiAPI.html

import json
import requests
import pandas
pandas.options.mode.chained_assignment = None  # default='warn'
import numpy
from datetime import *
from KalshiClientsBase import ExchangeClient
import config
from misc import simple_df
from IPython.display import display

# info for log in, entered through config
username = config.username
password = config.password
base_url = "https://trading-api.kalshi.com"

# log in
client = ExchangeClient(base_url, username, password)

# read in markets through api (array of json objects) and covert to pandas dataframe
market_data = client.get_public_markets()
df_unfiltered = pandas.json_normalize(market_data, record_path=['markets'])
df = df_unfiltered[['id', 'category', 'mini_title', 'yes_ask', 'create_date', 'close_date']]
simple_df(df)
display(df)