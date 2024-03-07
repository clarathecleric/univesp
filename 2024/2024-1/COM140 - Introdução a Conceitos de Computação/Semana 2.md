## 2. Representação de dados, sistemas de numeração e conversão de base

### Representação de dados

| Dados | Informação | Conhecimento |
| --- | --- | --- |
| * elementos conhecidos de um problema; <br> * desprovidos de significado se considerados isoladamente; | * conjunto estruturado de dados; <br> * possui utilidade e pode gerar ações; | * síntese de múltiplas fontes de informação; <br> * possui elevado significado e utilidade para o suporte à tomada de decisões; |

<br>

**Dispositivos analógicos** utilizam representação contínua, quantificando fenômenos da natureza e grandezas analógicas e contínuas, enquanto **dispositivos digitais** representam e operam sobre dados discretos ou dígitos.

<br>

**Codificação Binária**

**Bit** (**BI**nary digi**T**):
-  representa dois estados possíveis (0 e 1);
-  a combinação de bits permite armazenar um número maior de estados;

| 1 bit | 2 bits | 3 bits | 4 bits |
| --- | --- | --- | --- |
|0 <br> 1 | 00 <br> 01 <br> 10 <br> 11 | 000&nbsp; 100 <br> 001&nbsp; 101 <br> 010&nbsp; 110 <br> 011&nbsp; 111 | 0000 &nbsp;1000 &nbsp;0100 &nbsp;1100 <br> 0001&nbsp; 1001&nbsp; 0101&nbsp; 1101 <br> 0010&nbsp; 1010&nbsp; 0110&nbsp; 1110 <br> 0011&nbsp; 1011&nbsp; 0111&nbsp; 1111 |

<br>

**Byte** (**B**inar**Y** **TE**rm):
- unidade básica de armazenamento em memória e disco de computadores;
- composto por 8 bits;

<br>

**Palavras** são combinações que podem ser formadas por um grupo de 2, 4, 6 ou 8 bytes dependendo do modelo do computador. 

<br>

**Codificação Binária: Texto**

**EBCDIC**: 8 bits por caractere;  
**ASCII**: 7 bits por caractere, mais um bit de paridade para detecção de erros;  
**Unicode**: 16 bits por caractere;  
**UTF-8**: 32 bits por caractere;

<br>

**Codificação Binária: Imagem**

**Pixel**:  
&nbsp;&nbsp;&nbsp;&nbsp;menor componente de uma imagem digital;  
&nbsp;&nbsp;&nbsp;&nbsp;a quantidade de pixels em uma área determina a resolução da imagem;  
&nbsp;&nbsp;&nbsp;&nbsp;geralmente é representado pelo grau de participação de cada cor básica (RGB);

**Bitmap**:  
&nbsp;&nbsp;&nbsp;&nbsp;coleção de pixels de uma imagem;  
&nbsp;&nbsp;&nbsp;&nbsp;uma das mais diretas representações gráficas;  
&nbsp;&nbsp;&nbsp;composto pelos valores de cor dos pixels dispostos da esquerda para a direita de cima para baixo;

**Outros formatos**:  
Arquivos bitmap são muito pesados, fazendo necessário o uso de compressão das imagens em outros formatos.  
&nbsp;&nbsp;**GIF**:  
&nbsp;&nbsp;&nbsp;&nbsp;cada imagem pode ser composta por diferentes conjuntos de cores;  
&nbsp;&nbsp;&nbsp;&nbsp;permite imagens em movimento;  
&nbsp;&nbsp;**JPEG**:  
&nbsp;&nbsp;&nbsp;&nbsp;considerado superior para imagens coloridas;  
&nbsp;&nbsp;&nbsp;&nbsp;armazena a média das nuances de cores em curtas distâncias;
&nbsp;&nbsp;&nbsp;&nbsp;sistema de compressão razoavelmente complicado;

<br>

**Codificação Binária: Som**

A codificação binária de arquivos de som ocorre através do método **PCM** (pulse-code modulation), que transforma o sinal analógico de áudio em uma sequência de valores discretos, convertidos para a representação binária.

<br>

### Sistemas de numeração e conversão de bases

<br>

**Sistemas de Numeração**

