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

sexo = input("Digite o sexo (F/M): ")
if sexo == "M":
    print("O sexo é Masculino!")
elif sexo == "F":
    print("O sexo é Feminino!")
else:
    print("Sexo inválido")


#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Entre com uma letra qualquer do alfabeto: ")
vogais = ['a','e','i','o','u']
if letra in vogais:
    print("É uma vogal")
else:
    print("É uma consoante")

#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Entre com a nota 1: "))
nota2 = float(input("Entre com a nota 2: ")) 
media = (nota1 + nota2)/2
if media == 10:
    print("Aprovado com Distinção, sua média é:", media)
elif media >= 7:
    print("Aprovado, sua média é:", media)
elif media < 7:
    print("Reprovado, sua média é:", media)
else:
    print("Notas inválidas")