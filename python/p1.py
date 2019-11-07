#get spaced integers and store them in a list and sort them

#first line testcases
#second line n spaced integers 

#3 7 5 => [3,7,5] =>[3,5,7]

test=int(input())
while(test>0):
    num=[int(x)for x in input().split()]
    num.sort(reverse=True)
    print(num)
    test-=1
