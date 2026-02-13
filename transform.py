import pandas as pd
from datetime import datetime

def transform_data(raw_data):

    records = []

    for crypto, price_info in raw_data.items():
        record = {
            "crypto": crypto,
            "price_usd": price_info["usd"],
            "timestamp": datetime.now()
        }
        records.append(record)

    df = pd.DataFrame(records)

    return df
