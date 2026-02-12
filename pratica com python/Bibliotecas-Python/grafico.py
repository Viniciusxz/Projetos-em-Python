import matplotlib.pyplot as plt
from random import choice

estudantes = ['João', 'Maria', 'José']
estudantes_2 = ['João', 'Maria', 'José']
notas = [8.5, 9, 6.5]

plt.bar(x = estudantes, height = notas)
estudante = choice(estudantes_2)
print(f'o Estudante sorteado foi {estudante}') 
plt.show() 