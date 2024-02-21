## 2. Tipos de dados (parte 1)

### Expressões aritméticas e operadores

**Expressões aritméticas** são operações com **operadores aritméticos** e cujos operandos são números, constantes numéricas ou variáveis do tipo numérico.

|<center> Operador |<center> Significado |
| --- | --- |
|<center> + |<center> adição |
|<center> - |<center> subtração |
|<center> * |<center> multiplicação |
|<center> / |<center> divisão  |
|<center> // |<center> divisão inteira* |
|<center> % |<center> módulo** |
|<center> ** |<center> exponenciação |

\* &nbsp; a *divisão inteira* ignora o resto da divisão  
** &nbsp; o *módulo* apresenta apenas o resto da divisão

<br>

**Funções Matemáticas**  
**abs()**: retorna o valor absoluto de um número;  
**min()**: retorna o mínimo de um conjunto de valores;  
**max()**: retorna o máximo de um conjunto de valores;

<br>

### Expressões lógicas e operadores

**Expressões lógicas** são operações com **operadores lógicos ou relacionais** e cujos operandos são relações ou variáveis/constantes do tipo lógico.

São operadores relacionais:
|<center> Operador |<center> Significado |
| --- | --- |
|<center> == |<center> igual |
|<center> != |<center> diferente |
|<center> < |<center> menor |
|<center> > |<center> maior |
|<center> <= |<center> menor ou igual |
|<center> >= |<center> maior ou igual |

São operadores lógicos:
|<center> Operador |<center> Significado |
| --- | --- |
|<center> and |<center> e |
|<center> not |<center> não (T e F invertidos) |
|<center> or |<center> ou |
|<center> in |<center> pertence |
|<center> not in |<center> não pertence |
|<center> is |<center> é |
|<center> is not |<center> não é | 

Os resultados das expressões lógicas podem resultar apenas em **True** (verdadeiro) e **False** (falso).

<br>

A precedência das operações segue a ordem abaixo:
1. Parênteses mais internos;
2. Operadores aritméticos (seguindo precedência algébrica);
3. Operadores relacionais;
4. Operadores de atribuição (veremos futuramente);
5. Operadores lógicos (not, or, and primeiro);

<br>

### Variáveis

**Variável** é o nome a qual é atribuído (=) um objeto. Isso permite que a informação representada pela variável seja recuperada em diversas partes do código.

```
>>> x = 3 + 3
>>> 2 * x
12
>>> y = x -2
>>> y
4
```

Os nomes de variáveis podem conter apenas:
- caracteres maiúsculos (A-Z);
- caracteres minúsculos (a-z);
- underscore (_);
- dígitos de 0 a 9 (exceto no primeiro caractere);

**ATENÇÃO**: caracteres maiúsculos e minúsculos não são equivalentes (aVar =/= avar).

São consideradas boas práticas de nomenclatura:
- a utilização de nomes significativos (preco ao invés de p);
- a utilização de undercore ou letra maiúscula para separar duas palavras (tempVar, temp_var);
- a utilização de nomes curtos;

Palavras reservadas **não podem** ser usadas como nomes variáveis.

|<center> Palavras Reservadas |
| --- |
| False &nbsp;&nbsp;&nbsp;&nbsp; break &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; else &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; not &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; while <br> None &nbsp;&nbsp;&nbsp; class &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; except &nbsp;&nbsp;&nbsp;&nbsp; import &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; or &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; with &nbsp;&nbsp;&nbsp;&nbsp; <br> True &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; continue &nbsp;&nbsp;&nbsp;&nbsp; finally &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; in &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; pass &nbsp;&nbsp;&nbsp;&nbsp; yield <br> and &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; def &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; is &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; raise &nbsp;&nbsp;&nbsp;&nbsp; <br> as &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; del &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; from &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; lambda &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return <br> assert &nbsp;&nbsp;&nbsp; elif &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; global &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nonlocal &nbsp;&nbsp;&nbsp;&nbsp; try |


### Tipos de dados

**int**: números inteiros;  
**float**: números com casas decimais;  
**bool**: true ou false;  
**string (str)**: texto ou sequência de caracteres;

### Strings

**Strings** são um tipo de variável **imutável** usando para representar ou manipular texto ou uma sequência de caracteres. Ela é composta por uma sequência de caracteres envolvida por aspas (simples ou duplas).

Alguns operadores importantes são:  
**len()**: indica o tamanho da string;  
**[]**: operador de indexação  
&nbsp;&nbsp;&nbsp; - o índice varia de 0 a len()-1;  
&nbsp;&nbsp;&nbsp; - índices negativos iniciam a contagem do lado direito da string;  
&nbsp;&nbsp;&nbsp; - é possível acessar **substrings** através da indexação (s [ x : y ]);

```
>>> s = 'abcd'
>>> s[0:2]
'ab'
>>> s[-4:-2]
'ab'
>>> s[:3]
'abc'
>>> s[-1:]
'd'
```

<br>

**Métodos (strings)**  
**s.find(p)**: retorna o índice em que a substring p aparece em s  
**s.count(p)**: retorna a frequência em que a substring p aparece
em s  
**s.replace(p, q)**: substitui a substring p pela substring q em s  
**s.capitalize()**: substitui primeiro caractere de s em maiúscula  
**s.upper()**: substitui todos os caracteres de s em maiúscula  
**s.lower()**: substitui todos os caracteres de s em minúscula  
**s.strip()**: remove espaços em branco em excesso