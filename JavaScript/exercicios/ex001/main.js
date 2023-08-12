function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var body = window.document.body
    var data = new Date()
    var hora = data.getHours()
    var min = data.getMinutes()
    msg.innerHTML = `Agora são ${hora}:${min} horas.`

    if (hora >= 5 && hora < 12) {
        //BOM DIA!
        img.src = "fotos/fotomanha.jpg"
        body.style.backgroundColor = 'rgb(255, 188, 81)'
    } else if (hora >= 12 && hora < 18) {
        //BOA TARDE!
        img.src = "fotos/fototarde.jpg"
        body.style.backgroundColor = 'rgb(255, 121, 53)'
    } else if (hora >= 18 && hora < 23) {
        //BOA NOITE
        img.src = "fotos/fotonoite.jpg"
        body.style.backgroundColor = 'rgb(8, 0, 65)'
    } else {
        //HORA DO GAME
        img.src = 'fotos/fotomadrugada.jpg'
        body.style.backgroundColor = 'black'
    }
}
