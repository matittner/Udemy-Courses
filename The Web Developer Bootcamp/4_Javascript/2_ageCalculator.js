// Workaround for loading the HTML first in Google Chrome
window.setTimeout(function () {
  var age = prompt("What is your age?");
  age = age * 365;
  console.log("You've been alive for " + age + " days.");
  alert("You've been alive for " + age + " days.");
}, 500);