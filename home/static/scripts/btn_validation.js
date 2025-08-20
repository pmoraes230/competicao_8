const btnValidation = document.getElementById("btn_validation");
const campInput = document.getElementById("id_ticket");

function changeInput() {
    if(campInput.value.trim() !== "") {
        btnValidation.removeAttribute("disabled");
    } else {
        btnValidation.setAttribute("disabled", "true");
    }
}

changeInput()

campInput.addEventListener("input", changeInput)