//  Mateus H. Ittner 30/03/19

var buttons = document.getElementsByTagName("button");
/* 
buttons[0] = player 1 button
buttons[1] = player 2 button
buttons[2] = reset button
 */
var winnerscoreinput = document.querySelector("input");
var h1 = document.querySelector("h1");

winnerscore = winnerscoreinput.value;
var winner = 0; // 0 -> no winner -- 1-> player one wins -- 2-> player 2 wins
var p1score = 0;
var p2score = 0;

function checkWinner(one, two) {
    // adds a green color to the winners score text and sets a winner (if there is one)
    if (p1score >= winnerscore) {
        winner = 1;
        h1.innerHTML = "<span style=\"color:green\">" + one + "</span>" + " v " + two;
    } else if (p2score >= winnerscore) {
        winner = 2;
        h1.innerHTML = one + " v " + "<span style=\"color:green\">" + one + "</span>";
    }
}

function updateScore(one, two) {
    h1.textContent = one + " v " + two;
}

function reset() {
    // reset the scores and the winner
    p1score = 0;
    p2score = 0;
    updateScore(p1score, p2score);
    winner = 0;
}

// buttons[0] = player 1 button
buttons[0].addEventListener("click", function () {
    // adds score to player and checks if there's a winner
    if (winner == 0) {
        p1score++;
        updateScore(p1score, p2score);
        checkWinner(p1score, p2score);
    }
});

// buttons[1] = player 2 button
buttons[1].addEventListener("click", function () {
    // adds score to player and checks if there's a winner
    if (winner == 0) {
        p2score++;
        updateScore(p1score, p2score);
        checkWinner(p1score, p2score);
    }
});

// buttons[2] = reset button
buttons[2].addEventListener("click", reset);

winnerscoreinput.addEventListener("input", function () {
    // updates the score to play to value and text content and resets the game
    reset();
    winnerscore = winnerscoreinput.value;
    document.querySelector("p").textContent = "Playing to: " + winnerscore;
});