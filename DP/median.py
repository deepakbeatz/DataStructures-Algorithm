import math

def insertionSort(arr,e):
    arr.append(e) 
    for i in range(1, len(arr)): 
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
    return arr

table={}

def median(arr,Q):#this function returns the sorted array
    #using DP to get the sorted array using recursive equation[  table[i,j]=insertionSort(table[i,j-1],arr[j]) ]
    l,r=Q
    try:
        return table[(l,r)]
    except:
        if(l==r):
            table[(l,r)]=[arr[l]]
            return [arr[l]]
        if(r<l):
            return "Error"
        else:
            table[(l,r)]=insertionSort(median(arr,(l,r-1)),arr[r])
    return table[(l,r)]

arr=[1,7,5,6,4,8,2,10,11,15,20,18,19,23,24,25,26,27,28,30,3,5,6,7,8]
Q=[(0,5),(4,6),(0,7),(2,6),(4,15)]

for i in Q:
    res=median(arr,i)
    print(res)#sorted array
    print(res[math.ceil(len(res)/2)-1])#median

