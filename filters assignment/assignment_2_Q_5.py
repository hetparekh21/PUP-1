# Convert a number to positive if it's negative in the list. Only pass those that are converted from negative to positive to the new list.[Try using map inside filter]

def convert(i):

    if i < 0 :
        return True


l = [1,-2,-3,9,-10]

ans = filter(lambda i: True if i > 0 else False,map(lambda x : x*-1,l ))

print(list(ans))


