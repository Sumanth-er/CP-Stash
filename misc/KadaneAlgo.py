arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
tot_sum = float('-inf')
r_sum=0

for i in range(n):
    r_sum+=arr[i]
    tot_sum=max(r_sum,tot_sum)
    if r_sum<0:
        r_sum=0


print(tot_sum)

