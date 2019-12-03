from common import links_wl
from urllib.request import urlopen


def count_words(text):
    wordcount = {}
    for word in text.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1


def main():
    for link in links_wl:
        data = urlopen(link).read()
        count_words(data)
