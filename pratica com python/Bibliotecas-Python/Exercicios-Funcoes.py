# 1. Escreva um código que lê a lista abaixo e faça: A leitura do tamanho da lista, a leitura do maior e menor valor e a soma dos valores da lista
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

maior_lista = max(lista)
menor_lista = min(lista)
qtd_lista = len(lista)
soma_total = sum(lista)

print(f'A lista possui {qtd_lista} números em que o maior número é o {maior_lista} e o menor número é {menor_lista}. A soma dos valores presentes nela é igual a {soma_total}.')

#Escreva uma função que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 7, a tabuada deve ser mostrada no seguinte formato:

numero = int(input('Digite aqui um número!: '))
def tabuada(numero_escolhido):
    for multiplicador in range(1, 11):
        resultado = numero_escolhido * multiplicador
        print(f'{multiplicador} x {numero_escolhido} = {resultado}')
tabuada(numero)
    
