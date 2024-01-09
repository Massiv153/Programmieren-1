def online_count (statuses):
    x=statuses.values()
    counter=0
    for i in x:
        if i=="online":
            counter=counter+1
    return counter

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Steve": "online",
}

print(online_count(statuses))