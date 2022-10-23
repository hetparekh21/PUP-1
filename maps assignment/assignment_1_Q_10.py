# Add ‘@gmail.com’ to all the values of given dictionary and convert it to lower case.

def mail(i):

    return i.lower() + "@gmail.com"


l = ('A','B','C','D','E')

# ans = map(mail,l)

ans = map(lambda i:i.lower() + "@gmail.com" , l)

print(list(ans))
