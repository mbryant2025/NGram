import requests
import pandas as pd
import scipy.stats as stats
import numpy as np
import csv
import enchant
import os

class PQ:

    queue = []
    mxsze = 0

    def __init__(self, maxsize):
        self.mxsze = maxsize

    def put(self, item):
        self.queue.append(item)
        self.queue = sorted(self.queue, key=lambda val: val[0])
        if len(self.queue) > self.mxsze:
            self.queue = self.queue[:self.mxsze]

    def qsize(self):
        return len(self.queue)

    def get(self):
        return self.queue.pop()

d = enchant.Dict("en_us")

itr = 0

for filename in os.scandir(os.getcwd()):
    if filename.is_file() and os.fsdecode(filename).endswith(".csv"):
        f = filename.path
    else:
        continue

    file = open(f)
    csvreader = csv.reader(file)

    print("Gathering words...")

    words = []
    first = True
    currentWord = ""
    for row in csvreader:
        if first:
            first = False
            continue
        wrd = row[0]
        if "_" in wrd:
            if wrd != currentWord:
                if not d.check(wrd):
                    continue
                words.append(wrd)
                currentWord = wrd
            continue
        if wrd.isupper:
            if wrd.lower() != currentWord:
                if not d.check(wrd.lower()):
                    continue
                words.append(wrd.lower())
                currentWord = wrd.lower()
            continue
        if wrd != currentWord:
            if not d.check(wrd):
                continue
            words.append(wrd)
            currentWord = wrd

    file.close()

    print("Words: " + str(len(words)))

    chunk_size = 1
    q = PQ(maxsize = 10)

    def printQueue():
        for i in range(q.qsize()):
            print(q.queue[i][0], q.queue[i][1])

    def chunker(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    for group in chunker(words, chunk_size):

        input_words = ",".join(group)

        params = {
            "content": input_words,
            "year_start": "1800",
            "year_end": "2019"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36",
        }
        html = requests.get("https://books.google.com/ngrams/json", params=params, headers=headers, timeout=30).text
        try:
            time_series = pd.read_json(html, typ="series")
            year_values = list(range(int(params['year_start']), int(params['year_end']) + 1))
        except:
            continue

        for series in time_series:
            arr = np.array(series["timeseries"])
            peak = max(stats.zscore(arr))

            #Offset data that has peak at ends of data range
            loc = np.argmax(arr)
            if(loc < 3 or loc > len(arr) - 4):
                peak -= 100

            q.put((-peak, series["ngram"]))
            if itr % 10 == 0:
                print()
                print("Iteration " + str(itr) + ":\n===============================================")
                printQueue()
                print()
                print("Current word: " + str(series["ngram"]))
            
            itr += 1

        # time.sleep(1)

print()
print("Done\n===============================================")
printQueue()

while q.qsize() > 0:
    p = q.get()