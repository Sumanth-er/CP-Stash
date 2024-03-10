"""
there is a circle of people
each person kills next k-1 person till only 1 remains alive
find the position of alive person
"""


def josephus(n, k):
    i = 1
    ans = 0
    while i <= n:
        ans = (ans + k) % i
        i += 1
    return ans + 1


n = 14
k = 2
result = josephus(n, k)
print(result)
