Algoritmo "semnome"

Var
peso : real
altura: real
imc: real

Inicio

escreval ("----Calculo IMC----")
escreval ("Digite seu peso:")
leia (peso)
escreval ("Digite sua altura:")
leia (altura)
imc := peso/(altura^2)
escreval ("Seu imc é de:", imc)


Fimalgoritmo


_________________________________________________________________________


Algoritmo "semnome"

Var
TC : real
TF : real


Inicio

escreval ("----Transformando Farenheit em Celsius----")
escreval ("Escreva a temperatura emFarenheit:")
leia (TF)
TC := ((TF - 32) * 5) / 9
escreval ("A temperatura em celsius é de:", TC)


Fimalgoritmo


__________________________________________________________________

Algoritmo "semnome"

Var
altura: real
largura: real


Inicio

escreval ("----Area Retangulo----")
Escreval ("Digite a altura do retangulo:")
leia (altura)
Escreval ("Digite a largura do retangulo:")
leia (largura)
escreval("A area do retangulo é de:", (largura*altura))


Fimalgoritmo


________________________________________________________________________

Algoritmo "semnome"

Var
indice: inteiro


Inicio

para indice de 1 ate 50 faca
  escreval ("Seu numero é:", indice)
  
fimpara

Fimalgoritmo


__________________________________________________________________________

Algoritmo "semnome"

Var
nota1, nota2, nota3, media: real

Inicio
escreval ("-------BOLETIM-------")
escreva ("Digite a nota 1:")
leia (nota1)
escreva ("Digite a nota 2:")
leia (nota2)
escreva ("Digite a nota 3:")
leia (nota3)

media:= (nota1 + nota2 + nota3)/3

escreval ("---------------------")

se media >= 7 entao
 escreval ("APROVADOOOO!")
 senao
      escreval("Reprovado....")
fimse

Fimalgoritmo


_______________________________________________________________________________

Algoritmo "semnome"

Var
idade: inteiro
sexo: caractere

Inicio


escreval ("---------Seleção de Clubes------------")
escreval ("Digite sua idade:")
leia (idade)
escreval ("Digite seu sexo: (M/F)")
leia (sexo)

escreval ("---------------------")

se (idade>=18) E (sexo = "F") entao
 escreval ("Seja bem vinda ao clube Afrodite")
fimse

se (idade >= 18) E (sexo = "M") entao
  escreval("Seja bem vindo ao clube de Cavalheiros")

senao
escreval ("Vá pra casa!")

FIMSE

Fimalgoritmo


________________________________________________________________________________________

Algoritmo "semnome"

Var
idade: inteiro
sexo: caractere

Inicio


escreval ("---------Seleção de Clubes------------")
escreval ("Digite sua idade:")
leia (idade)
escreval ("Digite seu sexo: (M/F)")
leia (sexo)

escreval ("---------------------")

se (idade>=18) E (sexo = "F") entao
 escreval ("Seja bem vinda ao clube Afrodite")
 
 senao
      se (idade >= 18) E (sexo = "M") entao
       escreval("Seja bem vindo ao clube de Cavalheiros")

           senao
           escreval ("Vá pra casa!")
           
      fimse
fimse


Fimalgoritmo


_________________________________________________________________________________

Algoritmo "semnome"

Var
idade: inteiro
sexo: caractere

Inicio


escreval ("---------Seleção de Clubes------------")
escreval ("Digite sua idade:")
leia (idade)
se (idade< 18) entao
   escreval ("---------------------")
   escreval ("Vá pra casa!")
   
 senao
   escreval ("Digite seu sexo: (M/F)")
   leia (sexo)

escreval ("---------------------")

     se (idade>=18) E (sexo = "F") entao
      escreval ("Seja bem vinda ao clube Afrodite")
 
      senao
       se (idade >= 18) E (sexo = "M") entao
        escreval("Seja bem vindo ao clube de Cavalheiros")


       fimse
    fimse
fimse


Fimalgoritmo



____________________________________________________________________________________

Algoritmo "semnome"

Var
numero: inteiro

Inicio

escreval ("Digite um numero:")
leia(numero)

se (numero MOD 2 = 0) entao
 escreval ("O numero é par.")
 
 senao
  escreval ("O numero é impar!")
  
fimse

Fimalgoritmo



__________________________________________________________________





