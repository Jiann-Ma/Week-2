#Reference:http://pythonpro.weebly.com/ch6-3685222280-3272238988.html
'''
def calculate(min, max):
# 請用你的程式補完這個函式的區塊
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後在 console 印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後在 console 印出 30
'''

def calculate(min, max):
    sum = 0
    for min in range(min,max+1):
        sum += min
    print(sum)

calculate(1, 3)
calculate(4, 8)


