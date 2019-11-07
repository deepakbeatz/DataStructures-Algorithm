def check(a,b):
    if(a==b[2:]+b[:2]):
        return True
    return False

print(check('abcd','cdab'))