def anagram(a,b):
    a1=list(a)
    b1=list(b)
    if(len(a)==len(b)):
        a1.sort()
        b1.sort()
        if(a1==b1):
            return True
    return False

print(anagram('abdc','dcba'))