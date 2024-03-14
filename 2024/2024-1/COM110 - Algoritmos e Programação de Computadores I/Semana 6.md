## 6. Estruturas de repetição

As **estruturas de repetição** (também chamadas de laços ou loops) são estruturas de controle de fluxo que permitem repetir uma sequência de comandos. Enquanto a quantidade de repetições pode ser indefinida, ela deve ser **finita**.

### Estruturas de repetição - for

O comando **for** é utilizado para percorrer ou **iterar*** sobre uma sequência de dados (seja esse uma lista, uma tupla, uma string, etc.), executando um conjunto de instruções em cada item.

**&nbsp;**iteração**: processo de repetição de uma ou mais ações;*

for <variável> in <sequência>:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco de código indentado>  
<bloco de código não indentado>

A quantidade de iterações é igual a quantidade de itens na lista que atendam as condições definidas.

[Exemplo 1](Code/s6-ex1.py)  
[Exemplo 2](Code/s6-ex2.py)

<br>

**Função range()**

A função **range** permite especificar o início (**start**), o passo (**step**) e o valor final (**stop**) de uma sequência.

range(start, stop, step)

**LEMBRETE**: o único parâmetro obrigatório é o **fim**, os outros valores são automaticamente considerados 1 se não forem definidos.

O valor final **não é** exibido na sequência.

[Exemplo](Code/s6-ex3.py)

<br>

**Acumuladores**

As **variáveis acumuladoras** acumulam valores durante as iterações de um loop, ou seja, armazenam a somatória dos valores que atendem as condições definidas.

[Exemplo](Code/s6-ex4.py)

<br>

**Loops aninhados**

O **aninhamento** de loops consiste na inserção de loops dentro de outros loops. Dessa forma, a cada iteração do loop externo, ocorre a execução de todo o bloco do loop interno.

[Exemplo](Code/s6-ex5.py)

<br>

### Estruturas de repetição - while

O comando **while** é utilizado para execução de um bloco de código **enquanto** uma determinada condição for satisfeita. 

Sua estrutura é similar ao teste condicional de uma via: enquanto a condição for verdadeira (true), o bloco é executado. A partir do momento que ela se torna falsa (false), o programa prossegue.

while <condição>:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco de código indentado>  
<bloco de código não indentado>

Esse comando é útil quando não sabemos quantas vezes em bloco deverá ser repetido.

[Exemplo 1](Code/s6-ex6.py)  
[Exemplo 2](Code/s6-ex7.py)

<br>

**Loops infinitos**

Loops **infinitos** são executados "para sempre" e são úteis quando o programa deve fornecer um serviço indefinidamente.

while True:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<bloco de código indentado>

A saída do loop sedá por Ctrl+C.