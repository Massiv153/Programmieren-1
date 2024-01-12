def double_letters (s):
    speicher=""
    for i in s:
        if(i==speicher):
            return True
        speicher=i
    return False

x=input("Eingabe: ")
print(double_letters(x))