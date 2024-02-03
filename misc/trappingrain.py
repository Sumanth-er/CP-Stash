def fun(n,arr):
    l=[]
    r=[]
    mx=0
    for i in range(n):
        mx=max(arr[i],mx)
        l.append(mx)
    mx1=0
    for i in range(n-1,-1,-1):
        mx1=max(arr[i],mx1)
        r.append(mx1)
    r=r[::-1]
    ans=[]
    for i,j in zip(l,r):
        ans.append(min(i,j))
    count=0
    for i in range(n):
        temp=ans[i]-arr[i]
        if temp>0:
            count+=temp
    return count
n=int(input())
arr=list(map(int,input().split()))
print(fun(n,arr))