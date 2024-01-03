def capital_Indexes(s):
    counter=1
    for i in s:
        if i.isupper():
            print(counter)
        counter=counter+1    
        
x=input("Eingabe: ")
capital_Indexes(x)