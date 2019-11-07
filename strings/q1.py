def reverse(s):
    i=0
    j=len(s)-1
    st=[]
    
    for k in s:
        st.append(k)

    while(i<len(st)//2):
        st[i],st[j]=st[j],st[i]
        i+=1;
        j-=1;
    
    return "".join(st)

print(reverse("abcd"))
        

