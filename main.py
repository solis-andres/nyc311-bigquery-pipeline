from nyc_311_fetcher import fetch_nyc_311
from bigquery_loader import upload_to_bigquery

PROJECT = "nyc-311-pipeline"
DATASET = "nyc311"
TABLE = "complaints"

df = fetch_nyc_311(days=1)
if not df.empty:
    upload_to_bigquery(df, PROJECT, DATASET, TABLE)
else:
    print("No new records to load.")
