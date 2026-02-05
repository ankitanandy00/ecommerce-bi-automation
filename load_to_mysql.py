import pandas as pd
from sqlalchemy import create_engine

# 1. read csv
df = pd.read_csv("ecommerce_sales_data (2).csv")   # change filename

print("CSV loaded")

# 2. connect to MySQL
engine = create_engine( "mysql+pymysql://etluser:1234@127.0.0.1/ecommerce")

print("Connected to MySQL")

# 3. load into table
df.to_sql("raw_orders", engine, if_exists="replace", index=False)

print("Data loaded successfully!")
