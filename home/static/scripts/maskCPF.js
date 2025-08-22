function maskCPF(input) {
    let value = input.value.replace(/\D/g, "");
    if(value.length <= 3) {
        input.value = value
    } else if(value.length <=6) {
        input.value = value.replace(/(\d{3})(\d+)/, '$1.$2')
    } else if(value.length <=9) {
        input.value = value.replace(/(\d{3})(\d{3})(\d+)/, '$1.$2.$3')
    } else {
        input.value = value.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4')
    }
}