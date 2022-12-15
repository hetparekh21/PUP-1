# Separate even odd number from given list

even = []
odd = []

def even_odd(i):

    if(i % 2 == 0):
        
        global even
        even.append(i)

    else:
        global odd
        odd.append(i)


l = {1,2,3,4,5}

ans = map(even_odd,l) 

print(list(ans))

print(even)

print(odd)