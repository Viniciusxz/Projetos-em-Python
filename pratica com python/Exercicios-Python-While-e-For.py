#1) Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.

num1 = int(input('Digite um número aqui! -> '))
num2 = int(input('Digite outro número aqui! -> '))

inicio = min(num1, num2)
fim = max(num1, num2)

for i in range(inicio + 1, fim): # Aqui, como o usuario não quer o primeiro numero repetido, adicionamos +1 para não aparecer o primeiro numero digitado, e no fim, nao precisa colocar mais uma soma, pois a função ja puxa o numero antes do original digitado.
    print(i) 

# 2) Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

coloniaA = 4
coloniaB = 10

taxaA = 0.03
taxaB = 0.015

dias = 0

while coloniaA < coloniaB:
    coloniaA = coloniaA + (coloniaA * taxaA)
    coloniaB = coloniaB + (coloniaB * taxaB)
    dias += 1

print(f"Serão necessários {dias} dias.")


# 3) Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

usuario = 1

while usuario <= 15:
    print(f'Avaliação do usuario número {usuario}.')

    avaliacao = float(input('Digite uma nota de 0 a 5 aqui: '))

    while avaliacao < 0 or avaliacao > 5:
        print('Nota inválida!, Digite um valor novamente de 0 a 5.')
        avaliacao = float(input('Digite uma nota de 0 a 5: '))

    print('Nota válida!')
    usuario += 1

# 4) Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

contador_temperatura = 0
soma = 0
temperatura = 0

while True: # nesse exercicio, quando colocamos true, significa que nós não sabemos quantas vezes o usuario irá digitar um valor de temperaturas, por isso true está ali, por que o exericcio pede um conjundo indeterminado, se fosse determinado, ai colocariamos um contador.
    print(f'Calculo de média de temperaturas')
    temperatura = float(input('Informe uma temperatura: '))

    if temperatura == -273:
        break
    else:
        soma = soma + temperatura
        contador_temperatura += 1

media = soma / contador_temperatura

print(f'Sua média de temperatura digitadas é de {media}')


# 5) Escreva um programa que calcule o fatorial de um número inteiro fornecido pela pessoa usuária. Lembrando que o fatorial de um número inteiro é a multiplicação desse número por todos os seus antecessores até o número 1. Por exemplo, o fatorial de 5 é 5 x 4 x 3 x 2 x 1 = 120.

numero = int(input('Digite um número para descobrir seu valor fatorial aqui!: '))

fatorial = 1

while numero > 1:
    fatorial = fatorial * numero
    numero -= 1

print(f'O fatorial desse número é {fatorial}')

# Momento dos projetos
# 6) Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:

print('Bem vindo a minha tabuada!')
print('Informe um número para saber quais seus valores multiplicados de 1 até 10.')
numero_mult = int(input())
multiplicacao = 1

while multiplicacao <= 10:
    valor = numero_mult * multiplicacao
    print(f'{numero_mult} x {multiplicacao} = {valor}')
    multiplicacao += 1

print(f'Tabuada completa!')

# 7) Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

# 8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.

# 9) Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos