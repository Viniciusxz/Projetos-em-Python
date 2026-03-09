#1. Crie um código para imprimir a soma dos elementos de cada uma das listas contidas na seguinte lista:

lista_de_listas = [[4,6,5,9], [1,0,7,2], [3,4,1,8]]

for linha in lista_de_listas:

    soma = 0
    for numero in linha:
        soma = soma + numero
        
    print(f'{soma}')