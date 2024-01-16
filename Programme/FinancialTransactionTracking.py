b=[{"Type":"sale","Amount":"4","Date":5},{"Type":"purchase","Amount":"A lot","Date":8}]

def list_of(my_key,l):
    amount_values=[i[my_key] for i in l]
    return amount_values
print(list_of("Amount",b))