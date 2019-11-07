list=[1,3,6,5,4,8,10,12,13,17,15]

squares={}
result={}

def square(x):#using dp to calculate squares
    try:
        return sqaures[x]
    except:
        squares[x]=x*x
        return squares[x]


def triplet(list,i,j,k):#using recursion for computing the triplets
    if(i==j):
        return 
    else:
        if(square(list[i])+square(list[j])==square(list[k])):
            result[(list[i],list[j],list[k])]=True
            return
        elif(square(list[i])+square(list[j])<square(list[k])):
            triplet(list,i+1,j,k)
        elif(square(list[i])+square(list[j])>square(list[k])):
            triplet(list,i,j-1,k)

list.sort()
print(list)
for i in range(len(list)-1,1,-1):
    triplet(list,0,len(list)-2,i)
print("Triplets:")
print(result)
