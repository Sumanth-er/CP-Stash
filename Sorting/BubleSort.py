arr=[1,2,3,4,5,6,6,1,3,4,5,3,5,9,4,2,8]
n=len(arr)
for i in range(1,n-1):
    for j in range(i,n):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(*arr)