print('Bem-vindo à Loja de Açaí e Cupuaçu da Emelly Nair')

# Exibição do cardápio
print('-----------------Cardápio------------------')
print('-------------------------------------------')
print('---| Tamanho | Cupuaçu (CP)| Açaí (AC) |---')
print('---|    P    |   R$ 9.00   |  R$11.00  |---')
print('---|    M    |   R$14.00   |  R$16.00  |---')
print('---|    G    |   R$18.00   |  R$20.00  |---')
print('-------------------------------------------')

# Tabela de preços
tabela_precos = {
    "CP": {"P": 9, "M": 14, "G": 18},
    "AC": {"P": 11, "M": 16, "G": 20}
}

# Inicializa o acumulador do total de compras
total_pedido = 0

while True:
    # Loop para validar a escolha do sabor
    while True:
        sabor = input('Escolha seu produto (CP) para Cupuaçu ou (AC) para Açaí): ').strip().upper() #Aqui vai ser executado independente se for maiscula ou minuscula
        if sabor in tabela_precos:
            break
        else:
            print("Sabor inválido. Tente novamente.")
            continue
    
    # Loop para validar a escolha do tamanho
    while True:
        tamanho = input('Escolha o tamanho (P / M / G): ').strip().upper()
        if tamanho in tabela_precos[sabor]:
            preco = tabela_precos[sabor][tamanho]
            break
        else:
            print("Tamanho inválido. Tente novamente.")
            continue
    
    # Exibe o pedido e soma ao total
    sabor_nome = "Cupuaçu" if sabor == "CP" else "Açaí"
    print(f"Você pediu um {sabor_nome} no tamanho {tamanho}: R$ {preco:.2f}")
    total_pedido += preco
    
    # Perguntar se deseja fazer mais algum pedido
    while True:
        continuar = input("Deseja pedir mais alguma coisa? (S/N): ").strip().upper()
        if continuar == "S":
            break
        elif continuar == "N":
            print(f"O valor total a ser pago: R$ {total_pedido:.2f}")
            exit()
        else:
            print("Dígito inválido! Digite apenas 'S' para sim ou 'N' para não.")
            continue