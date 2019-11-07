#n spaced string 

# red blue green =>der eulb neerg

#first line testcases
#second line n spaced strings

test=int(input())
while(test>0):
    arr=input().split()
    for i in range(len(arr)):
        temp=list(arr[i])
        temp.reverse()
        arr[i]=''.join(temp)
    print(arr)

    test-=1