| Binário (base 2) | Octal (base 8) | Decimal (base 10) | Hexadecimal (base 16) |
| --- | --- | --- | --- |
| **0** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1000 <br> **1** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1001 <br> 10 &nbsp;&nbsp;&nbsp;&nbsp; 1010 <br> 11 &nbsp;&nbsp;&nbsp;&nbsp; 1011 <br> 100 &nbsp;&nbsp; 1100 <br> 101 &nbsp;&nbsp; 1101 <br> 110 &nbsp;&nbsp; 1110 <br> 111 &nbsp;&nbsp; 1111 | **0** &nbsp;&nbsp; 10 <br> **1** &nbsp;&nbsp; 11 <br> **2** &nbsp;&nbsp; 12 <br> **3** &nbsp;&nbsp; 13 <br> **4** &nbsp;&nbsp; 14 <br> **5** &nbsp;&nbsp; 15 <br> **6** &nbsp;&nbsp; 16 <br> **7** &nbsp;&nbsp; 17 <br> | **0** &nbsp;&nbsp; **8** <br> **1** &nbsp;&nbsp; **9** <br> **2** &nbsp;&nbsp; 10 <br> **3** &nbsp;&nbsp; 11 <br> **4** &nbsp;&nbsp; 12 <br> **5** &nbsp;&nbsp; 13 <br> **6** &nbsp;&nbsp; 14 <br> **7** &nbsp;&nbsp; 15 <br> | **0** &nbsp;&nbsp; **8** <br> **1** &nbsp;&nbsp; **9** <br> **2** &nbsp;&nbsp; **A** <br> **3** &nbsp;&nbsp; **B** <br> **4**  &nbsp;&nbsp;  **C** <br> **5** &nbsp;&nbsp; **D** <br> **6** &nbsp;&nbsp; **E** <br> **7** &nbsp;&nbsp; **F** <br> |

<br>

**Conversão de Base**

**Para base decimal**

$$
(a_n a_{n-1} ... a_0, a_{-1} a_{-2} ... a_{-m})\\  
a_n * x^n + a_{n-1} * x^{n-1} + ... a_0 * x^0 + a_{-1} + a_{-2} * x^{-2} + ... + a_{-m} * x^{-m}
$$

Exemplos:

$$
(1011)_b = 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 1*2^0\\
1 * 8 + 0 * 4 + 1 * 2 + 1 * 1 = 11 
$$

$$
(230,4)_8 = 2 * 8^2 + 3 * 8^1 + 0 * 8^0 + 4 * 8^{-1}\\
2 * 64 + 3 * 8 + 0 * 1 + 4 * \frac{1}{8} = 152,5 
$$

<br>

**A partir da base decimal**

- **Parte inteira**:  
   divide-se sucessivamente o valor pela base x;  
   considera-se o valor do resto;  
   o resultado é obtido de baixo para cima;

$$
53_d = x_b\\
$$

$$
53 \lfloor2 \quad| 1\\
26 \lfloor2 \quad| 0\\
13 \lfloor2 \quad| 1\\
6 \lfloor2 \;\;\quad| 0\\
3 \lfloor2 \;\;\quad| 1\\
1 \lfloor2 \;\;\quad| 1\\
0 \;\;\;\;\;\;\;\;\;
$$

$$
53_d = 110101_b
$$

<br>

- **Parte fracionária**:  
  multiplica-se sucessivamente o número fracionário pela base;  
  considera-se o número inteiro do resultado da multiplicação;   
  o resultado é obtido de cima para baixo;

$$
0,3_d = x_b
$$

$$
0,3 * 2 = 0,6 \quad | 0 \\
0,6 * 2 = 1,2 \quad | 1 \\
0,2 * 2 = 0,4 \quad | 0 \\
0,4 * 2 = 0,8 \quad | 0 \\
0,8 * 2 = 1,6 \quad | 1 \\
0,6 * 2 = 1,2 \quad | 1 \\
$$

$$
0,3_d = 0,010011..._b
$$

<br>

**Codificação Binária: Números Inteiros**

Para representar um valor inteiro na base decimal como um número binário de tamanho N (quantidade de bits), precisamos representar:
- valor 0;
- 2<sup>N-1</sup> valores negativos;
- 2<sup>N-1</sup> – 1 valores positivos;

Existem duas alternativas para a codificação binária de valores inteiros negativos, a **notação de excesso** e a **notação de complemento de dois**. Ambas usam o valor do primeiro bit como indicador de sinal.

- **Notação de Excessos**:  
0 para valores negativos;  
1 para valores positivos; 

<br>

| Negativos | | Positivos | |
| --- | --- | --- | --- |
| 0000 | -8 | 1000 | 0 |
| 0001 | -7 | 1001 | 1 |
| 0010 | -6 | 1010 | 2 |
| 0011 | -5 | 1011 | 3 |
| 0100 | -4 | 1100 | 4 |
| 0101 | -3 | 1101 | 5 |
| 0110 | -2 | 1110 | 6 |
| 0111 | -1 | 1111 | 7 |

<br>

- **Notação de Complemento de Dois**:  
0 para valores positivos;  
1 para valores negativos;

<br>

| Positivos | | Negativos | |
| --- | --- | --- | --- |
| 0000 | 0 | 1000 | -8 |
| 0001 | 1 | 1001 | -7 |
| 0010 | 2 | 1010 | -6 |
| 0011 | 3 | 1011 | -5 |
| 0100 | 4 | 1100 | -4 |
| 0101 | 5 | 1101 | -3 |
| 0110 | 6 | 1110 | -2 |
| 0111 | 7 | 1111 | -1 |

<br>