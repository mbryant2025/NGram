#Importing the package
from google_ngram_api.Downloader import Downloader

#Creating the object
downloader = Downloader()

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for letter in letters:
    print(letter)
    downloader.download_full_csv('eng','1',letter)
