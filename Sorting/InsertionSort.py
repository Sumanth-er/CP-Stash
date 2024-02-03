def insertionsort(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


arr = [5, 4, 2, 5, 6, 11, 9, 1, 10, 3]
arr = insertionsort(arr)
print(*arr)
