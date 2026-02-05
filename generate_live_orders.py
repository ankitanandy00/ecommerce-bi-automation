import random
import time
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://etluser:1234@127.0.0.1/ecommerce"
)

print("Starting live orders generator...")

products = ["Printer", "Mouse", "Tablet", "Laptop", "Keyboard"]
categories = ["Office", "Accessories", "Electronics"]
regions = ["North", "South", "East", "West"]

while True:

    new_order = {
        "Order_Date": datetime.now().date(),
        "Product_Name": random.choice(products),
        "Category": random.choice(categories),
        "Region": random.choice(regions),
        "Quantity": random.randint(1, 10),
        "Sales": round(random.uniform(500, 5000), 2),
        "Profit": round(random.uniform(50, 800), 2)
    }

    df = pd.DataFrame([new_order])

    df.to_sql("live_orders", engine, if_exists="append", index=False)

    print("Inserted:", new_order)

    time.sleep(5)
