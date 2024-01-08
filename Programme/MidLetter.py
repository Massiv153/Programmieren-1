def mid(s):
    l=list(s)
    if(len(l)%2==0):
        return ""
    else:
        return l[int(len(l)/2)]
    
x=input("String: ")
print(mid(x))