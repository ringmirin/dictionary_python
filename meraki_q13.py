# # Write a program to sort a dictionary in ascending or descending according to 
# # its values .

my_dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}

dict={}
a_dic=sorted(my_dic, key=my_dic.get)[::-1]
for x in a_dic:
   dict[x]=my_dic[x]
print("ascending",dict)
diction={}
d_dic=sorted(my_dic,key=my_dic.get)
for y in d_dic:
   diction[y]=my_dic[y]
print("descending",diction)



######
rec = {
"Name" : "Python", 
"Age":"20",
"Addr" : "NJ", 
"Country" :"USA"
}
id1 = id(rec)
del rec

rec = {
   "Name" : "Python", 
   "Age":"20", 
   "Addr" : "NJ", 
   "Country" : "USA"
   }
id2 = id(rec)
print(id == id2)

