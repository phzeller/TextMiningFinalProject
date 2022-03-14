import yfinance as yf
import os
from fomc_get_data.FomcMinutes import FomcMinutes
from fomc_get_data.FomcStatement import FomcStatement
from fomc_get_data.FomcTestimony import FomcTestimony
from fomc_get_data.FomcSpeech import FomcSpeech

script_dir = os.path.dirname(__file__)
rel_path = "../data"
rel_path_FOMC = "../data/FOMC"
if not os.path.exists(os.path.join(script_dir, rel_path_FOMC)):
    os.makedirs(os.path.join(script_dir, rel_path_FOMC))

# Get history of interest rate (10 Years Treasury Yield) and history of S&P500 prices
tickers = ['^TNX', 'SPY']
for symbol in tickers:
    ticker = yf.Ticker(symbol)
    ticker_hist = ticker.history(period='max')
    ticker_hist.to_csv(os.path.join(script_dir, rel_path + '/' + symbol + '.csv'))

# Get FED minutes
fomc_minutes = FomcMinutes()
df_minutes = fomc_minutes.get_contents()
df_minutes = df_minutes.fillna('')
df_minutes.to_csv(os.path.join(script_dir, rel_path_FOMC + '/minutes.csv'), index=False)

# Get FED statements
fomc_statements = FomcStatement()
df_statements = fomc_statements.get_contents()
df_statements = df_statements.fillna('')
df_statements.to_csv(os.path.join(script_dir, rel_path_FOMC + '/statements.csv'), index=False)

# Get FED testimonies
fomc_testimonies = FomcTestimony()
df_testimonies = fomc_testimonies.get_contents()
df_testimonies = df_testimonies.fillna('')
df_testimonies.to_csv(os.path.join(script_dir, rel_path_FOMC + '/testimonies.csv'), index=False)

# Get FED speeches
fomc_speeches = FomcSpeech()
df_speeches = fomc_speeches.get_contents()
df_speeches = df_speeches.fillna('')
df_speeches.to_csv(os.path.join(script_dir, rel_path_FOMC + '/speeches.csv'), index=False)


