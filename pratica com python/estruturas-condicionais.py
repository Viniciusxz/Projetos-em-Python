# Estruturas condicionais com IF, ELSE e ELIF

idade_maria = int(input('Digite a idade da Maria: '))
idade_beatriz = int(input('Digite a idade da Beatriz: '))

if idade_maria > idade_beatriz:
  print('Maria é mais velha que Beatriz.')


# Sistema de alunos aprovados ou reprovados.
# Atualização 1 - Sistema com recuperação

media = float(input('Digite a média: '))

if media >= 6.0:
  print('Aprovado(a)!')
if 6.0 > media >= 4.0:
  print('Recuperação!')
if media < 4.0:
  print('Reprovado(a)!')

# Sistema com recuperação

