def get_row_col (s):
    l=list(s)
    match l[0]:
        case "A":l[0]=0
        case "B":l[0]=1
        case "C":l[0]=2
        
    match l[1]:
        case "1":l[1]=0
        case "2":l[1]=1
        case "3":l[1]=2
    
    return tuple(l)

print(get_row_col("C1"))