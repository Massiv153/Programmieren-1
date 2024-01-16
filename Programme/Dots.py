def add_dots(s):
    s=s.replace("",".",len(s))
    return s[1:]

def remove_dots(s):
    s=s.replace(".","")
    return s

s="HALLO"
print(add_dots(s))
print(remove_dots(s))