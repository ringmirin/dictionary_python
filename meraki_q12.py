# # Write a program to print the top 3 highest values of a given dictionary.

my_dict = {
   'a':50, 
   'b':58,
   'c': 56,
   'd':40,
   'e':100, 
   'f':20 
   }
d=sorted(my_dict, key=my_dict.get)[-3:]
print(d)


