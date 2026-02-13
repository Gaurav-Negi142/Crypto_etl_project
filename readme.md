# Crypto ETL Pipeline

## Project Overview

This project is a **simple end-to-end ETL (Extract, Transform, Load) pipeline** built using Python.
It fetches live cryptocurrency prices from a public API, transforms the data, and stores it in a local SQLite database.

The project demonstrates core **data engineering concepts** such as:

* API data extraction
* Data transformation
* Database loading
* Logging
* Modular project structure

---

## Project Structure

```
crypto_etl_project/
│
├── src/
│   ├── extract.py      # Fetches crypto data from API
│   ├── transform.py    # Cleans and structures the data
│   ├── load.py         # Saves data to SQLite database
│   └── main.py         # Runs the ETL pipeline
│
├── data/
│   └── crypto.db       # SQLite database (auto-generated)
│
├── logs/
│   └── pipeline.log    # Execution logs
│
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── .gitignore          # Ignored files
```

---

## Technologies Used

* Python
* Requests (API calls)
* Pandas (data transformation)
* SQLite (database)
* Logging module

---

## How the Pipeline Works

### Step 1: Extract

* Fetches cryptocurrency prices (Bitcoin and Ethereum) from a public API.

### Step 2: Transform

* Converts raw JSON data into a structured Pandas DataFrame.
* Adds a timestamp column.

### Step 3: Load

* Saves the transformed data into a SQLite database.

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/crypto_etl_project.git
cd crypto_etl_project
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run the Pipeline

From the project root:

```bash
python src/main.py
```

You should see:

* Data extracted from the API
* Transformed data preview
* Data saved to the SQLite database
* Logs created in the `logs/` folder

---

## Example Output

```
Starting pipeline...
Raw data: {'bitcoin': {'usd': 68933}, 'ethereum': {'usd': 2040.27}}

Transformed Data:
     crypto  price_usd                  timestamp
0   bitcoin   68933.00 2026-02-13 21:04:12
1  ethereum    2040.27 2026-02-13 21:04:12

Data saved to database at data/crypto.db
Pipeline finished.
```

---

## Key Learning Outcomes

* Building a modular Python project
* Working with APIs
* Data transformation using Pandas
* Loading data into SQLite
* Implementing logging
* Using Git and GitHub for version control

---

## Future Improvements

* Add more cryptocurrencies
* Schedule pipeline using cron or Airflow
* Store data in a cloud database
* Add automated tests
* Build a dashboard for visualization

---

## Author

**Gaurav Singh Negi**
Data Science aspirate
India
