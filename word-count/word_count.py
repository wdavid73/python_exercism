import re
from collections import Counter

def count_words(sentence):
    res = sentence.replace("\n", "").lower()
    return Counter(re.findall(r"[a-z0-9]+(?:'[a-z]+)?", res))
