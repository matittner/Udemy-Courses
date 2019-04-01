var button = document.querySelector("button");
var clicked = false;

button.addEventListener("click",function(){
    clicked = !clicked;
    if (clicked){
        document.body.style.background= "purple";
    }
    else{
        document.body.style.background= "white";
    }
});