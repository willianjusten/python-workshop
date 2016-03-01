# coding: utf-8 

# definindo um valor
a = 25

# verificando onde está o a
print "A variável a está em", id(a)

# verificando onde está o 25
print "A variável 25 está em", id(25)

# mudando o valor de a
a = 'will'

# verificando onde está o a agora
print "A variável a está agora em", id(a)

# imprimindo o novo valor de a
# tipagem dinâmica! YEY! =D
print a

# separando os blocos de código na tela
print "=============\n\n\n\n\n\n\n\n"

# criando duas variáveis ao mesmo tempo
c, d = 5, 6

print "O valor de c:", c
print "O valor de d:", d

# trocando os valores entre as variáveis
# atribuição múltipla
c, d = d, c

print "O valor agora de c:", c
print "O valor agora de d:", d

# separando os blocos de código na tela
print "=============\n\n\n\n\n\n\n\n"

# verificando o tipo de a
print "O tipo de 3 é:", type(a)

print "O tipo de 3.14 é:", type(3.14)

print "O tipo da palavra will é:", type('will')

print "E para True", type(True)

# separando os blocos de código na tela
print "=============\n\n\n\n\n\n\n\n"

# convertendo tipos de variável (type casting)
print str(25) + ' will'

# convertendo para int
print int(100.123)