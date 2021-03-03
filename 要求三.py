
#Reference:https://www.runoob.com/python/att-list-max.html、https://newaurora.pixnet.net/blog/post/228238004-python-list%E8%B3%87%E6%96%99%E8%AE%80%E5%8F%96%E3%80%81%E5%A2%9E%E5%8A%A0%E3%80%81%E5%88%AA%E9%99%A4%E3%80%81%E4%BF%AE%E6%94%B9%E6%96%B9%E6%B3%95
def maxProduct(nums):            #nums是個list
# 請用你的程式補完這個函式的區塊
    count = 0
    eachSet = 0
    sumSet = []
    #所有不自我重複的組合
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            count += 1
            eachSet = nums[i]*nums[j]
            sumSet.append(eachSet)
            #print(eachSet)               #這時候得出所有六種組合的值
    print(max(sumSet))                    #這時候得出所有六種組合的值，是一組list，再用max()抓出最大值
    #print(count)                         #總共有六種組合


maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值



