# Data sources

import yfinance as yf
import pandas as pd
from fomc_get_data.FomcMinutes import FomcMinutes

# Get history of interest rate (10 Years Treasury Yield)
TNX = yf.Ticker('^TNX')
#TNX_hist = TNX.history(period='max')

# Get history of S&P 500
SP500 = yf.Ticker('SPY')
#SP500_hist = SP500.history(period='max')

# Get FED minutes
# TODO: Check if files already exist and if they are already up-to-date; if not get the data
# TODO: FIX years 2017 until 2022
fomc = FomcMinutes()
df_minutes = fomc.get_contents()

