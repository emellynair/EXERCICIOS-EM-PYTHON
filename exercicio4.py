
print('Bem-vindo a Livraria da Emelly Nair')

lista_livro = []
id_global = 0

# Função para cadastro
def cadastrar_livro(id):
    print('--------------------------------------------------')
    print('------------- MENU CADASTRAR LIVRO ---------------')
    print(f'Id do livro: {id}') # Exibe o ID do livro
    nome = input('Digite o nome do livro: ')
    autor = input('Digite o nome do autor: ')
    editora = input('Digite o nome da editora do livro: ')

    livro = { # Dicionário com os dados do livro
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    lista_livro.append(livro) # Adiciona o dicionário à lista de livros
    print('Livro cadastrado com sucesso!')

# Função para consultar livro
def consultar_livro():
    while True:
        print('------------------------------------------------')
        print('------------- MENU CONSULTAR LIVRO -------------')
        print('Escolha a opção desejada: ')
        print('1 - Consultar Todos')
        print('2 - Consultar por ID')
        print('3 - Consultar por Autor')
        print('4 - Retornar ao menu')

        opcao = input('>>')

        if opcao == "1":
            if not lista_livro:
                print("Não há livros cadastrados.")
            else:
                for livro in lista_livro:
                    for chave, valor in livro.items():  # Itera sobre os itens do dicionário
                        print(f"{chave}: {valor}")  # Imprime cada chave e valor formatados
                    print("-" * 20)  # Linha separadora entre os livros
        elif opcao == "2":
            try:
                id = int(input("Digite o ID do livro: "))
                for livro in lista_livro:
                    if livro["id"] == id:
                        for chave, valor in livro.items():  
                            print(f"{chave}: {valor}")  
                        break
                else:
                    print("Livro não encontrado.")
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        elif opcao == "3":
            autor = input("Digite o nome do autor: ")
            livros_encontrados = []
            for livro in lista_livro:
                if livro["autor"] == autor:
                    livros_encontrados.append(livro)
            if not livros_encontrados:
                print("Nenhum livro encontrado para este autor.")
            else:
                for livro in livros_encontrados:
                    for chave, valor in livro.items():  
                        print(f"{chave}: {valor}")  
                    print("-" * 20) 
        elif opcao == "4":
            return  # Retorna ao menu principal
        else:
            print("Opção inválida.")

# Função para remover livro
def remover_livro():
    while True:
        print('--------------------------------------------------')
        print('--------------- MENU REMOVER LIVRO ---------------')
        try:
            id = int(input("Digite o ID do livro a ser removido: "))
            for livro in lista_livro:
                if livro["id"] == id:
                    livro_removido = lista_livro.pop(lista_livro.index(livro))  # Remove o livro e armazena os dados
                    print("Livro removido com sucesso!")
                    for chave, valor in livro_removido.items():  # Imprime os dados do livro removido
                        print(f"{chave}: {valor}")
                    return
            else:
                print("ID inválido. Livro não encontrado.")
        except ValueError:
            print("ID inválido. Digite um número inteiro.")

if __name__ == "__main__":
    while True:
        print('--------------------------------------------------')
        print('----------------- MENU PRINCIPAL -----------------') 
        print('Escolha a opção desejada:')
        print('1 - Cadastrar Livro')
        print('2 - Consultar Livro(s)')  
        print('3 - Remover Livro')
        print('4 - Sair')  

        opcao = input(">>")  

        if opcao == "1":
            id_global += 1
            cadastrar_livro(id_global)
        elif opcao == "2":
            consultar_livro()
        elif opcao == "3":
            remover_livro()
        elif opcao == "4":
            print('Saindo do programa...') 
            break
        else:
            print('Opção inválida.')

