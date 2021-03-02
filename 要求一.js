function calculate(min, max){
    // 請用你的程式補完這個函式的區塊
    let sum = 0;
    for(i=min; i<=max; i++){
        sum = sum + min;
        min++;
    }
    document.write(sum);
}


calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後在 console 印出 6
//calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後在 console 印出 30
