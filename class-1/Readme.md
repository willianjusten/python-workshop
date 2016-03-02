## Resumo Class 1

### Material

- [Slides Apresentação](http://willianjusten.com.br/python-class-1/)
- [Documentação da Linguagem Python](http://turing.com.br/pydoc/2.7/contents.html)

### Rodando Python

Temos 2 formas de rodar Python:

- Interativa: basta digitar `python` no terminal que ele abre um interpretador dinâmico.
- Interpretador de arquivo: digitando `python nome_do_arquivo.py` dentro do terminal, ele irá interpretar e executar o arquivo.

### Imprimir na tela

Podemos usar o comando `print` para imprimir qualquer coisa na tela.

```python

print "Hello World!"
```

### Pedindo informação do usuário

Para pedir um dado do usuário, podemos usar o comando `input`.

```python

input('Digite um numero: ')
```

*Obs.: para que não tenhamos erro ao escrever algo sem o tipo correto, é aconselhável fazer o uso de **type casting** no valor do input. Veremos mais abaixo.*

### Comentários

Em python existem duas formas de se criar um comentário:

- Usando `#`
- Usando `"""` (3 aspas)

```python

# isso é um comentário

"""
Isso também é
um comentário
"""

```

### Variáveis

Aprendemos que Python é uma linguagem:

- **Tipagem dinâmica**: não precisamos definir os tipos de nossas variáveis.
- **Fortemente tipada**: uma variável não irá mudar seu tipo para se encaixar com outra. (Exemplo: não podemos concatenar 43 com string 'will')
- **Atribuição Múltipla**: podemos atribuir vários valores a mais de uma variável ao mesmo tempo.

Para definir uma variável, basta escolher um nome e passar só um sinal de igual `a = 3`.

#### Buscando a variável na memória

Cada variável no Python é um objeto e cada um deles possui um endereço de memória, podemos descobrir esse endereço usando o método `id`.

```python

a = 25

id(a) # endereço de memória
id(25) # mesmo endereço de memória de a

id(a) == id(25) # True
```

#### Tipos de variáveis

Existem diversos tipos de variáveis em Python, mas para esse início, vimos 4 dos mais importantes:

- **int**: define um número inteiro.
- **float**: define um número decimal.
- **string**: um conjunto de caracteres, que pode ser uma palavra ou frases.
- **boolean**: variável que indica `True` ou `False`

### Descobrindo métodos de um objeto

Como dito, tudo em Python é um objeto, portanto, cada objeto possui métodos builtin de Python. Para descobrir os métodos de um objeto, basta usar o comando `dir`.

```python

dir(3) # irá mostrar os métodos de um inteiro
dir(3.14) # irá mostrar os métodos de um float
dir('will') # irá mostrar os métodos de uma string
```

### String

Em strings, descobrimos alguns métodos como:

```python

# deixando tudo maiusculo
print 'will'.upper()

# verificando se termina com uma letra ou trecho
print 'will'.endswith('professor')

# buscando se existe a palavra numa string
print 'will'.find('will')

# verificando se a palavra é maiscula
print 'will'.isupper()

# substituindo letras/palavras
print 'will'.replace('will', 'jonas')

# criando array de um string
print 'will'.split()
```

### Usando o help para entender métodos

Uma coisa muito legal do Python é que ela possui um método chamado `help`, que te explica o que exatamente cada método faz, então se você quiser descobrir o que algum método faz, basta usar o help.

```python

help('will'.upper)

help(unittest.TestCase.assertEqual)
```

#### Marcadores

Descobrimos que podemos concatenar strings e até mesmo usar marcadores para facilitar o uso com variáveis.

```python

print "Hello" + " World!"

a = 13
print "O número %d é o favorito do Zagalo." %a

print "O will é um {} professor.".format('péssimo')
```

### Math

Assim como todas as linguagens, python possui os métodos básicos de aritmética.

```python

print 2 + 2 # soma
print 2 - 2 # subtração
print 2 / 2 # divisão
print 2 * 2 # multiplicação
print 2 % 2 # módulo
print 2 ** 2 # potência
```

### Módulos

Aprendemos que Python possui vários módulos para que possamos importar e facilitar nossas vidas com coisas já prontas. Para importar um módulo inteiro basta usar:

```python

import modulo_desejado
```

Para importar algum método de um módulo:

```python

from modulo import metodo
```

Segue abaixo um exemplo importando o método `sqrt` (raiz quadrada) do módulo `math`.

```python
from math import sqrt

print sqrt(16) # 4.0
```

### Métodos

Nossos métodos, que também podem ser conhecidos como funções em outros linguagens, são criados a partir da palavra `def`. Seguido de um parênteses contendo os argumentos e sempre ao inicializar um bloco de execução, usamos os `:` (Dois pontos). Segue um exemplo da criação de um método de soma:

```python

def soma(a, b):
    return a + b
```

*Lembre-se que em python a indentação é importante, portanto, sempre depois de iniciar um bloco, precisamos indentar o código do mesmo.*

### Testes

Uma das coisas mais importantes da programação e que precisa cada vez mais ser difundida e usada desde o início do aprendizado, é o método de se trabalhar com testes. Os testes visam garantir mais qualidade ao código, facilitar na construção do mesmo já antevendo problemas e ser um auxiliador para se encontrar bugs mais facilmente. Nessa primeira parte, tivemos uma pequena introdução, mas que iremos levar para todos os próximos estudos.

O Python já possui uma biblioteca de testes integrado que é o módulo `unittest` e dentro dela, temos o `TestCase`, que possui os principais `asserts`, que são:

- **assert**: permite fazer os próprios asserts
- **assertEqual(a, b)**: verifica se a é igual a b
- **assertNotEqual(a, b)**: verifica se a não é igual a b
- **assertIn(a, b)**: verifica se a existe em b
- **assertNotIn(a, b)**: verifica se a não existe em b
- **assertFalse(a)**: verifica se o valor é False
- **assertTrue(a)**: verifica se o valor é True
- **assertIsInstance(a, TYPE)**: verifica o tipo da variável
- **assertRaises(ERROR, a, args)**: verifica se quando a é chamado sobe um erro

Para se rodar os testes com o unitest temos os seguintes passos:

- Criamos uma `class` derivada de `unittest.TestCase`
- Criamos métodos iniciados com a palavra `test_`
- Fazemos a chamada do `unitest.main()` ao final do arquivo

Segue um exemplo de um teste simples:

```python

# primeiro importamos o módulo de testes
import unittest

#depois criamos a classe que vai realizar os testes
class Testing(unittest.TestCase):
    # definimos os métodos de teste sempre começando com a palavra
    # test_
    def test_upper(self):
        # usamos então os diferentes tipos de asserts para testar
        self.assertEqual('foo'.upper(), 'FOO')

    def test_soma(self):
        self.assertEqual(2+2, 4)

    def test_soma_errada(self):
        self.assertNotEqual(2*3, 8)

    def test_acha_palavra(self):
        self.assertIn('will', 'will é um péssimo professor')

    def test_acha_palavra(self):
        self.assertIn('willian', 'will é um péssimo professor')

# mandamos rodar o método de unittest
unittest.main()
```

Para rodar esses testes, basta executarmos o arquivo com `python arquivo_de_testes.py`. Podemos deixar ainda melhor passando alguns parâmetros como:

- `python arquivo_de_testes.py -v` (verbose): modo verboso que irá imprimir mais informações na tela.
- `python arquivo_de_testes.py -f` (failfast): irá parar no primeiro teste que quebrar.








