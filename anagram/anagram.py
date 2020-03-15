def find_anagrams(word, candidates):
    anagram = []
    for candidate in candidates:
        if word.lower() == candidate.lower():
            pass
        else:
            if sorted(word.lower()) == sorted(candidate.lower()):
                anagram.append(candidate)
    return anagram