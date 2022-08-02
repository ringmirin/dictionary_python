# Write a program such that the below given dictionaries are into a single dictionary 
# and add the values having same key.


from collections import Counter
dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
d=Counter(dic1)+Counter(dic2)+Counter(dic3)
print(d)

#####


##{1: 10, 2: 60, 3: 30, 5: 50, 6: 60}
      
 
   