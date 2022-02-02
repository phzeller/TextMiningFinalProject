import pandas as pd
import pickle


with open(r"C:\Users\chriq\PycharmProjects\Text_Mining\data\FOMC\minutes.pickle" , 'rb') as f:
    df=pickle.load(f)


df.head()