# ============================================================
# ETL PROJECT: Countries by GDP
# ============================================================
# This script:
# 1. Extracts GDP data from the web
# 2. Transforms IMF GDP data from million to billion USD
# 3. Saves the data as a JSON file
# 4. Loads the data into a SQLite database
# 5. Runs a SQL query for countries with GDP > 100 billion
# 6. Logs the complete ETL process
# ============================================================


# ============================================================
# STEP 1: IMPORT REQUIRED LIBRARIES
# ============================================================

import pandas as pd
import sqlite3
import requests
from bs4 import BeautifulSoup
import json
import logging
from io import StringIO


# ============================================================
# STEP 2: CONFIGURE LOGGING
# ============================================================
# All important steps of the ETL process will be recorded
# in the file: etl_project_log.txt

logging.basicConfig(
    filename='etl_project_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("ETL process started.")


# ============================================================
# STEP 3: EXTRACT - ACCESS THE WEBPAGE
# ============================================================
# URL containing the GDP information.

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"

# Download the webpage.
# verify=False is used because of the SSL certificate issue
# encountered with the Web Archive URL.

response = requests.get(url, verify=False)

logging.info("Webpage successfully accessed.")


# ============================================================
# STEP 4: EXTRACT - READ HTML TABLES
# ============================================================
# Convert the webpage HTML into pandas DataFrames.

tables = pd.read_html(StringIO(response.text))

print("Number of tables extracted:", len(tables))

logging.info(
    "Data extraction completed. %s tables extracted.",
    len(tables)
)


# Display all extracted tables
for i, table in enumerate(tables):
    print("\nTable", i)
    print(table.head())


# ============================================================
# STEP 5: SELECT THE REQUIRED GDP TABLE
# ============================================================
# Table 2 contains the country GDP information.

df = tables[2]

logging.info("Required GDP table selected.")


# ============================================================
# STEP 6: SELECT COUNTRY AND IMF GDP DATA
# ============================================================
# Select:
# - Country/Territory
# - IMF GDP Estimate

GDP_USD_million = df[
    ('IMF[1][13]', 'Estimate')
]

Country = df[
    ('Country/Territory', 'Country/Territory')
]


# ============================================================
# STEP 7: TRANSFORM - CONVERT GDP TO NUMERIC
# ============================================================
# Some GDP values may contain non-numeric values such as "—".
# errors='coerce' converts invalid values into NaN.

GDP_USD_million = pd.to_numeric(
    GDP_USD_million,
    errors='coerce'
)


# ============================================================
# STEP 8: TRANSFORM - CONVERT MILLION USD TO BILLION USD
# ============================================================
# 1 billion = 1000 million

GDP_USD_billion = GDP_USD_million / 1000


# ============================================================
# STEP 9: TRANSFORM - ROUND GDP TO 2 DECIMAL PLACES
# ============================================================

GDP_USD_billion = round(
    GDP_USD_billion,
    2
)


# ============================================================
# STEP 10: CREATE FINAL DATAFRAME
# ============================================================
# The project requires only:
# - Country
# - GDP_USD_billion

final_df = pd.DataFrame({
    'Country': Country,
    'GDP_USD_billion': GDP_USD_billion
})


# ============================================================
# STEP 11: REMOVE "WORLD" ROW
# ============================================================
# The project asks for countries, so "World" is not required.

final_df = final_df[
    final_df['Country'] != 'World'
]


# ============================================================
# STEP 12: SORT COUNTRIES BY GDP
# ============================================================
# Sort from highest GDP to lowest GDP.

final_df = final_df.sort_values(
    by='GDP_USD_billion',
    ascending=False
)


# Reset the DataFrame index after sorting.

final_df = final_df.reset_index(
    drop=True
)


print("\nTop 10 countries by GDP:")
print(final_df.head(10))

logging.info("Data transformation completed.")


# ============================================================
# STEP 13: LOAD - SAVE DATA AS JSON
# ============================================================
# Save the transformed data to:
# Countries_by_GDP.json

final_df.to_json(
    'Countries_by_GDP.json',
    orient='records',
    indent=4
)

print("\nJSON file created successfully.")

logging.info(
    "JSON file 'Countries_by_GDP.json' created successfully."
)


# ============================================================
# STEP 14: LOAD - CREATE SQLITE DATABASE
# ============================================================
# Create/connect to the database:
# World_Economies.db

conn = sqlite3.connect(
    'World_Economies.db'
)


# ============================================================
# STEP 15: LOAD - CREATE DATABASE TABLE
# ============================================================
# Create the table:
# Countries_by_GDP

final_df.to_sql(
    'Countries_by_GDP',
    conn,
    if_exists='replace',
    index=False
)

print("Database table created successfully.")

logging.info(
    "Database table 'Countries_by_GDP' created successfully."
)


# ============================================================
# STEP 16: VERIFY DATABASE
# ============================================================
# Display the first 10 records from the database.

query = """
SELECT *
FROM Countries_by_GDP
LIMIT 10
"""

result = pd.read_sql_query(
    query,
    conn
)

print("\nFirst 10 records from database:")
print(result)

logging.info(
    "Database verification query executed successfully."
)


# ============================================================
# STEP 17: BOSS'S REQUIRED SQL QUERY
# ============================================================
# Display only countries whose GDP is greater than
# 100 billion USD.

query = """
SELECT *
FROM Countries_by_GDP
WHERE GDP_USD_billion > 100
ORDER BY GDP_USD_billion DESC
"""

result = pd.read_sql_query(
    query,
    conn
)

print("\nCountries with GDP greater than 100 billion USD:")
print(result)

logging.info(
    "GDP > 100 billion USD query executed successfully."
)


# ============================================================
# STEP 18: CLOSE DATABASE CONNECTION
# ============================================================

conn.close()

logging.info(
    "Database connection closed."
)

logging.info(
    "ETL process completed successfully."
)

print("\nETL process completed successfully.")
