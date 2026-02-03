 # trabalhando com operadores logicos: AND, OR, NOT e IN

t1 = t2 = True
f1 = f2 = False # Multipla atribuição

if t1 and t2:
    print('expressão verdadeira')
else:
    print('expressão falsa')
    # Análise de condição com 2 variaveis. se os 2 valores são verdadeiros ou falsos.

if t1 or f2:
    print('expressão verdadeira')
else:
    print('expressão falsa')
    # Analisa se as condições possuem ao menos 1 condição verdadeira. se t1 é verdadeiro ou se f2 é verdadeiro, se apenas um possui valor verdadeiro, então a sentença é verdadeira.

if not t1:
    print('expressão verdadeira')
else:
    print('expressão falsa')
    # Analisa as condições para retornar o valor oposto a variavel que foi dado.

lista = 'Vinícius Ribeiro, Pedro Antônio, Marcelo Rodrigues'
nome_1 = 'Vinícius Ribeiro'
nome_2 = 'Maria Clara'

if nome_1 in lista:
    print(f'{nome_1} está na lista.')
else:
    print(f'{nome_1} não está na lista.')

if nome_2 in lista:
    print(f'{nome_2} está na lista.')
else:
    print(f'{nome_2} não está na lista.')