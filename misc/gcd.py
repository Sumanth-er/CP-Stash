"""
print gcd of 2 numbers

used euclidean algo

gcd(a,b)=gcd(a-b,b) where a>b
"""


def gcd(a, b):
    if a == 0:
        return b
    print(b % a, a)
    return gcd(b % a, a)


print("GCD = ", gcd(12, 10))
