var txt = document.getElementsByClassName('resultado')[0]
txt.style.opacity = '0'


function registrou() {
    var usuarioreg = document.getElementById('usuario-reg').value
    var senhareg = document.getElementById('senha-reg').value
    localStorage = usuarioreg
    localStorage = senhareg
    if (usuarioreg.length == 0 || senhareg.length == 0) {
        window.alert('Preencha todos os dados corretamente!')
    } else {
        txt.style.opacity = '100'
        txt.style.color = '#FFD700'
    }
}


function logar() {
    var usuario = document.getElementById('usuario').value
    var senha = document.getElementById('senha').value

    if (usuario.length == 0 || senha.length == 0){
        window.alert('Preencha todos os dados corretamente!')
    } else if (usuario == localStorage.usuarioreg && senha == localStorage.senhareg) {
        txt.style.opacity = '100'
        txt.style.color = '#FFD700'
    } else if (usuario == "Owner" && senha == "owner") {
        txt.style.opacity = '100'
        txt.style.color = '#FFD700'
        txt.innerHTML = `&check; Seja bem bindo Chefinho!`
    }
}