import re
from collections import Counter

def word_frequency(text):
    """Takes a string, strips it of all whitespace, punctuation and special chars,
    and returns a dictionary with words as the key, and the number of times they
    appear as the value. Uses Counter from collections"""
    stripped_text = re.sub('[^a-zA-Z\ \'\n]+', '', text).lower().split()
    common_words = Counter(stripped_text)
    return common_words

if __name__ == '__main__':
    with open("sample.txt") as sample:
        text = sample.read()
        common_words = word_frequency(text)

    #uses Counter.most_common method to find the 20 most commons words
    most_common = common_words.most_common(20)

    for count, word in most_common:
        print(word, count)
