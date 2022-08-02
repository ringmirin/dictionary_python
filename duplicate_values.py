##find keys with duplicate values in the dictionary

some_dict = {"firstname": "Albert", "nickname": "Albert", 
             "surname": "Likins", "username": "Angel"}    
a_list={}
for key,value in some_dict.items():
   if value not in a_list.values():
      a_list[key]=value
print(a_list)

  

