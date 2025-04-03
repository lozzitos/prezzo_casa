
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from joblib import dump
df = pd.read_excel(r"C:\Users\acer\Downloads\real\dataset.xlsx")
df["price_per_m2"] = df["Y house price of unit area"] / 3.3 * 10000
X = df[["X5 latitude", "X6 longitude"]]
y = df["price_per_m2"]
df.info()
df.describe()
model = LinearRegression()
model.fit(X, y)
#print(model.intercept_)
dump(model, 'model.joblib')
