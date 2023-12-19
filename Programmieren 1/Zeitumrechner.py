def tageInStunden(tage):
    return tage*24
def tageInMinuten(tage):
    return tage*24*60
def tageInSekunden(tage):
    return tage*24*60*60

def stundenInMinuten(stunden):
    return stunden*60
def stundenInSekunden(stunden):
    return stunden*60*60

def minutenInSekunden(minuten):
    return minuten*60

x=input("Eingabe: ")
y=x.split(" ")

match y[1]:
    case "Tage":
        match y[3]:
            case "Stunden":
                print((str)(tageInStunden((int)(y[0])))+" Stunden")
            case "Minuten":
                print((str)(tageInMinuten((int)(y[0])))+" Minuten")
            case "Sekunden":
                print((str)(tageInSekunden((int)(y[0])))+" Sekunden")

    case "Stunden":
        match y[3]:
            case "Minuten":
                print((str)(stundenInMinuten((int)(y[0])))+" Minuten")
            case "Sekunden":
                print((str)(stundenInSekunden((int)(y[0])))+" Sekunden")

    case "Minuten":
         match y[3]:
            case "Sekunden":
                print((str)(minutenInSekunden((int)(y[0])))+" Sekunden")

                      