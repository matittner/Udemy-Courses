// Mateus H. Ittner 30/03/2019

var winrgb = [0, 0, 0]
var btneasy = document.getElementById("dif-easy");
var btnhard = document.getElementById("dif-hard");
var btnnew = document.getElementById("newcolor");
var csquare = document.getElementsByClassName("color-square");
var hardmode = true; // false for easy difficulty, true for hard
var chosen;
var message = document.getElementById("message");
var won = false;

function colorCreator() {
    // returns an array with 3 numbers between 0-255
    var rgb = [0, 0, 0];
    rgb[0] = Math.round(Math.random() * 256);
    rgb[1] = Math.round(Math.random() * 256);
    rgb[2] = Math.round(Math.random() * 256);
    return rgb;
}

function changeDifficulty() {
    // toggle visibility of color squares for each difficulty
    hardmode = !hardmode;
    reset();
    btneasy.classList.toggle("active");
    btnhard.classList.toggle("active");
    if (!hardmode) {
        csquare[3].classList.add("d-none");
        csquare[4].classList.add("d-none");
        csquare[5].classList.add("d-none");
    }
}

function squareAmount() {
    // checks the difficulty and returns a number of how many squares are in use
    if (hardmode) {
        return 6;
    } else {
        return 3;
    }
}

function colorize() {
    // adds a new random color for each square
    var color;
    for (var i = 0; i < squareAmount(); i++) {
        color = colorCreator();
        csquare[i].style.background = "rgb(" + color[0] + "," + color[1] + "," + color[2] + ")";
        csquare[i].classList.remove("d-none");
    };
}

function pickWinner() {
    chosen = Math.round(Math.random() * (squareAmount() - 1));
    console.log("chosen = " + chosen);
    csquare[chosen].style.background = "rgb(" + winrgb[0] + "," + winrgb[1] + "," + winrgb[2] + ")";
}

function checkWinner(square) {
    if (square == csquare[chosen]) {
        message.textContent = "You won!";
        btnnew.textContent = "PLAY AGAIN?";
        winnerColor();
        won = true;
    } else {
        message.textContent = "Try again!";
        square.classList.add("d-none");
    };
}

function winnerColor() {
    //color the background and squares with the winners color
    for (var i = 0; i < squareAmount(); i++) {
        csquare[i].style.background = "rgb(" + winrgb[0] + "," + winrgb[1] + "," + winrgb[2] + ")";
        csquare[i].classList.remove("d-none");
    }
    document.querySelector(".header").style.background = "rgb(" + winrgb[0] + "," + winrgb[1] + "," + winrgb[2] + ")";
    document.querySelector(".active").style.background = "rgb(" + winrgb[0] + "," + winrgb[1] + "," + winrgb[2] + ")";
}

function reset() {
    document.querySelector(".header").style.background = "rgb(60,118,174)";
    document.querySelector(".active").style.background = "";
    message.textContent = "";
    btnnew.textContent = "NEW COLORS";
    winrgb = colorCreator();
    won = false;
    document.getElementById("r").textContent = winrgb[0];
    document.getElementById("g").textContent = winrgb[1];
    document.getElementById("b").textContent = winrgb[2];
    colorize();
    pickWinner();
}


btnnew.addEventListener("click", reset);

btneasy.addEventListener("click", function () {
    if (hardmode && !won) {
        changeDifficulty();
    };
});

btnhard.addEventListener("click", function () {
    if (!hardmode && !won) {
        changeDifficulty();
    }
});

for (var i = 0; i < 6; i++) {
    csquare[i].addEventListener("click", function () {
        if (!won) {
            checkWinner(this);
        }
    });
}

reset();