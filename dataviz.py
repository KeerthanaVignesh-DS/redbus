import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# MySQL database configuration
db_username = 'root'         # Replace with your MySQL username
db_password = ''             # Replace with your MySQL password
db_host = 'localhost'        # Hostname of the MySQL server
db_port = '3306'             # Default MySQL port
db_name = 'redbus'           # Name of the database

# Create SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

# Query to get data
query = "SELECT * FROM bus_routes"
df = pd.read_sql(query, engine)

st.title("Redbus Data Analysis")

# Filters
st.sidebar.header("Filters")

route_name = st.sidebar.multiselect("Select Bus Type", options=df['route_name'].unique(), default=df['route_name'].unique())
price_range = st.sidebar.slider("Select Price Range", float(df['price'].min()), float(df['price'].max()), (float(df['price'].min()), float(df['price'].max())))
star_rating = st.sidebar.slider("Select Minimum Star Rating", 0.0, 5.0, 0.0)
seats_available = st.sidebar.slider("Select Minimum Seats Available", 0, int(df['seats_available'].max()), 0)

# Apply filters
if route_name:
    df = df[df['route_name'].isin(route_name)]
df = df[(df['price'] >= price_range[0]) & (df['price'] <= price_range[1])]
df = df[df['star_rating'] >= star_rating]
df = df[df['seats_available'] >= seats_available]

# Display data
st.write("### Filtered Bus Routes")
st.dataframe(df)

# Display data statistics
st.write("### Data Statistics")
st.write(df.describe())

# Save the filtered data to a CSV file
csv = df.to_csv(index=False)
st.download_button(
    label="Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_redbus_data.csv',
    mime='text/csv',
)

st.write("Filtered data saved to `filtered_redbus_data.csv`.")
