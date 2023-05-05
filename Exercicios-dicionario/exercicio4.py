#4. Como você pode verificar se a chave 'pêssego' está presente no dicionário frutas? Escreva o código que retorna um valor booleano (True ou False) dependendo da existência da chave.

#UMA DAS MANEIRAS DE RESOLVER:
#frutas = {'maça': 5, 'banana': 8, 'laranja': 12}
#if 'pêssego' in frutas:
#    print("A chave 'pêssego' está presente no dicionário frutas!")
#else:
#    print("A chave 'pêssego' não está presente no dicionário frutas.")

#OUTRA MANEIRA
frutas = {'maça': 5, 'banana': 8, 'laranja': 12}

tem_pessego = 'pêssego' in frutas
if tem_pessego == False:
    print("A chave pessego nao esta presente em frutas")
    
else: print("A chave pessego está presente em frutas")



