// Workaround for loading the HTML first in Google Chrome

function reverseArray(sarray) {
    for (var i = sarray.length - 1; i >= 0; i--) {
        console.log(sarray[i]);
    }
}

function isUniform(sarray) {
    firstelement = sarray[0];
    for (var i = 1; i < sarray.length; i++) {
        if (!(sarray[i] === firstelement)) {
            return false;
        }
    }
    return true;
}

function sumArray(sarray) {
    total = 0;
    sarray.forEach(function (num) {
        total += num;
    });
    return total;
}

function max(sarray) {
    max = sarray[0];
    for (var i = 1; i < sarray.length; i++) {
        if (sarray[i] > max) {
            max = sarray[i];
        }
    }
    return max;
}

var simplearray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log("Original array:");
console.log(simplearray);
console.log("Function reverseArray():");
reverseArray(simplearray);
console.log("-------------------");

console.log("Function isUniform():");
console.log("Original array:");
console.log(simplearray);
console.log("isUniform returns " + isUniform(simplearray));
simplearray = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
console.log("Original array:");
console.log(simplearray);
console.log("isUniform returns " + isUniform(simplearray));
console.log("-------------------");


simplearray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log("Original array:");
console.log(simplearray);
console.log("Function sumArray():");
console.log("sumArray() returns " + sumArray(simplearray));
console.log("-------------------");

console.log("Original array:");
console.log(simplearray);
console.log("Function max():");
console.log("max() returns " + max(simplearray));
console.log("-------------------");
