# # Count the total number of items from the values of the dictionary which are in 
# # the form of a list.

dict1 =  {
   'Alex': ['subj1', 'subj2', 'subj3'], 
   'David': ['subj1', 'subj2']}
count=0
for l in dict1.values():
   for i in l:
      count+=1
print(count)
