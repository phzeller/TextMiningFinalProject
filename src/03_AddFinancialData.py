import pandas as pd

minutes = pd.read_csv('../data/minutes.csv', parse_dates=['date'])
SP500 = pd.read_csv('../data/SPY.csv', parse_dates=['Date'])
SP500 = SP500[['Date', 'Close']]
TNX = pd.read_csv('../data/^TNX.csv', parse_dates=['Date'])
TNX = TNX[['Date', 'Close']]


def add_SP500_data(df, SP500_hist):
    ret = df.copy()
    for i in range(1, -15, -1):  # iterate from previous day until 2 weeks after the announcement
        tmp = SP500_hist.copy()
        tmp['Close'] = tmp['Close'].shift(periods=i)
        column_name = 'SPY: d' + str(-i) if i > 0 else 'SPY: d+' + str(-i)
        ret[column_name] = pd.merge(left=minutes, right=tmp, left_on='date', right_on='Date', how='left')[
            'Close']
    return ret


def add_interest_rate(df, TNX_hist):
    ret = df.copy()
    for i in [1, 0]:  # add interest date on the day of the announcement and on the previous day
        tmp = TNX_hist.copy()
        tmp['Close'] = tmp['Close'].shift(periods=i)
        column_name = '^TNX: d' + str(-i) if i > 0 else '^TNX: d+' + str(-i)
        ret[column_name] = pd.merge(left=minutes, right=tmp, left_on='date', right_on='Date', how='left')['Close']
    return ret


df = add_SP500_data(minutes, SP500)
df = add_interest_rate(df, TNX)

df.to_csv('../data/CompleteTable.csv', index=False)