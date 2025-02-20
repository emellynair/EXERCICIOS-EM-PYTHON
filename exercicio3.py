print('Bem-vindo a Copiadora da Emelly Nair')

# Função para escolher o serviço
def escolha_servico():
    while True:
        print('Digite o serviço desejado:')
        print('DIG - Digitalização')
        print('ICO - Impressão Colorida')
        print('IPB - Impressão Preto e Branco')
        print('FOT - Fotocópia')
        servico = input('>>')
        if servico == "dig":
            return 1.10
        elif servico == "ico":
            return 1.00
        elif servico == "ipb":
            return 0.40
        elif servico == "fot":
            return 0.20
        else:
            print('Escolha inválida, entre com o tipo de serviço novamente')

# Função para obter o número de páginas com desconto
def num_pagina():
    while True:
        try:
            num_paginas = int(input('Digite o número de páginas: '))
            if num_paginas < 20:
                return num_paginas * 0.0 #sem desconto
            elif num_paginas < 200:
                return num_paginas * 0.85 #15% de desconto
            elif num_paginas < 2000:
                return num_paginas * 0.80 #20% de desconto
            elif num_paginas < 20000:
                return num_paginas * 0.75 #25% de desconto
            else:
                print('Não aceitamos tantas páginas de uma vez')
                print('Por favor, entre com o número de páginas novamente.')
        except ValueError:
            print('Valor inválido. Digite um número inteiro.')

# Função para escolher o serviço extra
def servico_extra():
    while True:
        try:
            print('Deseja adicionar algum serviço extra?')
            print('1 - Encadernação Simples - R$ 15.00')
            print('2 - Encadernação Capa Dura - R$ 40.00')
            print('0 - Não desejo mais nada')
            extra = int(input(">>"))
            if extra == 1:
                return 15.00
            elif extra == 2:
                return 40.00
            elif extra == 0:
                return 0.00
            else:
                print('Opção inválida.')
        except ValueError:
            print('Valor inválido. Digite um número inteiro.')

if __name__ == "__main__":
    servico = escolha_servico()  
    num_paginas = num_pagina()  
    extra = servico_extra()  

    total = (servico * num_paginas) + extra

    print(f'Total: R$ {total:.2f} (serviço: {servico} * páginas: {num_paginas:.0f} + extra: {extra:.2f})')
