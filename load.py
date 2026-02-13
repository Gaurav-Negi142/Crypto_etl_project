import sqlite3
import os

def load_data(df):
    os.makedirs("DATA", exist_ok=True)

    db_path = "DATA/crypto.db"

    conn = sqlite3.connect(db_path)
    df.to_sql("crypto_prices", conn, if_exists="append", index=False)
    conn.close()

    print(f"Data saved to database at {db_path}")
