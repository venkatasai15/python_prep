#Write a function to reverse a given string.


def r_str(s):
    return s[::-1]
s="Hello Welcome All"
a=r_str(s)
print(a)

#steps:-

#There is no built-in function to reverse a String in Python.
#The fastest (and easiest?) way is to use a slice that steps backwards, -1.
#the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backwards
