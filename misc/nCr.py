'''
shortcut for finding ncr
'''
def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1)
    return res


print(nCr(5, 2))
