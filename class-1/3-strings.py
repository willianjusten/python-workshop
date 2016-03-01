# coding: utf-8

#importando módulos do pythonx
from pprint import pprint

# podemos somar strings (concatenação)
print "Hello" + " World!"

# marcadores
a = 13

print "O número %d é o favorito do Zagalo." %a

s = 'também'
print "Usando outra forma {} é legal.".format(s)

# separando os blocos de código na tela
print "=============\n\n\n\n\n\n\n\n"

# descobrindo os métodos de um objeto
w = 'O will é um péssimo professor'

# método dir vai listar todos os métodos do objeto 
# pprint vai imprimir bonitinho
# pprint(dir(w))

# deixando tudo maiusculo
print w.upper()

# verificando se termina com uma letra ou trecho
print w.endswith('professor')

# buscando se existe a palavra numa string
print w.find('will')

# verificando se a palavra é maiscula
print w.isupper()

# substituindo letras/palavras
print w.replace('will', 'jonas')

# criando array de um string
print w.split()