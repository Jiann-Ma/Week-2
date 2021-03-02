'''
def twoSum(nums, target):
# your code here
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9
'''

#nums是一個list
#target是一個int
'''
def twoSum(nums, target):
    for i in range(len(nums)):             #列出所有組合，但只有順序不同就不列
   #for i in range(len(nums)-1)  這也可以，因為j永遠都出現在i後面，所以i部可能是最後一個。     
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                print([i, j])

#寫法二

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                print([i, j])
'''
#寫法三
def twoSum(nums, target):
        dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in dict:
                print([dict[target-x], i])
            dict[x] = i


twoSum([2, 11, 7, 15], 9)