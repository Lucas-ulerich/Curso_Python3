# Operadores Lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisa ser verdadeiras
# Se qualquer valor for considerado falso a expressão intreira será avaliada naquele valor
# São consideredo falsy 
# 0 0.0 '' False
# Também existe o tipo None
# Usado para representar um não valor


entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

# Todas as condições precisam ser verdadeiras para entrar.
# Em python, se a primeira condição for falsa, ele não checa a segunda.
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    