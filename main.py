import os
lista = []
while True:
    print("PROGRAMA DE CADASTRO DE NOMES")
    print("CADASTRAR - digite 1")
    print("LISTAR - digite 2")
    print("PESQUISAR - digite 3")
    print("ORDENAR - digite 4")
    print("ATUALIZAR - digite 5")
    print("DELETAR- digite 6")
    print("FECHAR O PROGRAMA - digite 0")
    opcao = int(input("Qual operação deseja realizar?"))
    os.system("cls")

    match opcao:
        case 1:
            os.system("cls")
            print("Cadastrando nome")
            novo = str(input("Insira o nome\n"))
            lista.append(novo)
            print(f"nome: {novo} inserido na lista")
            print(f"Lista:", end=' ')
            for nome in lista:
                print(f"{nome}", end=", ")
            print("\n")
        case 2:
            os.system("cls")
            print("listando nomes")
            for v, nome in enumerate(lista):
                print(f"{v + 1}-{nome} ")

        case 3:
            os.system("cls")

            print("Pesquisando nome")
            pesquisa = str(input("Insira o nome\n"))
            if pesquisa in lista:
                print(f"o nome {pesquisa} está na lista")
            else:
                print(f"o nome {pesquisa} NÃO está na lista")
        case  4:
            os.system("cls")
            lista.sort()
            print("Lista Ordenada:")
            for nome in lista:
                print(f"{nome}", end=", ")
            print("\n")
        case  5:
            os.system("cls")
            while True:
                print("Atualizando nome")
                atualizar = str(input("Qual nome deseja atualizar?\n"))
                if atualizar in lista:
                    lista.remove(atualizar)
                    break
                else:
                    os.system("cls")
                    print("Nome inexistente na lista, escolha outro")
                    continue

            while True:
                novo_nome = str(input(f"insira novo nome para {atualizar}\n"))
                if novo_nome not in lista:
                    lista.append(novo_nome)
                    print(lista)
                    break
                else:
                    print("o nome já está na lista")
                    continue

        case 6:
            os.system("cls")
            while True:
                deletar = str(input("Qual nome deseja deletar?\n"))
                if deletar in lista:
                    lista.remove(deletar)
                    print(f"{deletar} removido da lista")
                    print("Nova lista")
                    print(lista)
                    break
                else:
                    print(
                        f"O nome: {deletar} NÃO está na lista\n")
                    continue

        case 0:
            os.system("cls")
            print("Encerrando o programa")
            break
        case _:
            os.system("cls")
            print("valor invalido, digite outro valor")
