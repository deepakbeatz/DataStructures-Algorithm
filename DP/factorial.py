facttable={}
def factorial(n):
    try:
        return facttable[n]
    except:
        if(n==0):
            facttable[0]=1
            return 1
        else:
            facttable[n]=n*factorial(n-1)
            return facttable[n]

print(factorial(50))