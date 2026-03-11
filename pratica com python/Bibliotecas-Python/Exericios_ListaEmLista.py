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

