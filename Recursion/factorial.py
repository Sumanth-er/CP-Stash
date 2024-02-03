def recursion_fact(n):
    if n == 0:
        return 1
    sol = n * recursion_fact(n - 1)
    return sol


print(recursion_fact(10))
