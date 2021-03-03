//從陣列中使用Math.max()拿出最大值的方法https://www.jstips.co/zh_tw/javascript/calculate-the-max-min-value-from-an-array/

function maxProduct(nums){
    // 請用你的程式補完這個函式的區塊

    var eachSet = 0;
    var sumSet = [];
    //所有不自我重複的組合
    for(i=0; i<nums.length; i++){
        for(j=i+1; j<nums.length; j++){
            eachSet = nums[i]*nums[j];
            sumSet.push(eachSet)
        }
    }
    console.log(Math.max.apply(null, sumSet))
}


maxProduct([5, 20, 2, 6]); // 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]); // 得到 30 因為 10 和 3 相乘得到最大值