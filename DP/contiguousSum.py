def csum(arr):
    maxsum=0
    for i in range(1,len(arr)):
        cursum=0
        for j in range(0,i+1):
            cursum+=arr[j]
            if(cursum<0):
                cursum=0
            if(cursum>maxsum):
                maxsum=cursum
    return maxsum

print(csum([10,20,-30,40,50,70]))