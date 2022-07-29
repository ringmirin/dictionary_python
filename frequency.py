# # Store the unique letters and their frequency of the letters from the word 
# # "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies 
# # are the values.

word="MISSISSIPPI"
freq={}
for i in word:
   if i in freq:
      freq[i]+=1
   else:
      freq[i]=1
print(freq)


###
word="MISSISSIPPI"
dict={}
i=0
while i<len(word):
   if word[i] in dict:
      dict[word[i]]+=1
   else:
      dict[word[i]]=1
      i+=1
print(dict)