#5. Qual é o comando para remover um item do dicionário frutas que possui a chave 'laranja'?

frutas = {'maça': 5, 'banana': 8, 'laranja': 12}

def remover():
    chave = 'laranja'
    if chave in frutas:
        frutas.pop(chave)
        print(f"A chave '{chave}' foi removida do dicionário.")
    else:
        print(f"A chave '{chave}' não existe no dicionário.")

remover()

