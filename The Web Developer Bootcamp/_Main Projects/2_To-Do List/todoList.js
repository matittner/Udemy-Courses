// Mateus H. Ittner 31/03/2019

$("ul").on("click", "li", function () {
    $(this).toggleClass("completed");
});

$("ul").on("click","span", function () {
    $(this).closest("li").fadeOut(1000,function(){
        $(this).remove();
    });
});

$("input").keypress(function (e) {
    if (e.which == 13) {
        var text = $(this).val();
        $(this).val("");
        $("ul").append($("<li><span><i class=\"fas fa-trash-alt\"></i></span>" + text + "</li>").hide().fadeIn(1000));
    }
});

$("h1").on("click", "i", function () {
    $("input").fadeToggle(100);
});

