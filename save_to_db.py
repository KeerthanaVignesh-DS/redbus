import pandas as pd
from sqlalchemy import create_engine

# MySQL database configuration
db_username = 'root'         # Replace with your MySQL username
db_password = ''     # Replace with your MySQL password
db_host = 'localhost'        # Hostname of the MySQL server
db_port = '3306'             # Default MySQL port
db_name = 'redbus'           # Name of the database

# Create SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Read scraped data
df = pd.read_csv("rtc_details.csv")

# Create table and insert data
df.to_sql('bus_routes', engine, if_exists='replace', index=False)

print("Data stored in database successfully.")
