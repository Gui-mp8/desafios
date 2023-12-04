def length_of_last_word(s: str) -> int:
    return len(s.split()[-1])

s = "   fly me   to   the moon  hello danny "
print(length_of_last_word(s))