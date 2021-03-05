function maxZeros(nums){
    // 請用你的程式補完這個函式的區塊
    var count = 0;
    var prev = 0;
    for(i=0; i<nums.length; i++){
        if(nums[i] == 0){
            count += 1;
        }else{
            if (count > prev){
                prev = count;
            }
            count = 0
        }
    }
    console.log(prev)
}

maxZeros([0, 1, 0, 0]) // 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) // 得到 4
maxZeros([1, 1, 1, 1, 1]) // 得到 0