import numpy as np
import matplotlib as mp
from random import choice, randrange, randint 
# 1. Escreva um código para instalar a versão 3.7.1 da biblioteca matplotlib.

# crtl+shift+' e digitar no terminal python -m pip install matplotlib'

# 2. Escreva um código para importar a biblioteca numpy com o alias np.

# import numpy as np

# 3. Crie um programa que leia a seguinte lista de números e escolha um número desta aleatoriamente.
# lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
sorteio = choice(lista) # choice serve para sortear um número aleatorio.
print(f'O número sorteado para ser escolhido foi {sorteio}.')

# 4. Crie um programa que sorteia, aleatoriamente, um número inteiro positivo menor que 100.
print('Vamos ver quanta sorte você terá hoje, da escla de 0 até 100!')
listaVazia = []
for i in range(0,1):
    listaVazia.append(randrange(100))

print(f'Sua sorte hoje será de {listaVazia}.')
# 5. Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

num1 = int(input('Digite aqui um número!: '))
num2 = int(input('Digite aqui um outro número!: '))

resultado = pow(num1, num2) # pow serve para calcular a potencia de 2 numeros selecionados, sendo num1 a base e num2 a potencia.
print(f'Basicamente, o primeiro número que voce digitou é a base, e o segundo é o expoente! Vamos ver quanto é e... {resultado}.')

# Aplicando a projetos
# 6. Um programa deve ser escrito para sortear uma pessoa seguidora de uma rede social para ganhar um prêmio. A lista de participantes é numerada e devemos escolher aleatoriamente um número de acordo com a quantidade de participantes. Peça à pessoa usuária para fornecer o número de participantes do sorteio e devolva para ela o número sorteado.
print('SORTEIO ONLINE')
sorteio1 = int(input('Digite aqui quantas pessoas irão participar, e realizaremos um sorteio!: '))

sorteio2 = randrange(1, (sorteio1 + 1))
print(f'A pessoa sorteada foi: {sorteio2}. Parabéns!')

# 7. Você recebeu uma demanda para gerar números de token para acessar o aplicativo de uma empresa. 
# O token precisa ser par e variar de 1000 até 9998. Escreva um código que solicita à pessoa usuária o seu nome e exibe uma mensagem junto a esse token gerado aleatoriamente.

nome = str(input('Digite seu nome aqui: '))
token = randrange(1000, 9998, 2)

print(f'Olá, {nome}, o seu token de acesso é {token}! Seja bem vindo(a)!')
    



# "Olá, [nome], o seu token de acesso é [token]! Seja bem-vindo(a)!"

# 8. Para diversificar e atrair novos(as) clientes, uma lanchonete criou um item misterioso em seu cardápio chamado "salada de frutas surpresa". 
# Neste item, são escolhidas aleatoriamente 3 frutas de uma lista de 12 para compor a salada de frutas da pessoa cliente. Crie o código que faça essa seleção aleatória de acordo com a lista abaixo:

