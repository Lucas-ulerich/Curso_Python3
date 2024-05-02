print(12)
"""
A função print pode receber um ou mais argumentos,
para adicionar mais argumentos precisamo colocar uma virgula
e adicionar o proximo argumento
"""

print(35, 78)

"""
O print também possui argumentos não nomeados, note que na saida ele quebrou a linha 
e na outra saida ele deu um espaço entre os números.
"""

"""Temos também os argumentos nomeados, onde podemos configurar enão deixar padrão"""

print(12, 45, sep=" - ") # O argumento sep significa separador o nesse caso o espaço foi subistituido pelo "-"

"""
O argumento end=" " mexe no final dos argumentos, podemos adicionar qualquer coisa
ou colocar uma quebra de linha
"""

print(12, 45, 1001, end='#\n')
print(12, 45, 1001, end='\n****')
