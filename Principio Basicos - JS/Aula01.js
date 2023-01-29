 /*alert ("Olá Mundo")

nome = prompt("Digite seu nome:")

alert ("Seja bem vindooo " + nome + "!!!")

dia = prompt("Digite o dia de nascimento: ")
mes = prompt("Digite o mes de nascimento: ")
ano = prompt("Digite o ano de nascimento: ")

alert ("Você nasceu em " + dia + "/" + mes + "/" + ano)



let num1 = Number(prompt("Digite um numero"))
let num2 = Number(prompt("Digite outro numero"))

media = (num1 + num2)/2

alert("A média entre " + num1 + " e " + num2 + " é " + media)



let num = Number(prompt("Digite um numero "))

for(let i = 0; i <= 10; i++) {
    let res = num * i
    alert(num +" * " +  i + " = " +res)
}



let kg = Number(prompt("Digite o peso em kg"))
pesoemG = kg * 1000

alert(`O peso ${kg}kg convertido dá ${pesoemG}g`)

*/

let valor = Number(prompt("Digite o valor a ser abastecido"))
litros = (valor /6.5).toFixed(2)
alert(`Com R$ ${valor}, vc vai abastecer  ${litros.toFixed(2)} litros`)
