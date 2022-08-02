# # Write a program to create a dictionary with all numbers from 1 to 15 as the keys 
# # and their squares as the corresponding values.

dict={}
i=1
while i<=15:
   a=i*i 
   dict[i]=a
   i+=1
print(dict)
