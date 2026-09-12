valor = float(input("Bem vindo! Digite o valor da compra: "))                                       # entrada de dados
porcentagem = 0 
desconto = 0
valor_descontado = 0
if valor >= 300:                                                                                    # processamento de dados 
    porcentagem = 15
    valor_descontado = valor * 0.15
    desconto = valor - valor_descontado
else:
    if valor >= 200:
        porcentagem = 10
        valor_descontado = valor * 0.10
        desconto = valor - valor_descontado
    else:
        if valor < 200:
            porcentagem = 5
            valor_descontado = valor * 0.05
            desconto = valor - valor_descontado                                      
print(f"Você recebeu {porcentagem}% de desconto, o valor a ser pago será de R$ {desconto:.2f}")      # saída de dados
print(f"O desconto foi de R$ {valor_descontado:.2f}")
print(f"Obrigado por nos visitar, até a próxima!")            

        
