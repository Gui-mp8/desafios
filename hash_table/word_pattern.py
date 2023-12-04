def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()

    if len(pattern)!= len(words):
        return False

    for i in range(len(words)):
        if pattern.find(pattern[i]) != words.index(words[i]):
            print(pattern[i], words[i])
            return False

    return True

pattern = "abbac"
s = "dog cat cat dog cat"
print(word_pattern(pattern, s))