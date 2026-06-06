import pandas as pd

url = "https://www.kaggle.com/datasets/shibumohapatra/house-price?select=1553768847-housing.csv"
df = pd.read_csv (url)

df.to_csv ("C:/Users/ogbid/OneDrive/House_ICA/data/house_predict.csv")

class DataLoader:
    def __init__ (self, url, file_type = 'csv'):
        self.source = url
        self.file_type = file_type.lower()
        self.data = None

    def load_data (self):
        if self.file_type == "csv":
            self.data = pd.read_csv(self.url)
        elif self.file_type == "excel":
            self.data = pd.read_excel(self.url)
        elif self.file_type == "json":
            self.data = pd.read_json(self.url)

        else:
            raise ValueError(f"unsuported file type{self.file_type}")
        print("Data loades successfully")
        return self.data

    def preview (self, n = 5):
        if self.data is None:
            raise ValueError("There is no dataset loades here")
        return self.data.head(n)
        