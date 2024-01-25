def largest_difference (l):
    s1=l[0]
    for i in l:
        if i<s1:
            s1=i
            
        s2=l[0]
    for i in l:
        if i>s2:
            s2=i
            
    return s2-s1