import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_nyc_311(days=1):
    url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json"
    since = (datetime.utcnow() - timedelta(days=days)).isoformat()
    params = {"$where": f"created_date >= '{since}'", "$limit": 50000}
    resp = requests.get(url, params=params)
    df = pd.DataFrame(resp.json())
    return df
