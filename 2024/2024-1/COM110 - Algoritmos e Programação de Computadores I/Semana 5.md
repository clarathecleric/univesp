## 5. Estruturas de Condição

### Estruturas de condição de uma ou duas vias

As **estruturas de seleção** permitem escolher um conjunto de ações para ser executado em um determinado momento. Tais conjuntos (**instruções**) são representadas por **blocos** delimitados por indentações. A escolha de execução depende de uma **condição**, representada por expressões lógicas ou relacionais, ser ou não satisfeita (true ou false).

As estruturas de seleção podem ser de uma, duas, ou três ou mais vias.

Nas estruturas de uma ou duas vias, apenas **uma** condição é testada.

**Seleção de uma via (if)**

Se a condição é verdadeira o bloco é executado, e se é falsa, é ignorado;

if <condição>:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco 1 de instruções indentado>  
<bloco de instruções não indentado>

**Seleção de duas vias (if/else)**

Se a condição é verdadeira um dos blocos é executado, e se é falsa, o outro; 

if <condição>:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco 1 de instruções indentado>  
else:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco 2 de instruções indentado>  
<bloco de instruções não indentado>

[Exemplo](Code/s5-ex1.py)

### Estruturas de condição de três ou mais vias

**Seleção três ou mais vias**

Nas estruturas de condição de três ou mais vias, testa-se **mais de uma** condição. Se a condição é verdadeira, o bloco corresponde é executado, se é falsa, testa-se a próxima condição.

if <condição 1>:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco de instruções intentado 1>  
elif <condição 2>:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco de instruções indentado 2>  
elif <condição 3>:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco de instruções indentado 3>  
else:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<último bloco de instruções indentado>  
<bloco de instruções não indentado>

[Exemplo](Code/s5-ex2.py)

<br>

**Ordem das Condições**

No caso de condições com três ou mais vias, é necessário verificar a ordem em que as condições são definidas para evitar erros.