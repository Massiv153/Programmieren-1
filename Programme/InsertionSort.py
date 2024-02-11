def insertionSort(l):
    a=list()
    a.append(l[0])
    for i in range(1,len(l)):
        for e in a:
            if l[i]>=e:
                a.insert(i,l[i])
    