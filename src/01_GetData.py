# Data sources

import yfinance as yf
import os
import pandas as pd
from fomc_get_data.FomcMinutes import FomcMinutes

# Get history of interest rate (10 Years Treasury Yield)
TNX = yf.Ticker('^TNX')
TNX_hist = TNX.history(period='max')
TNX_hist.to_csv('../data/^TNX.csv')

# Get history of S&P 500
SP500 = yf.Ticker('SPY')
SP500_hist = SP500.history(period='max')
SP500_hist.to_csv('../data/SPY.csv')

# Get FED minutes
# TODO: Check if files already exist and if they are already up-to-date; if not get the data
fomc = FomcMinutes()
df_minutes = fomc.get_contents()

if not os.path.exists('../data/FOMC'):
    os.makedirs('../data/FOMC')
df_minutes.to_csv('../data/FOMC/minutes.csv', index=False)


