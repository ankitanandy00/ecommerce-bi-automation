# 🛒 Real-Time E-Commerce BI System with Automated ETL

An end-to-end Business Intelligence system that simulates real-time e-commerce transactions, processes data through an automated ETL pipeline, and visualizes business insights using Power BI.
This project demonstrates how historical and streaming data can be combined to build a near real-time analytics workflow similar to industry BI systems.

# 🚀 Project Overview

This project collects historical e-commerce data using the Kaggle API and combines it with simulated live order data generated through Python scripts. An automated ETL pipeline cleans and transforms the data before loading it into an analytics-ready table in MySQL. Power BI dashboards are then used to monitor sales performance, profit trends, and business KPIs.

# ⚙️ Architecture
Kaggle Dataset
      ↓
   MySQL (raw_orders)
      ↓
Python Live Order Generator
      ↓
   MySQL (live_orders)
      ↓
Python ETL Cleaning Pipeline
      ↓
   MySQL (clean_orders)
      ↓
Power BI Dashboard

# 🧰 Tech Stack

- Python (Pandas, SQLAlchemy)
- MySQL
- Power BI
- Kaggle API
- SQL
- Windows Task Scheduler

# 📊 Features

- Historical data ingestion using Kaggle API
- Real-time order simulation using Python
- Automated ETL pipeline for data cleaning and transformation
- Scheduled workflows using Windows Task Scheduler
- Interactive Power BI dashboards
- Sales, Profit, and KPI monitoring
- Regional and category-based analysis

# 🔄 Automation

- Automation is implemented using Windows Task Scheduler:
- Live order generator runs periodically to simulate streaming data
- ETL pipeline runs at scheduled intervals to update cleaned analytics tables
- Power BI dashboards refresh to reflect updated data

# 📈 Dashboard Insights

- The Power BI dashboard provides:

1. Sales trend analysis

2. Profit analysis

3. Regional performance comparison

4. Category-wise performance

5. Key business KPIs

# 📂 Project Structure
├── data/
├── generate_live_orders.py
├── python_cleaning.py
├── load_to_mysql.py
├── dashboard/
└── README.md

# 🧠 Learning Outcomes

- Built an automated ETL pipeline using Python and SQL
- Worked with batch and simulated streaming data
- Designed analytics-ready database tables
- Developed business intelligence dashboards
- Implemented task scheduling for automation

# 📌 Future Improvements

- Deploy ETL pipeline using Airflow
- Real-time streaming using Kafka
- Cloud deployment (AWS / Azure)
- Automatic Power BI refresh using Power BI Service
