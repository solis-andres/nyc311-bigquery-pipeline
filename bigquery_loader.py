from google.cloud import bigquery

def upload_to_bigquery(df, project_id, dataset, table):
    client = bigquery.Client(project=project_id)
    dest = f"{project_id}.{dataset}.{table}"
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    job = client.load_table_from_dataframe(df, dest, job_config=job_config)
    job.result()
    print(f"Loaded {len(df)} rows to {dest}")
