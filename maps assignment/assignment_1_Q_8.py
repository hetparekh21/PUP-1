# Convert all float digits into integer using built in function from given list.

def convert(i):

    return int(i)


l = {1.12 , 4.4 , 9.2 , 16.1 , 25.43}

ans = map(convert,l)

# ans = map(lambda i:int(i) , l)

print(list(ans))

