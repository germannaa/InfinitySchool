function Quest01(){
    alert(`Questão 01`)

}

function Quest02(){
    alert(`Questão 02`)

    let num1 = Number(prompt("Digite o primeiro numero"));
    let num2 = Number(prompt("Digite o segundoo numero"));

    if (num1 == num2){
        alert(`Os valores digitados são iguais`)
    } 
    if (num1 > num2){
        alert(`O primeiro numero digitado é maior que o segundo`)
    }
    else {
            alert(`O segundo numero digitado é maior que o primeiro`)
        }
    }


function Quest03() {
    alert(`Questão 03`)

    let num = Number(prompt("Digite um numero"));

    if (num % 2 == 0){
        alert(`O numero digitado é par.`)
    } else {
        alert(`O numero digitado é impar.`)

    }
}

function Quest04() {
    alert(`Questão 04`)

    let salario = Number(prompt("Digite seu salario"));

    novoSalario = salario * 1.15;
    alert(`Parabéns! Seu novo salário é de ${novoSalario.toFixed(2)}.`)
}

function Quest05(){
    alert(`Questão 05`)

    for (i=1; i<=100; i++){
        console.log(i)
    }
}



function Exercicios() {
    let exercicios = Number(prompt("Escolha a questão: (De 1 a 5)"));

    if(exercicios == 1){
        Quest01()
    } else if(exercicios == 2){
        Quest02()
    } else if(exercicios == 3){
        Quest03()
    } else if(exercicios == 4){
        Quest04()
    } else if(exercicios == 5){
        Quest05()
    } else {
        alert(`Questão invalida.`)
        Exercicios()

    }
}

//Exercicios()

//__________________________________________________________________________________________

//Atividade 02



function Quest06(nome){
    console.log("Olá, ", nome)
}

function Quest07(lado){
    area = lado*lado;
    //alert(`A area do quadrado com lado de ${lado} é de ${area}.`)
    console.log("A  area do quadrado com lado de ", lado, "é de ", area, "m2.")
}

//Quest07(10)


function Quest08(base, altura){
    areaT = (base*altura)/2
    console.log("A area do triangulo com base de ", base, " e altura de ", altura, " é de ", areaT, " m2.")
}

//Quest08(10, 2)

function Quest09(numero){
    for (i=0; i<= numero; i++){
        console.log(i)
    }
}
//Quest09(10)

function Quest10(numero){
    for (i=0; i<= numero; i++){
        if (i%2 == 0 )
        console.log(i)
    }
}
//Quest10(10)


/*
let nome1 = prompt("Digite seu nome");
Quest06(nome1)

let numero = prompt("Digite um numero");

Quest07(numero)
Quest08(numero, numero)
Quest09(numero)
Quest10(numero)

*/


function Quest11(nota1, nota2){
    media = (nota1+nota2)/2

    if (media>=6){
        return "Aprovado"
    } else {
        return "Reprovado"
    }
}

//console.log(Quest11(5,5))

function Quest12(num1,num2,num3){
    if (num1>=num2 && num1>=num3){
        return (num1)
    } else if (num2>=num3){
        return (num2)
    } else {
        return (num3)
    }
    }
console.log(Quest12(1,2,10))

function Quest13(idade,cnh){
    if(idade<18 || cnh==false){
        return ("Vc nao pode dirigir")
    } else {
        return("Vc pode dirigir")
    }
}

//console.log(Quest13(8, true))