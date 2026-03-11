#1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

for linha in lista_de_listas:

    soma = 0
    for numero in linha:
        soma = soma + numero
        
    print(f'{soma}')

#2. Crie um código para gerar uma lista que armazena o terceiro elemento de cada tupla contida na seguinte lista de tuplas:

lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]
idades = []

for idade in lista_de_tuplas:
    idades.append(idade[2])

print(f'{idades}')

#3. A partir da lista: lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo'], crie um código para gerar uma lista de tuplas em que cada tupla tenha o primeiro elemento como a posição do nome na lista original e o segundo elemento sendo o próprio nome.

lista = ['Pedro', 'Júlia', 'Otávio', 'Eduardo']
codigo_lista = []

for elemento, pessoa in enumerate(lista):
    codigo_lista.append((elemento, pessoa))

print(codigo_lista)

#4. Crie uma lista usando o list comprehension que armazena somente o valor numérico de cada tupla caso o primeiro elemento seja 'Apartamento', a partir da seguinte lista de tuplas:
aluguel = [('Apartamento', 1700), ('Apartamento', 1400), ('Casa', 2150), ('Apartamento', 1900), ('Casa', 1100)]

apartamento_ofc = [n[1] for n in aluguel if n[0] == 'Apartamento']
print(apartamento_ofc)

#5. Crie um dicionário usando o dict comprehension em que as chaves estão na lista meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'] e os valores estão em despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360].
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
despesa = [860, 490, 1010, 780, 900, 630, 590, 770, 620, 560, 840, 360]

despesa_anual = {meses[i]: despesa[i] for i in range(len(meses))}
print(despesa_anual)

#6. Uma loja possui um banco de dados com a informação de venda de cada representante e de cada ano e precisa filtrar somente os dados do ano 2022 com venda maior do que 6000. A loja forneceu uma amostra contendo apenas as colunas com os anos e os valores de venda para que você ajude a realizar a filtragem dos dados a partir de um código:
vendas = [('2023', 4093), ('2021', 4320), ('2021', 5959), ('2022', 8883), ('2023', 9859), ('2022', 5141), ('2022', 7688), ('2022', 9544), ('2023', 4794), ('2021', 7178), ('2022', 3030), ('2021', 7471), ('2022', 4226), ('2022', 8190), ('2021', 9680), ('2022', 5616)]
# Crie uma lista usando list comprehension para filtrar os valores de 2022 e que sejam maiores que 6000.

vendas_ofc = [x for x in vendas if x[0] == '2022' and x[1] > 6000]
print(vendas_ofc)

#7.Uma clínica analisa dados de pacientes e armazena o valor numérico da glicose em um banco de dados e gostaria de rotular os dados da seguinte maneira:

#Glicose igual ou inferior a 70: 'Hipoglicemia'
#Glicose entre 70 a 99: 'Normal'
#Glicose entre 100 e 125: 'Alterada'
#Glicose superior a 125: 'Diabetes'
#A clínica disponibilizou parte dos valores e sua tarefa é criar uma lista de tuplas usando list comprehension contendo o rótulo e o valor da glicemia em cada tupla.

glicemia = [129, 82, 60, 97, 101, 65, 62, 167, 87, 53, 58, 92, 66, 120, 109, 62, 86, 96, 103, 88, 155, 52, 89, 73]

sistema_glicemia = [
    (
    'Hipoglicemia' if valor <= 70
    else 'Normal' if valor <= 99
    else 'Alterada' if valor <= 125
    else 'Diabetes',
    valor
    )
  for valor in glicemia
]

print(sistema_glicemia)

#8. Um e-commerce possui as informações de id de venda, quantidade vendida e preço do produto divididos nas seguintes listas:

#O e-commerce precisa estruturar esses dados em uma tabela contendo o valor total da venda, que é obtida multiplicando a quantidade pelo preço unitário. 
# Além disso, a tabela precisa conter um cabeçalho indicando as colunas: 'id', 'quantidade', 'preco' e 'total'.

#Crie uma lista de tuplas em que cada tupla tenha id, quantidade, preço e valor total, na qual a primeira tupla é o cabeçalho da tabela.

id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
quantidade = [15, 12, 1, 15, 2, 11, 2, 12, 2, 4]
preco = [93.0, 102.0, 18.0, 41.0, 122.0, 14.0, 71.0, 48.0, 14.0, 144.0]

ecommerce_sistema = []
ecommerce_sistema.append(('id', 'quantidade', 'preco', 'total'))

for i in range(len(quantidade)):
    resultado = quantidade[i] * preco[i]
    tupla = (id[i], quantidade[i], preco[i], resultado)
    ecommerce_sistema.append(tupla)
print(ecommerce_sistema)