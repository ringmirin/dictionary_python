# # Chef wants to reach home as soon as possible. He has two options:
# # Travel with his BIKE which takes X minutes.
# # Travel with his CAR which takes Y minutes.
# # Which of the two options is faster or do they both take the same time?
# # Input Format
# # First-line will contain T, the number of test cases. Then the test cases follow.
# # Each test case contains a single line of input, two integers X, Y representing the 
# # time taken to travel with BIKE and CAR respectively.
# # Output Format
# # For each test case, print CAR if traveling with a car is faster, BIKE if traveling 
# # with a Bike is faster, SAME if they both take the same time.
# # You may print each character of CAR, BIKE, and SAME in uppercase or lowercase 
# # (for example, CAR, Car, cAr will be considered identical).
# # Sample Input 1 
# # 1 5
# # 4 2
# # 6 6
# # Sample Output 1 
# # BIKE
# # CAR
# # SAME


bike=int(input("minutes took by bike: "))
car=int(input("minutes took by cars: "))
if bike<car:
   print("BIKE")
elif bike>car:
   print("CARS")
else:
   print("SAME")


######## 

def traveling():
   if bike<car:
      return "BIKE"
   elif bike>car:
      return "CAR"
   else:
      return "SAME"
bike=int(input("minute took by bike: "))
car=int(input("minute took by car: "))
print(traveling())