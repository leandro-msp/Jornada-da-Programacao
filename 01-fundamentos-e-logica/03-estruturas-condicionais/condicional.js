let produto1 = 300;
let produto2 = 200;


//simples
if (produto1>produto2){
    console.log("O produto 2 é mais barato");
}else{
    console.log("O produto 1 é mais barato");
}

//composta

let produto3 = 100
if (produto1<produto2 && produto1<produto3){
    console.log("O Produto 1 é mais barato");
}else if(produto2<produto1 && produto2<produto3){
    console.log("O Produto 2 é mais barato");
}else{
    console.log("O Produto 3 é mais barato");
}

//ternário

let carga = 47

let notificacao = (carga<20) ? "Bateria baixa. Coloque o dispositvo para carregar!" : "Ainda resta "+carga+"% de bateria";
    console.log(notificacao)