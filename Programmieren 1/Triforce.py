def dreieck(size):
    zaehler=0
    for i in range(size):
        for e in range(size-i,0,-1):
            print(" ",end="")
        for e in range(0,i,1):
            if(zaehler%2==0):
                print("°",end="")
            else:
                print("*",end="")
        for e in range(i-1):
            if(zaehler%2==0):
                print("°",end="")
            else:
                print("*",end="")
        print("")
        zaehler=zaehler+1

dreieck(10)