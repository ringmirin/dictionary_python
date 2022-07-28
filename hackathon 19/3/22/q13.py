# Given an integer array nums, move all 0's to the end of it while maintaining the 
# relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
 
# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

# nums=[0,1,0,3,12]
# i=0
# temp=[]
# zeroes=[]
# while i<len(nums):
#    if nums[i]!=0:
#       temp.append(nums[i])
#    else:
#       zeroes.append(nums[i])
#    i+=1
# print(temp+zeroes)


 #####
# def move_zero(nums):
#    i=0
#    temp=[]
#    zeroes=[]
#    while i<len(nums):
#       if nums[i]!=0:
#          temp.append(nums[i])
#       else:
#          zeroes.append(nums[i])
#       i+=1
#    return temp+zeroes
# print(move_zero([0,1,0,3,12]))