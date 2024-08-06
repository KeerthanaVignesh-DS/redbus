# RedBus Web Scraping and Data Analysis

This repository contains scripts for scraping bus route and booking information from the RedBus website, storing the data in a MySQL database, and providing a Streamlit-based web application for data analysis.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Scraping Data](#scraping-data)
  - [Storing Data in MySQL](#storing-data-in-mysql)
  - [Running the Streamlit App](#running-the-streamlit-app)
- [Scripts](#scripts)
  - [scrap_data2.py](#scraperpy)
  - [save_to_db.py](#setuppy)
  - [dataviz.py](#apppy)
- [Notes](#notes)
- [Disclaimer](#disclaimer)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/KeerthanaVignesh-DS/redbus.git
   cd redbus
2. Create virtualenvironment(venv)

.Install the required Python packages:
    pip install selenium pandas sqlalchemy streamlit pymysql

3.Download and install the appropriate WebDriver for your browser:
4.Set up your MySQL database(redbus) and update the database create a table using table.sql

# usage

## Scraping Data
Run the scrap_data2.py script to scrape data from the RedBus website and save it to a CSV file:
    python scrap_data2.py

## Storing Data in MySQL
Run the save_to_db.py script to read the scraped data from the CSV file and store it in a MySQL database:
    python save_to_db.py

## Running the Streamlit App
Run the dataviz.py script to start the Streamlit web application for data analysis:
    streamlit run app.py
