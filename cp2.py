#1 Crie uma lista alphabet contendo todas as letras do alfabeto em inglês em ordem alfabética.
from random import sample

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(alphabet)

#Crie uma lista rotor que represente um rotor simples. Para isso, embaralhe as letras do alfabeto de alguma forma.

rotor = sample(alphabet, 26)
print(rotor)

#Crie uma lista reflector que represente um refletor simples. Para isso, embaralhe novamente as letras do alfabeto de outra maneira. 

reflector = sample(rotor, 26)
print(reflector)

#Dado um message (mensagem), você deve cifrar a mensagem da seguinte maneira: 
#Para cada letra da mensagem, encontre sua posição no alphabet. 

message = "doideira"
mensagemCifrada = ""
mensagemDecifrada = ''

for letra in message: 
    posicao = alphabet.index(letra)
    posicao += 1
    rotorLetra = rotor[posicao]
    reflectorPosicao = reflector.index(rotorLetra)
    letrasCifradas = alphabet[reflectorPosicao]
    mensagemCifrada += letrasCifradas
print("A mensagem cifrada é: ", mensagemCifrada)

for letra in mensagemCifrada:
    reflectorPosicao = alphabet.index(letra)
    refletidaLetra = reflector[reflectorPosicao]
    rotorPosicao = rotor.index(refletidaLetra)
    rotorPosicao -= 1
    letrasCifradas = alphabet[rotorPosicao]
    mensagemDecifrada += letrasCifradas

print("A mensagem decifrada é: ", mensagemDecifrada)

