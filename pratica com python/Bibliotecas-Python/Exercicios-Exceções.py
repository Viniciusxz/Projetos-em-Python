#1. Faça um programa que solicite à pessoa usuária digitar dois números float e calcular a divisão entre esses números. O código deve conter um tratamento de erro, 
# indicando o tipo de erro que foi gerado caso a divisão não seja possível de realizar.


print('Bem vindo a minha calculadora de divisão entre 2 numeros decimais!')
print('Digite números decimais com . e não com , !')
try:
    numero1 = float(input("Digite um número aqui! : "))
    numero2 = float(input("Digite outro número aqui! : "))
except ValueError as erro1:
    print(f"Você precisa digitar um número válido. {erro1}")
except ZeroDivisionError as erro2:
    print(f"Não é possível dividir por zero. {erro2}")
else:
    print(f"Números digitados: {numero1} e {numero2}, realizando a divisão...")
    divisao = numero1 / numero2
    print(f"Divisão realizada!, a resposta é... {divisao}")
finally:
    print("Fim do programa.")

#2. Faça um programa que solicite à pessoa usuária digitar um texto que será uma chave a ser pesquisada no seguinte 
# dicionário: idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}, 
# armazenando o resultado do valor em uma variável. 
# O código deve conter um tratamento de erro KeyError, 
# imprimindo a informação 'Nome não encontrado', caso ocorra o erro; e imprimir o valor caso não ocorra nenhum.

idades = {'Júlia': 16, 'Carol': 23, 'Alberto': 19, 'Roberta': 17}

try:
    nome = input("Digite p nome do(a) estudante: ")
    resultado = idades[nome]
except KeyError:
    print("Nome não encontrado.")
else:
    print(resultado)
