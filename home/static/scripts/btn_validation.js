const btnValidation = document.getElementById("btn_validation");
const campInput = document.getElementById("id_ticket");

function changeInput() {
    if(campInput.value.trim() === "") {
        btnValidation.setAttribute("disabled", "true");
    } else {
        btnValidation.removeAttribute("disabled")
    }
}

changeInput()

campInput.addEventListener("input", changeInput)