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

Os dados suportados pela linguagem Python são armazenados na memória na forma de **objetos**. Cada objeto possui um **tipo** e um **valor**. 

O **tipo** de um objeto indica quais valores ele pode armazenar e quais operações podem ser executadas. Ele pode ser verificado através da função *type()*.
- o tipo *int* comporta grandes valores com base na disponibilidade de memória;
- o tipo *float* atualmente comporta valores de até 64 bits, que podem ser aproximados;

Podemos usar **construtores** (int(), float(), str() e list()) para explicitamente definir objetos de um determinado tipo. Seus valores padrão são, respectivamente: 0, 0.0, '' e []. Construtores são tipicamente utilizados para a **conversão** de tipos.

**Conversões Implícitas**

Dá-se o nome de **conversão implícita** àquela que ocorre quando há uma expressão com operandos de diferentes tipos que são automaticamente convertidos pela linguagem Python. 

**Conversões Explícitas**

Já a **conversão explícita** ocorre quando é necessário definir "manualmente" a conversão através dos construtores.

<br>

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

\>>> import fractions  
\>>> a = fractions.Fraction(1,2)  
\>>> b = fractions.Fraction(3,4)   
\>>> a + b


$$
\frac{1}{2} + \frac{3}{4} = \frac{5}{4}
$$

<br>

Enquanto o uso das frações permite a representação de números muito maiores que o tipo float, seu uso torna o processo mais lento.