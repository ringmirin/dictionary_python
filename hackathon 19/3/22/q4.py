# There are N bikes and M cars on the road.
# Each bike has 2 tyres.
# Each car has 4 tyres.
# Find the total number of tyres on the road.
# Input Format
# The first line will contain T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains two integers N,M.
# Output Format
# For each test case, output in a single line, the total number of tyres on the road.
# Sample Input 1 
# 2 1
# 3 0
 
# Sample Output 1 
# 8
# 6

#####
bike=int(input("enter the total of bikes: "))
car=int(input("enter the total of bikes: "))
biketyres=2
cartyres=4
print("total number of tyres: ",bike*biketyres+car*cartyres)


########
def tyres():
   biketyres=2
   cartyres=4
   bc=biketyres*bike+cartyres*car
   return bc
bike=int(input("enter no of bike: "))
car=int(input("enter no of car: "))
print(tyres())
   
   