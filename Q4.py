def Q4(arr):
    arr.sort()
    arr4=[]
    arr5=[]
    n=len(arr)
    a=n/2
    for i in range(0,n):
        if(i<a):
            arr4.append(arr[i])
        elif(i>=a):
            arr5.append(arr[i])

    return arr4,arr5

arr1=[1,3,5,7]
arr2=[2,4,6,8]
arr=arr1+arr2
reuslt=Q4(arr)
print(reuslt)

