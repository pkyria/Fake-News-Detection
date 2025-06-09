import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import joblib

df_news = pd.read_csv('ML/WELFake_Dataset.csv')

print(df_news.head(20))