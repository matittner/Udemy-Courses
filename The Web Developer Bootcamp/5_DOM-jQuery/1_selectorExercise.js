var firstp = null;

window.setTimeout(function(){
    firstp = document.getElementById("first");
    firstp.textContent = "Selected for the first time using getElementByID";
    firstp.style.color = "blue";
},1500);


window.setTimeout(function(){
    firstp = document.getElementsByClassName("special");
    firstp[0].textContent = "Selected for the second time using getElementsByClassName[0]";
    firstp[0].style.color = "red";
},3000);

window.setTimeout(function(){
    firstp = document.getElementsByTagName("p");
    firstp[0].textContent = "Selected for the third time using getElementsByTagName[0]";
    firstp[0].style.color = "pink";
},4500);

window.setTimeout(function(){
    firstp = document.querySelector(".special");
    firstp.textContent = "Selected for the fourth time using querySelector(.special)";
    firstp.style.color = "red";
},6000);

window.setTimeout(function(){
    firstp = document.querySelector("p");
    firstp.textContent = "Selected for the fifth time using querySelector(p)";
    firstp.style.color = "purple";
},7500);

window.setTimeout(function(){
    firstp = document.querySelectorAll("p");
    firstp[0].textContent = "Selected for the sixth time using querySelectorAll[0]";
    firstp[0].style.color = "green";
},9000);

