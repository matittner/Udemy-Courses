// Workaround for loading the HTML first in Google Chrome

window.setTimeout(function () {

    quit = false;
    var choice;
    var todolist = [];

    while (!quit) {
        choice = prompt("What do you want to do?")
        choice = choice.toLowerCase();
        if (choice.includes("new") || choice.includes("add")) {
            todolist.push(prompt("What do you want to add?"));
        } else if (choice.includes("list") || choice.includes("view")) {
            console.log(todolist);
        } else if (choice.includes("quit") || choice.includes("exit")) {
            console.log("Quitting!");
            quit = true;
        } else {
            console.log("Invalid Choice.");
        }
    }
}, 500);