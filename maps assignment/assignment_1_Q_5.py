# Eliminate duplicate letter from given string
import re

string = ""

def duplicate(i):

    global string
    if re.search(i,string) == None:
        
        string += i  

    return


l = "aabbbccc"

ans = map(duplicate,list(l))

print(list(ans)) # it doesn't work when this is commented , why ????? 

print(string)
