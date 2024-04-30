#### COM130 - Fundamentos de Internet e Web

## 4. Linguagem de marcação: HTML

### 4.1. Linguagens de marcação para web

Uma **página** é uma unidade básica de um site que pode ser acessada através de um navegador. Elas geralmente são criadas e armazenadas em servidores web, sendo acessíveis através de seus endereços URL exclusivos. Entre os elementos que podem estar presentes em uma página web temos texto, imagens, vídeos, links, assim como outros conteúdos multimídia. Elas geralmente são construídas usando **linguagens de marcação**, sendo HTML a mais comum.

O **HTML** (Hyper Text Markup Language) consiste em um conjunto de comandos (**tags**) usados para identificar e estruturar os diferentes elementos de uma página.

```
<html>  
    <head>  
        <title>Exemplo</title>
    </head>  
    <body> Eu sou um exemplo.  
        <p><a href="teste.html"> Eu sou um link</a></p>  
        </body>  
</html>
```

Abaixo estão alguns exemplos de tags HTML:


| tag | descrição |
| --- | --- |
| **\<html>** |	Define o início e o fim do documento HTML |
| **\<head>** |	Define a seção de cabeçalho do documento HTML |
| **\<title>**	| Define o título do documento |
| **\<body>** | Define o corpo do documento HTML|
| **\<h1>-\<h6>** | Define cabeçalhos de diferentes níveis
| **\<p>** | Define um parágrafo |
| **\<a href ="?">** | Define um hyperlink |
| **\<img scr="?">** | Define uma imagem |
| **\<table>** | Define uma tabela |
| **\<tr>** | Define uma linha em uma tabela |
| **\<th>**	| Define um cabeçalho de célula em uma tabela |
| **\<td>**	| Define uma célula de dados em uma tabela |

Algumas tags podem ser usadas para manipular diretamente a formatação de texto:

| tag | descrição |
| --- | --- |
| **\<b>** | negrito |
| **\<i>** | itálico |
| **\<u>** | sublinhado |
| **\<font size=?>** | tamanho da fonte |
| **\<font color=?>** | cor da fonte |