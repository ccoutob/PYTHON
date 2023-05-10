#1 Crie uma lista alphabet contendo todas as letras do alfabeto em inglês em ordem alfabética.
from random import sample

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(alphabet)

#Crie uma lista rotor que represente um rotor simples. Para isso, embaralhe as letras do alfabeto de alguma forma.

rotor = sample(alphabet, 26)
print(rotor)

#Crie uma lista reflector que represente um refletor simples. Para isso, embaralhe novamente as letras do alfabeto de outra maneira. 

reflected = sample(rotor, 26)
print(reflected)

#Dado um message (mensagem), você deve cifrar a mensagem da seguinte maneira: 
#Para cada letra da mensagem, encontre sua posição no alphabet. 

message = "doideira"
cifra = []
cifra2 = []

for letra in message:
    if letra in alphabet:
        posicao = alphabet.index(letra)
        cifra.append(posicao)
print(cifra)

#Adicione 1 à posição encontrada (simulando uma rotação simples) e, em seguida, encontre a letra correspondente no rotor. 

for letra in message:
    if letra in rotor:
        posicao = alphabet.index(letra)
        cifra2.append(posicao + 1)
print(cifra2)


