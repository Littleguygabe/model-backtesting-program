import yfinance as yf
import pandas as pd
import random
import numpy as np

ticker_list = ['AAPL','MSFT','TSLA','AMZN']

for tic_string in ticker_list:
    ticker = yf.Ticker(tic_string)
    data = ticker.history(period='1500d',interval='1d')
    data['Ticker'] = tic_string

    data['Indicator'] = np.random.choice([-1,0,1],size = len(data))
    data['OrderVal'] = np.random.uniform(low=10,high=200,size=len(data))

    data.to_csv(f'backtestingData/syntheticData/{tic_string}.csv')