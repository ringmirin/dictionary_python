# Write a function named mid that takes a string as its parameter. Your function should 
# extract and return the middle letter. If there is no middle letter, your function 
# should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(n):
   if len(n)%2==0:
      return " "
   else:
      mid=int(len(n)/2) 
      return n[mid:mid+1]
n=input("enter the string: ")
print(mid(n))