def remove(s,i):
    if(i==len(s)):
        return s
    elif(s[i]==s[i-1] and i-1>=0):
        del s[i]
        return remove(s,i)
    return remove(s,i+1)

print(remove(list('bbbacccca'),1))

    

