def sub(s):
    st=[]
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            st.append(s[i:j])
    return st

def palindrome(s):
    i=0
    j=-1
    for i in range(len(s)//2):
        if(s[i]!=s[j]):
            return False
        i+=1;
        j-=1
    return True



def long(s):
    max=0
    substrings=sub(s)
    res=""
    for i in substrings:
        if(palindrome(i)):
            if(len(i)>max):
                max=len(i)
                res=i
    return res

print(long('abcba'))
