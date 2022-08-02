# # Create a dictionary from 2 lists, where the elements of 1st list are the keys and 
# # the elements of the 2nd list are the corresponding values.

list1=["one","two","three","four","five"]
list2=[1,2,3,4,5]

dictionary=dict(zip(list1,list2))
print(dictionary)

