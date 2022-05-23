import os
import enchant
import csv

words = set()
d = enchant.Dict("en_us")

itr = 0
print("0/26")

for filename in os.scandir(os.getcwd()):

    itr+=1

    if filename.is_file() and os.fsdecode(filename).endswith(".csv"):
        f = filename.path
    else:
        continue

    file = open(f)
    csvreader = csv.reader(file)

    print(str(itr) + "/26")

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
                words.add(wrd)
                currentWord = wrd
            continue
        if wrd.isupper:
            if wrd.lower() != currentWord:
                if not d.check(wrd.lower()):
                    continue
                words.add(wrd.lower())
                currentWord = wrd.lower()
            continue
        if wrd != currentWord:
            if not d.check(wrd):
                continue
            words.add(wrd)
            currentWord = wrd

    file.close()

word_list = list(words)

word_list = sorted(word_list)

textfile = open("word.txt", "w")
for element in word_list:
    textfile.write(element + "\n")
textfile.close()

print("Done")