# Operadores in e not in
# Strings são iteráeis

# 0 1 2 3 4 
# L U C A S
# -5-4-3-2-1

nome = 'Lucas'
print(nome[-5])

print('a' in nome)
print('x' in nome)
print('zas' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else: 
    print(f'{encontrar} não está em {nome}')