class Weihnachtsternchen:
    reihen=(int)(input("Reihen eingeben: "))
    for i in range (reihen):
        for e in range (reihen-i):
            print(" ",end="")
        for e in range (i):
            print("*",end="")   
        print() 
