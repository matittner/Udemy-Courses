// Workaround for loading the HTML first in Google Chrome

function isEven(num){
    if (num % 2 == 0){
        return true;
    }
    else {
        return false;
    }
}

function factorial(num){
    var total = 1;
    for (i = 1; i <= num; i++){
        total = total * i;
    }
    return total;
}

function kebabToSnake(str){
    return str.replace(/-/g,"_");
}

window.setTimeout(function () {
    var test;
    test = prompt("Function isEven(), enter a number:");
    alert(isEven(test));
    test = prompt("Function factorial(), enter a number:");
    alert(factorial(Number(test)));
    test = prompt("Function kebabToSnake(), enter a string:");
    alert(kebabToSnake(test));
  }, 500);