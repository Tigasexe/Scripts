function sim(){
    window.alert("Você aceitou namorar comigo!!!")
    //Redirecionar para uma musica
    window.open("https://youtube.com/watch?v=4iKtTmnHojU", "_blank")
}

function desvia(t) {
    var btn = t
    btn.style.position = "absolute"
    btn.style.bottom = geraPosicao(40, 60)
    btn.style.left = geraPosicao(40, 60)
    console.log("Desviei haha")
}

function geraPosicao(min, max) {
    return (Math.random() * (max - min) + min) + "%"
}