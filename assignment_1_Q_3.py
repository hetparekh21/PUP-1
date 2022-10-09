# Print all string in lower case from given tuple

def to_lower(i):

    return i.lower()


l = ('A','B','C','D','E')

# ans = map(to_lower,l)

ans = map(lambda i:i.lower() , l)

print(list(ans))