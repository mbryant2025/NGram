
count = 0

with open('words.txt', 'r') as f:

    for line in f:
        count +=1

        if count % 10000 == 0: 
            print("Current count: " + str(count))

print("Total words: " + str(count))
print("Done")