//Reference: https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Array
//Reference: https://ccckmit.gitbooks.io/javascript/content/ch5/chapter5.html
//Reference: https://ccckmit.gitbooks.io/javascript/content/ch3/chapter3.html
//let 與 var不同之處：https://realdennis.medium.com/%E9%96%92%E8%81%8A-var%E8%88%87let%E7%9A%84%E6%87%B6%E4%BA%BA%E5%8C%85-javascript-b5a3f40ee28d
function avg(data){
    // 請用你的程式補完這個函式的區塊
    var salarySum = 0;
    var salaryAvg = 0;
    var headCount = 0;
    var employeesList = data.employees;    //data是字典，要取出要使用data.employees
    for(i=0; i<data.count; i++){           //data是字典，要取出3要使用data.count
        headCount = headCount + 1
    };
    for(j=0; j<headCount; j++){
        eachSalary = employeesList[j].salary;
        salarySum += eachSalary;
    }
    j+=1;
    salaryAvg = salarySum / headCount;
    document.write(salaryAvg)
}

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
}); // 呼叫 avg 函式



//employees是個array
//var employees = [{"name":"John","salary":30000}, {"name":"Bob", "salary":60000}, {"name":"Jenny","salary":50000}]
//跑出打印結果
//console.log(employees)
/*[
    { name: 'John', salary: 30000 },
    { name: 'Bob', salary: 60000 },
    { name: 'Jenny', salary: 50000 }
  ]
*/
//console.log(employees[0])
//{ name: 'John', salary: 30000 }

//console.log(employees[0].salary)
//30000