#Reference:https://sites.google.com/site/ezpythoncolorcourse/dict、 https://stackoom.com/question/3yOX7/%E5%A6%82%E4%BD%95%E5%AF%B9%E5%AD%97%E5%85%B8%E4%B8%AD%E7%9A%84%E5%80%BC%E6%B1%82%E5%B9%B3%E5%9D%87%E5%80%BC
#python的list，符號為[]
#python的dic，符號為{}
#employees是list

def avg(data):
# 請用你的程式補完這個函式的區塊
    salarySum = 0
    salaryAvg = 0
    headCount = 0
    employeesList = data['employees']
    for i in range(0, int(data['count'])):
        headCount += 1              #算出count是多少，也就是人數多少
 
    for j in range(0,headCount):    #<class 'list'>  
        each = (employeesList[j])
        eachSalary = each['salary'] #每個name的salary
        salarySum += eachSalary
    j+=1                        #salarySum是所有人salary的加總

    salaryAvg = salarySum / headCount
    print('Average Salary: '+str(salaryAvg)) 

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式



# 呼叫 avg 函式

#字典
                                #key            #key 
#data={"count":3, "employees":[{"name":"John", "salary":30000}, {"name":"Bob", "salary":60000}, {"name":"Jenny", "salary":50000}]}
#data['employees']是一個list名稱
#data['employees'][0] 抓第一組
#data['employees'][1] 抓第二組
#data['employees'][2] 抓第三組
#print(data['count'])     #取出3
#employeesList = data['employees']
#print(data['employees']) #取字典內容要用[]
#print(type(employeesList))    #<class 'list'>
#print(employeesList[0])       #{'name': 'John', 'salary': 30000}
#print(type(employeesList[0])) #<class 'dict'>