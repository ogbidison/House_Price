import pandas as pd

url = "https://www.kaggle.com/datasets/shibumohapatra/house-price?select=1553768847-housing.csv"
df = pd.read_csv (url)

df.to_csv ("C:/Users/ogbid/OneDrive/House_ICA/data/house_predict.csv")