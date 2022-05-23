import requests
import pandas as pd

with open('timeseries.txt', 'w') as f_out:
    with open('words.txt', 'r') as f_in:

        itr = 0
        wds = []

        for line in f_in:

            word = line[:-1]

            if itr % 50 == 0:
                print("Completed: " + str(itr) + "\t" + "Current word: " + word)

            itr += 1

            if len(wds) < 10:
                wds.append(word)
                continue

            str_words = ",".join(wds)

            params = {
            "content": str_words,
            "year_start": "1800",
            "year_end": "2019"
             }

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
            }

            try:
                html = requests.get("https://books.google.com/ngrams/json", params=params, headers=headers, timeout=30).text

                time_series = pd.read_json(html, typ="series")
            except:
                continue

            for ts in time_series:
                write_string = ts["ngram"] + " " + str(ts["timeseries"]) + "\n"
                f_out.write(write_string)

            wds.clear()