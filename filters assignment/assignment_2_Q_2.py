# Using filter function, filter the even numbers so that only odd numbers are passed to the new list.

def even_odd(i):

    if i % 2 != 0 :
        return True


l = [1,2,3,4,5,6]

# ans = filter(even_odd, l)

ans = filter(lambda x:x %2 != 0,l)

print(list(ans))
