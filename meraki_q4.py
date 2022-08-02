# # Write a program to remove the first key value pair from a nested dictionary.

dic= {
   1: 'NAVGURUKUL',
   2: 'IN',  
   3:{
      'A' : 'WELCOME',
      'B' : 'To',
      'C' : 'DHARAMSALA'
      }
   }
del dic[3]["A"]
print(dic)
