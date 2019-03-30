
// Workaround for loading the HTML first in Google Chrome
window.setTimeout(function() {
    var firstName = prompt("What is your first name?");
    var lastName = prompt("What is your seconde name?");
    var age = prompt("How old are you?");
    console.log("Your name is " + firstName + " " + lastName + ".");
    console.log("You're " + age + " years old");
  }, 500);