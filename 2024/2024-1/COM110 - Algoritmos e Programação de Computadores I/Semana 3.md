## Tipos de dados (parte 2)

### Listas, tuplas e operadores

**Listas** são sequências **mutáveis** de objetos separados por vírgulas e envoltos por colchetes.

```
>>> pets = ['cão', 'gato', 'peixe']
>>> pets
['cão', 'gato', 'peixe']
```

**Operadores suportados**: [] (index), in, not in, +, *, len(), min(), max(), sum()

**Tuplas** são similares às listas, porém são **imutáveis**. Elas são representadas com parênteses ao invés de colchetes.

**Métodos (listas)**  
**a.append('b')**: adiciona o elemento b ao final da lista a;   
**a.count('b')**: retorna a quantidade de vezes que o elemento b aparece na lista a;  
**a.index('b')**: retorna a posição do elemento b na lista a;  
**a.insert(2,'b')**: insere o elemento b em uma determinada posição na lista a;  
**a.pop()**: retorna e remove o último elemento da lista a;   
**a.remove('b')**: remove o elemento b da lista a;  
**a.reverse()**: inverte a ordem dos elementos da lista a;  
**a.sort()**: organiza os elementos da lista a em ordem alfabética para strings e ordem crescente para valores numéricos;

<br>

### Tipos de dados

Os dados suportados pela linguagem Python são armazenados na memória na forma de objetos. Cada objeto possui um tipo e um valor.

### Biblioteca Padrão Python

A biblioteca padrão Python é uma coleção de mais de 200 módulos compostos por funções e classes específicos para um domínio de aplicação.

Aplicações que contam com módulos predefinidos incluem:
- programação para redes de computadores;
- programação para web;
- desenvolvimento de interfaces gráficas;
- banco de dados;
- funções matemáticas;
- geradores de números pseudoaleatórios;

<br>

**Módulo math**

O módulo **math** é uma biblioteca de constantes e funções matemáticas. Para usá-lo é necessário importá-lo explicitamente (**>>> import math**). O mesmo deve ser feito com a função desejada (***>>>math.sqrt(4) -> 2.0**).

| Função | Explicação |
| --- | --- |
| sqrt(x) | raiz quadrada de x |
| ceil(x) | [x] (ou seja, o menor inteiro >= x) |
| floor(x) | [x] (ou seja, o maior inteiro <>= x) |
| cos(x) | cos(x) |
| sin(x) | sin(x) |
| log(x, base) | logb(x) |
| pi | 3,14159263589793 |
| e | 2,718281828459045 |

**Módulo fractions**

O módulo **fractions** torna possível o uso de frações e a realização de números racionais. 

```
>>> import fractions
>>> a = fractions.Fraction(1,2)
>>> b = fractions.Fraction(3,4)
>>> a + b
```
<br>

S