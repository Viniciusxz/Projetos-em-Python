#1) Faça um programa que tenha a seguinte lista contendo os valores de gastos de uma empresa de papel [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]. Com esses valores, faça um programa que calcule a média de gastos. Dica: use as funções built-in sum() e len().

papel_empresa = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
produtos = len(papel_empresa)
soma_empresa = sum(papel_empresa)
media_empresa = soma_empresa / produtos
print(f'A empresa teve um total de {produtos} produtos e teve uma média de lucro de {media_empresa}.')

#2) Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.
contar_produtos = 0

for valor_alto in papel_empresa:
    if valor_alto > 3000:
        contar_produtos += 1

total_compras = len(papel_empresa)
porcentagem = (contar_produtos / total_compras) * 100

print(f'Foram realizadas {contar_produtos} compras acima de 3000 reais!')
print(f'A porcentagem total de compras é de {porcentagem:.2f}%')

#3) Faça um código que colete em uma lista 5 números inteiros quaisquer e imprima a lista. Exemplo: [1,4,7,2,4].
contador_numeros = 1
numeros_oficial = []

while contador_numeros < 6:
    numeros = int(input('Digite aqui um número: '))
    numeros_oficial.append(numeros)
    contador_numeros += 1

print(numeros_oficial)

#4) Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

contador_numeros2 = 1
numeros_oficial_2 = []

while contador_numeros2 < 6:
    numeros1 = int(input('Digite aqui um número: '))
    numeros_oficial_2.append(numeros1)
    contador_numeros2 += 1

print(f'Haha!, Inverti seus números! agora olha como eles estão: {numeros_oficial_2[::-1]}')

#5) Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

n = int(input('Digite um número: '))

lista_primos = []

for numero in range(2, n + 1):
    primo = True
    divisor = 2

    while divisor < numero:
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1

    if primo:
        lista_primos.append(numero)

print(lista_primos)


#6) Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.

data = int(input('Informe a dia atual: '))
mes = int(input('Informe o mês atual: '))
ano = int(input('Informe o ano atual: '))

dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if ano > 0: # ANO
    print('Ano válido!')
else:
    print('Ano inválido!')

if 1 <= mes <= 12: # MES
    print('Mês válido!')
else:
    print('Mês inválido!')

max_dias_mes = dias_meses[mes - 1]

if 1 <= data <= max_dias_mes: # DATA
    print('Data Válida!')
else:
    print('Data Inválida.')




#Momento dos projetos
#7) Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado o número de bactérias por dia (em milhares) e pode ser observado a seguir: [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número de bactérias em cada dia com o número de bactérias do dia anterior. Dica: para calcular o percentual de crescimento usamos a seguinte equação: 100 * (amostra_atual - amostra_passada) / (amostra_passada).

#8) Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.

#9) Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.

#10) Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

#11) Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:

#{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
# 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}

#Escreva um código que calcule o total de vendas e o produto mais vendido.

#12) Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

#'''
#Design 1 - 1334 votos
#Design 2 - 982 votos
#Design 3 - 1751 votos
#Design 4 - 210 votos
#Design 5 - 1811 votos
#'''

#Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.

#13) As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.

#14) Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta. A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário. Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.

# {'Área Norte': [2819, 7236],
 #'Área Leste': [1440, 9492],
 #'Área Sul': [5969, 7496],
 #'Área Oeste': [14446, 49688],
 #'Área Centro': [22558, 45148]}

# Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica. Dica: use as funções built-in sum() e len().

#15) O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:

#{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 #'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 #'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 #'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

#Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.