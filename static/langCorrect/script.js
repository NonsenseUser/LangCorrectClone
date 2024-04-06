let correct = document.getElementsByClassName("edit");
    console.log("Коррект")
    console.log(correct);
    for (let i = 0; i < correct.length; i++) {
    correct[i].addEventListener("click", function() {
        // Показать новый элемент, установив его стиль display в значение "block"
        let correctWindow = document.getElementsByClassName("correctWindow")[i];
        console.log(correctWindow.style.display)
        if (correctWindow.style.display == "none"){
            correctWindow.style.display = "block";
            } else {
            correctWindow.style.display = "none";
            }
    });
}