# This time using filter() and list() functions filter all the positive integers in the string.

def neg_(i):

    if i in "0123456789" :
        return True


string = "1-2378356"

l = list(string)

ans = filter(neg_, l)

print(list(ans))
