def rotate(a,k):
    for i in range(k%len(a)):
        temp=a[0]
        del a[0]
        a.append(temp)
    return a

a=[10,20,30,40]
print(rotate(a,10000000000))