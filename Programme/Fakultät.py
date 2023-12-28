def Fakultät(stelle):
    if stelle==1:
        return 1
    else:
        return stelle*Fakultät(stelle-1)
    
x=input("Stelle: ")
print(Fakultät(int(x)))