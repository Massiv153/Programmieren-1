def bubbleSort(l):
    for i in l:
        for e in range(0,len(l)-i):
            if l[e]>l[e+1]:
                speicher =l[e+1]
                l[e+1]=l[e]
                l[e]=speicher
                
    return l                

x=[1,4,2,67,3,8]
print(bubbleSort(x))