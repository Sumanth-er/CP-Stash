"""
birthday coign
Your birthday is coming soon and one of your friends, Alex, is thinking about a gift for you. He knows that you really like integer arrays with interesting properties.

He selected two numbers, N and K and decided to write down on paper all integer arrays of length K (in form a[1], a[2], …, a[K]), where every number a[i] is in range from 1 to N, and, moreover, a[i+1] is divisible by a[i] (where 1 < i <= K), and give you this paper as a birthday present.

Alex is very patient, so he managed to do this. Now you’re wondering, how many different arrays are written down on this paper?

Since the answer can be really large, print it modulo 10000.
"""
n = int(input())
k = int(input())
count = 0
if k == 2:
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            print(i, j)
            count += 1
if k == 3:
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            for k in range(j, n + 1, j):
                print(i, j, k)
                count += 1
print(count)
