# 1) Escreva um programa que peça à pessoa usuária para fornecer dois números e exibir o número maior.

num = float(input('Digite aqui um número: '))
num2 = float(input('Digite aqui outro número: '))

if num > num2:
    print(f'{num} é o maior número.')
else:
    print(f'{num2} é o maior número.')

# 2) Escreva um programa que solicite o percentual de crescimento de produção de uma empresa e informe se houve um crescimento (porcentagem positiva) ou decrescimento (porcentagem negativa).

percentual_salario = float(input('Informe aqui o percentual de produção que sua empresa teve: '))

if percentual_salario > 0:
    print(f'Houve um crescimento de {percentual_salario}%!')
elif percentual_salario < 0:
    print(f'Houve um decrescimento de {percentual_salario}%!')
else:
    print(f'Seu crescimento {percentual_salario}% foi nulo!')


# 3) Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

letra = str(input('Informe uma letra aqui!: ')).lower()

if letra in 'aeiou':
    print('Sua letra é uma vogal.')
else:
    print('Sua letra uma consoante.')

# 4) Escreva um programa que leia valores médios de preços de um modelo de carro por 3 anos consecutivos e exiba o valor mais alto e mais baixo entre esses três anos.

valor_carro1 = float(input('Informe a média de preço de um carro no seu primeiro ano: '))
valor_carro2 = float(input('Informe a média de preço de um carro no seu segundo ano: '))
valor_carro3 = float(input('Informe a média de preço de um carro no seu terceiro ano: '))

maior_valor = max(valor_carro1, valor_carro2, valor_carro3)
menor_valor = min(valor_carro1, valor_carro2, valor_carro3)

print(f'O maior valor deste carro foi de {maior_valor}!')
print(f'O menor valor deste carro foi de {menor_valor}!')



# 5) Escreva um programa que pergunte sobre o preço de três produtos e indique qual é o produto mais barato para comprar.

produto1 = float(input('Insira o valor do primeiro produto aqui: '))
produto2 = float(input('Insira o valor do segundo produto aqui: '))
produto3 = float(input('Insira o valor do terceiro produto aqui: '))

menor_produto = min(produto1, produto2, produto3)

if menor_produto == produto1:
    print(f'O produto mais barato para se comprar é o Produto 1 que custa {menor_produto}.')
elif menor_produto == produto2:
    print(f'O produto mais barato para se comprar é o Produto 2 que custa {menor_produto}.')
else:
    print(f'O produto mais barato para se comprar é o Produto 3 que custa {menor_produto}.')


# 6) Escreva um programa que leia três números e os exiba em ordem decrescente.

numero1 = float(input('Informe um valor númerico aqui: '))
numero2 = float(input('Informe um valor  outro númerico aqui: '))
numero3 = float(input('Informe um valor  outro númerico aqui: '))

numeros = [numero1, numero2, numero3]
numeros.sort(reverse=True)

print(f'Números em ordem decrescente: {numeros}') 


# 7) Escreva um programa que pergunte em qual turno a pessoa usuária estuda ("manhã", "tarde" ou "noite") e exiba a mensagem "Bom Dia!", "Boa Tarde!", "Boa Noite!", ou "Valor Inválido!", conforme o caso.

turno = str(input('Em que turno você estuda (manha, tarde ou noite)?: ')).lower() # lower para transformar todas as letras que o usuario escrever em minusculas, para ficar mais compreensivel.

if turno == 'manha':
    print('Bom dia!')
elif turno == 'tarde':
    print('Boa tarde!')
elif turno == 'noite':
    print('Boa noite!')
else:
    print('Valor inválido!') # se o usuario não digitar corretamente os horarios de turno, retornará um valor inválido ao usuario. 


# 8) Escreva um programa que peça um número inteiro à pessoa usuária e determine se ele é par ou ímpar. Dica: Você pode utilizar o operador módulo %.

number = float(input('Digite um número aqui e confira se ele é ímpar ou par '))

if number % 2 == 0:
    print('Seu número é par.')
else:
    print('Seu número é ímpar.')



# 9) Escreva um programa que peça um número à pessoa usuária e informe se ele é inteiro ou decimal.

# Momento dos projetos
# 10) Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

# 11) Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.
# 12) Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R$ 2,00 e o preço do litro de etanol é R$ 1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente. Tenha em mente algumas dicas:

# O do valor do desconto será a multiplicação entre preço do litro, quantidade de litros e o valor do desconto.
# O valor a ser pago por um cliente será o resultado da multiplicação do preço do litro pela quantidade de litros menos o valor de desconto resultante do cálculo.
# 13) Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:

# Para variação acima de 20%: bonificação para o time de vendas.
# Para variação entre 2% e 20%: pequena bonificação para time de vendas.
# Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas.
# Para variação abaixo de -10%: corte de gastos.