# Write a function named add_dots that takes a string and adds "." in between each letter. 
# For example, calling add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots that removes 
# all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
# If both functions are correct, calling remove_dots(add_dots(string)) should return back 
# the original string for any string.
# (You may assume that the input to add_dots does not itself contain any dots.)

# def add_dots(string):
#    new_string=".".join(string)
#    return new_string
# print(add_dots("test"))
# def remove_dots(string):
#    new_string=string
#    result=new_string.replace(".","")
#    return result
# print(remove_dots("t.e.s.t"))
# print(remove_dots(add_dots("r.i.n.g")))



# def add_dots(string):
#    s=""
#    for letter in string:
#       s+=letter+"."
#    return s
# string=input("enter the string")
# print(add_dots(string))
# def remove_dots(string):
#    s=""
#    for letter in string:
#       if letter!=".":
#          s+=letter
#    return s
# string=input("enter word with dots: ")
# print(remove_dots(string))
# name=input("enter the word: ")
# print(remove_dots(add_dots(name)))