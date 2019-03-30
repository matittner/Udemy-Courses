var counter;

console.log("Print all numbers between -10 and 19.");
counter = -10;
while (counter < 19) {
    counter++;
    console.log(counter);
}

console.log("Print all numbers between 10 and 40.");
counter = 10;
while (counter < 40) {
    counter++;
    console.log(counter);
}

console.log("Print all numbers between 300 and 333.");
counter = 300;
while (counter < 333) {
    counter++;
    console.log(counter);
}

console.log("Print all numbers divisible by 5 and 3 between 5 and 50.");
counter = 5;
while (counter < 50) {
    counter++;
    if (counter % 5 == 0 && counter % 3 == 0)
        console.log(counter);
}