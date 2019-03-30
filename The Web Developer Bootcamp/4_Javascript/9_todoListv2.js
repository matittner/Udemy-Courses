// Workaround for loading the HTML first in Google Chrome

function printall(list) {
    console.log("************");
    list.forEach(function (todo, i) {
        console.log(i + ". " + todo);
    });
    console.log("************");
}


window.setTimeout(function () {

    quit = false;
    var choice;
    var todolist = [];
    var str;

    while (!quit) {
        choice = prompt("What do you want to do?")
        choice = choice.toLowerCase();
        if (choice.includes("new") || choice.includes("add")) {
            str = prompt("What do you want to add?");
            todolist.push(str);
            console.log(str + " added to the list.")
        } else if (choice.includes("list") || choice.includes("view")) {
            printall(todolist);
        } else if (choice.includes("delete") || choice.includes("remove")) {
            str = prompt("Enter index to delete.");
            Number(str);
            todolist.splice(str, 1);
            console.log("Index " + str + " removed from the list.")
        } else if (choice.includes("quit") || choice.includes("exit")) {
            console.log("Quitting!");
            quit = true;
        } else {
            console.log("Invalid Choice.");
        }
    }
}, 500);