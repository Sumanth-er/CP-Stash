
def one_to_n(n):
    if n == 1:
        print(1)
        return
    one_to_n(n - 1)
    print(n)


def n_to_one(n):
    if n==1:
        print(1)
        return
    print(n)
    n_to_one(n-1)

print('****1 to n****')
one_to_n(10)
print('****n to 1****')
n_to_one(10)
