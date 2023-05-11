#ESTRUTURA DE DECISAO

#Faça um Programa que peça dois números e imprima o maior deles.
numero1 = float(input("Entre com o primeiro número: "))
numero2 = float(input("Entre com o segundo número: "))
if numero1 > numero2:
    print(numero1,"é o maior número")
elif numero2 > numero1:
    print(numero2,"é o maior número")
else:
    print("Os números são iguais")

#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
valor = float(input("Entre com um número positivo ou negativo: "))
if valor > 0:
    print("O número é positivo")
elif valor < 0:
    print("O número é negativo")
else:
    print("O número é zero")

#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.