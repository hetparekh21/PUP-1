# Using filter() and list() functions and .lower() method filter all the vowels in a given string

def vow(i):
    if(i in "aeiou"):
        return True

l = "Het Kirtan Jinay"

list_ = list(l)

lower_str = map(lambda i: i.lower() , list_ )

lower_str = list(lower_str)

ans = filter(vow,lower_str)

print(list(ans))


