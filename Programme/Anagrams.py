def is_anagram(a1,a2):
    s=False
    a2=list(a2)
    for i in a1:
        for e in range(0,len(a2)-1):
            if i==a2[e]:
                s=True
                del a2[e]
                break
        if s==False:
            return False
        s=False
    return True
