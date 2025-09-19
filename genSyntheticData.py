import yfinance as yf
import pandas as pd
import random
import numpy as np
import os


ticker_list = [
    # Mega-Cap Tech
    "AAPL",  # Apple Inc.
    "MSFT",  # Microsoft Corporation
    "GOOGL", # Alphabet Inc. (Class A)
    "GOOG",  # Alphabet Inc. (Class C)
    "AMZN",  # Amazon.com, Inc.
    "NVDA",  # NVIDIA Corporation
    "META",  # Meta Platforms, Inc.
    "TSLA",  # Tesla, Inc.
    
    # Semiconductors
    "TSM",   # Taiwan Semiconductor Manufacturing Company
    "AVGO",  # Broadcom Inc.
    "QCOM",  # QUALCOMM Incorporated
    "AMD",   # Advanced Micro Devices, Inc.
    "INTC",  # Intel Corporation
    "TXN",   # Texas Instruments Incorporated
    "MU",    # Micron Technology, Inc.
    "ASML",  # ASML Holding N.V.
    "LRCX",  # Lam Research Corporation
    "AMAT",  # Applied Materials, Inc.
    "KLAC",  # KLA Corporation
    
    # Software - Infrastructure & Enterprise
    "ORCL",  # Oracle Corporation
    "ADBE",  # Adobe Inc.
    "CRM",   # Salesforce, Inc.
    "SAP",   # SAP SE
    "NOW",   # ServiceNow, Inc.
    "INTU",  # Intuit Inc.
    "VMW",   # VMware, Inc. (Part of Broadcom)
    "SNOW",  # Snowflake Inc.
    "PANW",  # Palo Alto Networks, Inc.
    "CRWD",  # CrowdStrike Holdings, Inc.
    "ZS",    # Zscaler, Inc.
    "DDOG",  # Datadog, Inc.
    "MDB",   # MongoDB, Inc.
    "PLTR",  # Palantir Technologies Inc.
    "U",     # Unity Software Inc.
    
    # Software - Consumer & Internet
    "NFLX",  # Netflix, Inc.
    "UBER",  # Uber Technologies, Inc.
    "ABNB",  # Airbnb, Inc.
    "SPOT",  # Spotify Technology S.A.
    "PINS",  # Pinterest, Inc.
    "SNAP",  # Snap Inc.
    "DASH",  # DoorDash, Inc.
    "SHOP",  # Shopify Inc.
    "SQ",    # Block, Inc.
    
    # Hardware & Equipment
    "CSCO",  # Cisco Systems, Inc.
    "IBM",   # International Business Machines Corporation
    "DELL",  # Dell Technologies Inc.
    "HPQ",   # HP Inc.
    "ARW",   # Arrow Electronics, Inc.
    "ANET",  # Arista Networks, Inc.
    
    # IT Services & Consulting
    "ACN",   # Accenture plc
    "CTSH",  # Cognizant Technology Solutions Corporation
    "INFY",  # Infosys Limited
    
    # Other Notable Tech
    "BABA",  # Alibaba Group Holding Limited
    "TCEHY", # Tencent Holdings Ltd.
    "SONY",  # Sony Group Corporation
]

ticker_list = ['AAPL','MSFT','AMZN']

save_folder = 'smallNoTech'
save_location = os.path.join('backtestingData',save_folder)

if not os.path.exists(save_location):
    os.mkdir(save_location)

for tic_string in ticker_list:
    ticker = yf.Ticker(tic_string)
    data = ticker.history(period='1500d',interval='1d')
    data['Ticker'] = tic_string

    data['Indicator'] = np.random.choice([-1,0,1],size = len(data))
    data['OrderVal'] = np.random.uniform(low=10,high=200,size=len(data))

    data.to_csv(f'{save_location}/{tic_string}.csv')