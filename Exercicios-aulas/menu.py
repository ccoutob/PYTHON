from inventario import adicionar, relatorio, buscar, buscar_simples, alterar, remover, remover_por_index
produtos = {1:["Banana",20,3,12345,1.0,"18/03/2023","",1,"Copa","São Paulo"], 3:["Notebook",2,-1,54321,3500.0,"01/01/2023","",3000,"RH","São Paulo"]}
while True:
    print("Bem Vindo!\n")
    
    print("Digite 1 para Adicionar;")
    print("Digite 2 para Relatorio;")
    print("Digite 3 para Busca Simples;")
    print("Digite 4 para Busca por Nome;")
    print("Digite 5 para Alterar Quantidade;")
    print("Digite 6 para Remover por ID;")
    print("Digite 7 para Remover por Nome;")
    print("Digite 8 para Sair;")
    opcao = int(input("Entre com a opção desejada: "))
    
    if opcao == 1:
        adicionar(produtos)
    elif opcao == 2:
        relatorio(produtos)
    elif opcao == 3:
        buscar_simples(produtos)
    elif opcao == 4:
        buscar(produtos)
    elif opcao == 5:
        alterar(produtos)
    elif opcao == 6:
        remover_por_index(produtos)
    elif opcao == 7:
        remover(produtos)
    elif opcao == 8:
        quit()