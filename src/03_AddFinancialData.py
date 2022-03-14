import pandas as pd
import os

script_dir = os.path.dirname(__file__)
rel_path_CLEANED = "../data/cleaned_data"
rel_path_COMPLETE = "../data/complete_data"
rel_path = "../data"
files = os.listdir(os.path.join(script_dir, rel_path_CLEANED))

SP500 = pd.read_csv(os.path.join(script_dir, rel_path + '/SPY.csv'), parse_dates=['Date'])
SP500 = SP500[['Date', 'Close']]
TNX = pd.read_csv(os.path.join(script_dir, rel_path + '/^TNX.csv'), parse_dates=['Date'])
TNX = TNX[['Date', 'Close']]

if not os.path.exists(os.path.join(script_dir, rel_path_COMPLETE)):
    os.makedirs(os.path.join(script_dir, rel_path_COMPLETE))


def add_sp500_data(df, sp500_hist):
    ret = df.copy()
    for i in range(1, -15, -1):  # iterate from previous day until 2 weeks after the announcement
        tmp = sp500_hist.copy()
        tmp['Close'] = tmp['Close'].shift(periods=i)
        column_name = 'SPY: d' + str(-i) if i > 0 else 'SPY: d+' + str(-i)
        ret[column_name] = pd.merge(left=ret, right=tmp, left_on='date', right_on='Date', how='left')[
            'Close']
    return ret


def add_interest_rate(df, tnx_hist):
    ret = df.copy()
    for i in [1, 0]:  # add interest date on the day of the announcement and on the previous day
        tmp = tnx_hist.copy()
        tmp['Close'] = tmp['Close'].shift(periods=i)
        column_name = '^TNX: d' + str(-i) if i > 0 else '^TNX: d+' + str(-i)
        ret[column_name] = pd.merge(left=ret, right=tmp, left_on='date', right_on='Date', how='left')['Close']
    return ret


for file in files:
    input_df = pd.read_csv(os.path.join(script_dir, rel_path_CLEANED + '/' + file), parse_dates=['date'])
    input_df = add_sp500_data(input_df, SP500)
    input_df = add_interest_rate(input_df, TNX)
    file_name = file.split(".")[0] + '_spy_tnx.csv'
    input_df.to_csv(os.path.join(script_dir, rel_path_COMPLETE + '/' + file_name), index=False)