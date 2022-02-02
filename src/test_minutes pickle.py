import pandas as pd
import pickle


with open(r"C:\Users\philippz\PycharmProjects\TextMiningFinalProject\data\FOMC\minutes.pickle" , 'rb') as f:
    df=pickle.load(f)

print(df.i['contents'])
