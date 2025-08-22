const inputPassword = document.getElementById("password_user");
const btnPassword = document.getElementById("btn_eye");
const imgPassword = document.getElementById("img_password");

// Confirmação de senha
const inputPasswordConfirmation = document.getElementById("Confirmation_password");
const btnPasswordConfirmation = document.getElementById("btn_eyeConfirmation");
const imgPasswordConfirmation = document.getElementById("img_passwordConfirmation");

btnPassword.addEventListener("click", function() {
    if (inputPassword.type == "password") {
        inputPassword.type = "text"
        imgPassword.src = "/static/icons/eye-slash-solid-full.svg"
    } else {
        inputPassword.type = "password"
        imgPassword.src = "/static/icons/eye-solid-full.svg"
    }
})

btnPasswordConfirmation.addEventListener("click", function() {
    if (inputPasswordConfirmation.type == "password") {
        inputPasswordConfirmation.type = "text"
        imgPasswordConfirmation.src = "/static/icons/eye-slash-solid-full.svg"
    } else {
        inputPasswordConfirmation.type = "password"
        imgPasswordConfirmation.src = "/static/icons/eye-solid-full.svg"
    }
})