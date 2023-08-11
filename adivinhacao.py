print('********************************')
print('Bem vindo ao jogo de adivinhação')
print('********************************')


numero_secreto = 42

chute = input('Digite o seu número: ')

print('Você digitou o número: ')
print(chute)

if (numero_secreto == chute):
    print('Você acertou')
else:
    print('Você errou!')
