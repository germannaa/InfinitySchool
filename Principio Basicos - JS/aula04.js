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

Exercicios()