# Conversão de tipos, coerção, type convertion, typecasting, coercion.
# É o ato de converter um tipo em outro tipos imutáveis e primitivos.
# str, int, float, bool

print('1' + 1)
print('a' + 'b') # o sinal de mais também server para concatenar

# print('1' + 1) # vai gerar erro de tipo pois o python não converte os tipos automaticamente.
# Pois o python tem a tipagem forte.

print(int('1'), type(int('1')))
print(int('1') + 1) # converteu a string '1' para um numero e somou.
print(float('1') + 1)
print(bool('')) # String vazia
print(bool('_')) # String com conteudo
print(str(11) + 'b') # converteu o número 11 para string