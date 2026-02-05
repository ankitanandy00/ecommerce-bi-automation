import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://etluser:1234@127.0.0.1/ecommerce"
)

print("Connected")


# =====================================
# EXTRACT SEPARATELY
# =====================================
raw_df = pd.read_sql("SELECT * FROM raw_orders", engine)
live_df = pd.read_sql("SELECT * FROM live_orders", engine)

print("Raw rows :", len(raw_df))
print("Live rows:", len(live_df))


# =====================================
# FIX ONLY RAW TABLE COLUMN NAMES
# =====================================
raw_df.columns = [
    "Order_Date",
    "Product_Name",
    "Category",
    "Region",
    "Quantity",
    "Sales",
    "Profit"
]

# live table already correct


# =====================================
# NOW COMBINE (schemas match perfectly)
# =====================================
df = pd.concat([raw_df, live_df], ignore_index=True)

print("\nInitial rows:", len(df))
print("Columns:", list(df.columns))


# =====================================
# CLEANING
# =====================================

df = df.dropna()
print("After dropna:", len(df))

df = df.drop_duplicates()
print("After duplicates:", len(df))

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Quantity"] = pd.to_numeric(df["Quantity"])
df["Sales"] = pd.to_numeric(df["Sales"])
df["Profit"] = pd.to_numeric(df["Profit"])

df = df[df["Quantity"] > 0]
print("After quantity:", len(df))

df = df[df["Sales"] > 0]
print("After sales:", len(df))


# =====================================
# LOAD
# =====================================
df.to_sql("clean_orders", engine, if_exists="replace", index=False)

print("\n🎉 Final clean rows:", len(df))
