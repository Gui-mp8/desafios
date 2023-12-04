def str_is_palindrome(x: int) -> bool:
    numbers = str(x)
    reversed = numbers[::-1]
    if numbers == reversed:
        return True

def int_is_palindrome(x):
    if x < 0 or (x != 0 and x % 10 == 0):
        return False

    half = 0
    while x > half:
        half = (half * 10) + (x % 10)
        x = x // 10

    return x == half or x == half // 10

x = 121
print(str_is_palindrome(x))
print(int_is_palindrome(x))