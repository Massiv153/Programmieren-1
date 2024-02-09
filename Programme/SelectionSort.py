def selectionSort(l):
    speicher=0
    a=list()
    for e in range (len(l)):
        for i in l:
            if speicher > i:
                speicher=i
        a.append(speicher)
        l.remove(speicher)
    