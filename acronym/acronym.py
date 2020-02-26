def abbreviate(sentence, result=""):
    words = sentence.replace(",", "").replace("_", "").replace("-", " ").split()
    for word in words:
        if word[0].isupper() or word[0].islower():
            result += word[0]
    return result.upper()
