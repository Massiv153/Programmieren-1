def max(l):
    speicher=l[0]
    for i in l:
        if speicher<i:
            speicher=i
    return speicher
def min(l):
    speicher=l[0]
    for i in l:
        if speicher>i:
            speicher=i
    return speicher

l=[3,5,93,2,34,1,423,3,22,7]
print(min(l))
print(max(l))

m=["h","a","b"]
print(min(m))
print(max(m))