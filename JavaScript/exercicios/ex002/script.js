function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')

    if (fano.value.length == 0 || fano.value > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        
        res.style.textAlign = 'center'

        if (fsex[0].checked) {
            genero = 'Homem'
            res.innerHTML = `Detectamos um ${genero} com ${idade} anos.`
            res.appendChild(img)
            if (idade >= 0 && idade < 10){
                //CRIANÇA
                img.setAttribute('src','fotos/bebem.jpg')
            } else if (idade < 21){
                //JOVEM
                img.setAttribute('src', 'fotos/jovemm.jpg')
            } else if (idade < 50) {
                //ADULTO
                img.setAttribute('src','fotos/adultom.avif')
            } else {
                //IDOSO
                img.setAttribute('src', 'https://i0.wp.com/www.kdcare.com.br/wp-content/uploads/2019/01/Acessibilidade-para-idosos-5-dicas-para-deixar-sua-casa-mais-segura.jpg?fit=2500%2C1667&ssl=1')

            }

            
        } else if (fsex[1].checked){ 
            genero = 'Mulher'
            res.innerHTML = `Detectamos uma ${genero} com ${idade} anos.`
            res.appendChild(img)
            if (idade >= 0 && idade < 10){
                //CRIANÇA
                img.setAttribute('src','fotos/bebef.jpeg')
            } else if (idade < 21){
                //JOVEM
                img.setAttribute('src','fotos/jovemf.jpg')
            } else if (idade < 50) {
                //ADULTO
                img.setAttribute('src', 'https://www.psitto.com.br/wp-content/uploads/2022/12/autismo-adulto.jpg')
            } else {
                //IDOSO
                img.setAttribute('src', 'https://metodosupera.com.br/wp-content/uploads/2021/09/No-Dia-do-Idoso-5-dicas-para-abandonar-o-preconceito-a-pessoas-com-mais-de-60-anos_SUPERA-Ginastica-para-o-cerebro_.jpg')
            }
        }
        
    }
}