def palindrome (s):
    l=list(s)
    for i in range (len(l)):
        if (l[i]!=l[len(l)-1-i]):
            return False
    return True