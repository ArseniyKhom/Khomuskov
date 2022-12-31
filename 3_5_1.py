import pandas as pd
import sqlite3

df = pd.read_csv("3.3.1.csv")

connection = sqlite3.connect("3_5_1.db")
cursor = connection.cursor()
df.to_sql(name="currency_from_api", con=connection, if_exists='replace', index=False)
connection.commit()