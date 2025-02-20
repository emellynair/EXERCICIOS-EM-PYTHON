print('Bem-vindo à Loja de Atacado da Emelly Nair')
  
valor_unitario = float(input('Digite o valor unitário do produto: R$ '))  
quantidade = int(input('Digite a quantidade de produtos: '))

# Calcula o valor total sem desconto  
valor_total = valor_unitario * quantidade

# Determina o percentual de desconto com base no valor total da compra  
if valor_total < 2500:
    desconto = 0  
elif valor_total < 6000:
    desconto = 0.04  
elif valor_total < 10000:
    desconto = 0.07  
else:
    desconto = 0.11 

# Calcula o valor do desconto aplicado  
valor_desconto = valor_total * desconto

# Calcula o valor final a ser pago após o desconto  
valor_final = valor_total - valor_desconto

# Exibe os resultados para o usuário  
print(f'Valor total dos produtos sem desconto: R$ {valor_total:.2f}')
print(f'Desconto aplicado: {desconto * 100:.0f}%')  # Exibe o percentual de desconto em inteiro
print(f'Valor total com desconto: R$ {valor_final:.2f}')
