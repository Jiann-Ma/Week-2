#Reference: https://stackoverflow.com/questions/40166522/find-longest-sequence-of-0s-in-the-integer-list

def maxZeros(nums):
    count = 0
    prev = 0
    for i in range(0, len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            if count > prev:
                prev = count
            count = 0
    print(prev)
# 請用你的程式補完這個函式的區塊


maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0



        


