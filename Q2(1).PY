def missing_interger(arr):
    n=len(arr)
    n=n+1
    value =[0]*(n+1)
    for num in arr:
        value[num]+=1
    for i in range(1,n+1):
        if value[i]== 0:
            return i

    return -1
arr=[1,2,4,5]
missing=missing_interger(arr)
print(missing)
arr=[1,2,3,5,6,7,8,9,10]
missing=missing_interger(arr)
print(missing)
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
missing=missing_interger(arr)
print(missing)