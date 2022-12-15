# Using filter() function filter the list so that only negative numbers are left.

def neg_(i):

    if i < 0 :
        return True


l = [-1,2,-3,4,-5,6]

# ans = filter(neg_, l)
ans = filter(lambda x: x < 0, l)
print(list(ans))