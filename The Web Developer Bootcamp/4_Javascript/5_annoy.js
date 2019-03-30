// Workaround for loading the HTML first in Google Chrome
window.setTimeout(function () {

    arrived = false;
    var answer;

    while (!arrived) {
        answer = prompt("Are we there yet?")
        answer = answer.toLowerCase();
        if (answer == "yes" || answer == "yeah" || answer.includes("yes") || answer.includes("yeah")) {
            alert("Yay, we finally made it!");
            arrived = true;
        }
    }
}, 500);