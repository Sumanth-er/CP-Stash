"""
find total numer of ways to encode
"""


def fun(s):
    if s == 0 or len(s) == 1 and s[0] == "0":
        return 0
    return helper(s, len(s))


def helper(s, n):
    if n == 0 or n == 1:
        return 1
    count = 0
    if s[n - 1] > '0':
        counter = helper(s, n - 1)
    if s[n - 2] == '1' or s[n - 2] == '2' and s[n - 1] < '7':
        counter = helper(s, n - 2)
    return counter


s = int(input())
print(fun(s))
