def roman_to_int(s: str) -> int:
    symbols = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    sum = 0

    for i in range(len(s)):
        if i < len(s) - 1 and symbols[s[i]] < symbols[s[i+1]]:
            sum -= symbols[s[i]]
        else:
            sum += symbols[s[i]]

    return sum

def super_roman_to_int(s: str) -> int:
    translations = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum = 0
    s = s.replace("IV", "IIII").replace("IX", "VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for number in s:
        sum += translations[number]
    return sum

s = "CDXLIV"
print(super_roman_to_int(s))