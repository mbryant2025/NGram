import requests
import pandas as pd

word = "Obama"

params = {
            "content": word,
            "year_start": "1800",
            "year_end": "2019"
             }

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
}


html = requests.get("https://books.google.com/ngrams/json", params=params, headers=headers, timeout=30).text

time_series = pd.read_json(html, typ="series")

print("Data for " + word + ":\n")

print(time_series[0]["timeseries"])
