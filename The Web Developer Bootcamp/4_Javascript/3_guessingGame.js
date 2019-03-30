// Workaround for loading the HTML first in Google Chrome
window.setTimeout(function () {

    var correctNumber = 7;
    guessed = false;
    var number;

    while (!guessed) {
        number = prompt("Guess a number: ")
        if (number < 7) {
            alert("Too low, try again!");
        } else if (number > 7) {
            alert("Too high, try again!");
        } else if (number == 7) {
            guessed = true;
            alert("You guessed it!");
        } else {
            alert("That's not a number.");
        }
    }
}, 500);