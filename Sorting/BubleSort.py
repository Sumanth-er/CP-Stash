arr=[1,2,3,4,5,6,6,1,3,4,5,3,5,9,4,2,8]
n=len(arr)

for i in range(n-1,0,-1):
    print(i)
    for j in range(i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]

print(*arr)