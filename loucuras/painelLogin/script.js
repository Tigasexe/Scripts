let txt = document.getElementsByClassName('resultado')[0]
txt.style.opacity = '0'


function registrou() {
    let usuarioreg = document.getElementById('usuario-reg').value
    let senhareg = document.getElementById('senha-reg').value
    localStorage.user = usuarioreg
    localStorage.pass = senhareg


    if (usuarioreg.length == 0 || senhareg.length == 0) {
        txt.style.opacity = '100'
        txt.style.color = 'red'
        txt.style.fontSize = '14pt'
        txt.innerHTML = 'Preencha todos os dados corretamente!'
    } else if (usuarioreg.length <= 5){
        txt.style.opacity = '100'
        txt.style.color = 'red'
        txt.style.fontSize = '14pt'
        txt.innerHTML = `O usuario ${usuarioreg} não possui 5 ou mais caracteres!`
    } else {
        window.location.href = '../index.html'
    }
}

function logar() {
    let usuario = document.getElementById('usuario').value
    let senha = document.getElementById('senha').value


    if (usuario != localStorage.user || senha != localStorage.pass) {
        txt.style.opacity = '100'
        txt.style.color = 'red'
        txt.style.fontSize = '14pt'
        txt.innerHTML = 'Usuario ou senha incorretos!'
    } else {
        txt.style.opacity = '100'
        txt.style.color = 'green'
        txt.style.fontSize = '14pt'
        location.href = 'python/script.py'
    }
}

function olhoureg() {
    let senha = document.getElementById('senha-reg')
    let olho = document.getElementById('olho')

    if (senha.type == 'password') {
        senha.setAttribute('type', 'text')
        olho.setAttribute('class', 'bi bi-eye-slash-fill')
    } else {
        senha.setAttribute('type', 'password')
        olho.setAttribute('class', 'bi bi-eye-fill')
    }
}

function olhou() {
    let senha = document.getElementById('senha')
    let olho = document.getElementById('olho')

    if (senha.type == 'password') {
        senha.setAttribute('type', 'text')
        olho.setAttribute('class', 'bi bi-eye-slash-fill')
    } else {
        senha.setAttribute('type', 'password')
        olho.setAttribute('class', 'bi bi-eye-fill')
    }
}