from extract import extract_data
from transform import transform_data
from load import load_data
from logger import get_logger

logger = get_logger()

logger.info("Pipeline started")

try:
    raw_data = extract_data()
    logger.info("Data extracted successfully")

    df = transform_data(raw_data)
    logger.info("Data transformed successfully")

    load_data(df)
    logger.info("Data loaded into database")

    logger.info("Pipeline finished successfully")

except Exception as e:
    logger.error(f"Pipeline failed: {e}")
    print("Pipeline failed. Check logs.")
