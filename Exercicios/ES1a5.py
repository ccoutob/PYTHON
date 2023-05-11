#ESTRUTURA SEQUENCIAL

#Faça um Programa que mostre a mensagem "Alo mundo" na tela
print("Alo mundo")

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numeroQualquer = input("Entre com um número qualquer: ")
print(numeroQualquer)

#Faça um Programa que peça dois números e imprima a soma.
numero1 = float(input("Entre com um número qualquer para somar: "))
numero2 = float(input("Entre com outro número qualquer para somar: "))
print(numero1 + numero2)

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Entre com a primeira nota: "))
nota2 = float(input("Entre com a segunda nota: "))
nota3 = float(input("Entre com a terceira nota: "))
nota4 = float(input("Entre com a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print(media)

#Faça um Programa que converta metros para centímetros.
ninha = float(input("Qual a altura da ninha EM CENTIMETROS? "))
convertendo = ninha/100
print("ninha tem",convertendo, "metros")