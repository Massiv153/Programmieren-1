class Primzahlen:
    x=(int)(input("Bis wohin sollen die Primzahlen ausgegeben werden: "))
    isPrime= True
    for i in range (x):
        for e in range (2,i,1):
            if i % e == 0:
                isPrime=False
                break
        if isPrime:
                print(i)
        isPrime=True
