# Print square root of numbers given in list
from cmath import sqrt

def square_root(i):

    return sqrt(i)


l = {1,4,9,16,25}

ans = map(square_root,l)

# ans = map(lambda i:sqrt(i) , l)

print(list(ans))