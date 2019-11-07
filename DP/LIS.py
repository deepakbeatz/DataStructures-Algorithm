def seq(num):
    lis=[1]
    for i in range(1,len(num)):
        lis.append(1)
        for j in range(0,i):
            if(num[i]>num[j] and lis[i]<=lis[j]):
                lis[i]=lis[j]+1
    return lis

print(max(seq([1,2,0,5,6,7,3,2,8,4,5,9])))
