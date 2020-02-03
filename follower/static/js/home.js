$(document).ready(function () {
    let choiceInput = $("#sI");
    choiceInput.focus(function () {
        if(document.getElementById("sI").getAttribute("placeholder") !== "搜索"){
            document.getElementById("sI").value = document.getElementById("sI").getAttribute("placeholder")
        }
        document.getElementById("sI").setAttribute("placeholder", "");
        document.getElementById("removeText").style.display = "inline";

    });
    choiceInput.blur(function () {
        if(document.getElementById("sI").value !== ""){
            document.getElementById("sI").setAttribute("placeholder", document.getElementById("sI").value);
            document.getElementById("sI").value = "";
        }
        else {
            document.getElementById("sI").setAttribute("placeholder", "搜索");
        }

        document.getElementById("removeText").style.display = "none";

    })
});

$("#removeText").mousedown(function () {
    document.getElementById("sI").value = "";
    document.getElementById("sI").setAttribute("placeholder", "搜索");
    console.log("666");
});
