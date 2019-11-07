#code

t=int(input())

while(t>0):
    s=input()
    
    if(len(s)%2==0):
        i=len(s)//2-1
        j=len(s)//2
    else:
        i=len(s)//2
        j=len(s)//2
    
    st=[]
    for w in s:
        st.append(w)
    
    while(i>0 and j<len(st)):
        if(st[i]==st[j]):
            i-=1;
            j+=1
        else:
            a=st[i]
            b=st[j]
            st.insert(i+1,a)
            st.insert(i,b)
            i-=1
            j+=1
    print(("".join(st)))        
    print(len("".join(st))-len(s))
        
    
    t-=1

