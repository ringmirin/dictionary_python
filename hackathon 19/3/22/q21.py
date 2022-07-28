# # Two strings are anagrams if you can make one from the other by rearranging the letters.
# # Write a function named is_anagram that takes two strings as its parameters. Your 
# # function should return True if the strings are anagrams, and False otherwise.
# # For example, the call is_anagram("typhoon", "opython") should return True while the 
# # call is_anagram("Alice", "Bob") should return False.

def is_anagram():
   a1=a.lower()
   b2=b.lower()
   if len(a)==len(b):
      if a1[-1]==b2[-1]:
         print(a,"and",b, "are anagram")
      else:
         print(a, "and" ,b, "are not anagram")
   else:
      print(a,"and",b,"are not anagram")
a=input("enter the words: ")
b=input("enter the words: ")
is_anagram()