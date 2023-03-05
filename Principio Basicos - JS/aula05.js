
function arrayInformacoes(nome, idade, curso){
let aluno = [nome, idade, curso];
console.log("Informações da função: ", aluno)
};
//arrayInformacoes("Germanna", 12, "ADS")


//---------------------------------------------------

let aluno2 = ["Germanna", 12, "ADS"];
//console.log("Informacoes: ", aluno2)
aluno2[2] = "FullStack"
//console.log("Informacoes atualizadas: ", aluno2)

//---------------------------------------------------

function arrayNotas(n1, n2, n3){
    let notas = [n1, n2, n3];
    console.log("Notas: ", notas);

    media = (notas[0] + notas[1] + notas[2])/3;
    console.log("Média: ", media.toFixed(2));

    notas[1] = notas[1]/2;
    media2 =(notas[0] + notas[1] + notas[2])/3;
    console.log("Média após atualizar a segunda nota: ", media2.toFixed(2));
};

//arrayNotas(10,10,10);

//---------------------------------------------------


let numeros = [10,20,30,40,50];

for (i = 0; i<numeros.length; i++){
   // console.log("Numero: ", numeros[i])
}

for (i in numeros){
   // console.log("Exemplo2: ", numeros[i])
}


//---------------------------------------------------


function pares(){
    let aleatorios = [10,15,17,22,9,4]
    let contador=0
    for (i in aleatorios){
        if ((aleatorios[i]%2) == 0) {
            contador++;
        }
    }
    console.log("Quantidade de numeros pares: ", contador)
}

// pares();


function notas(){
    notasAlunos = [5.5, 6, 4.3, 7 , 3.2, 8.2]
    for (i in notasAlunos){
        while (notasAlunos[i] < 6) {
            //Aumentar um ponto até a nota ser maior que 6
            notasAlunos[i] = notasAlunos[i]+1
           // console.log("Nota do aluno atualizada", notasAlunos[i])
            
        }
    }
    console.log("Nota dos alunos atualizada", notasAlunos)
}

 // notas();

 //---------------------------------------------------


 /*
 .shift => Remove o primeiro
 .unshift => Adiciona no começo do array
  .pop  => Remove o ultimo
 .push => Adiciona no final do array
*/

function parImpar(){
     let numeros = [1,2,3,4,5,6,7,8,9,10]
    let numerosPares = []
    let numerosImpares = []

     for (i in numeros){
        if ((numeros[i]%2) == 0){
            numerosPares.push(numeros[i])
        } else {
            numerosImpares.push(numeros[i])
        }
     }
     console.log("Numeros pares: ", numerosPares)
     console.log("Numeros impares: ", numerosPares)
}

// parImpar()

 //---------------------------------------------------


 

