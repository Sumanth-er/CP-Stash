def solve(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[2,6,1,3,8,6,7]
print(solve(arr))