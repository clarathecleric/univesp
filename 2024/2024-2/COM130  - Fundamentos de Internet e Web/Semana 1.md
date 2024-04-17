#### COM130 - Fundamentos de Internet e Web

## 1. Conceitos de redes de computadores

### 1.1. Introdução às redes de computadores


A ***internet*** é uma rede de computadores que conecta bilhões de dispositivos ao redor do mundo, sejam computadores, *smarthphones*, *tablets*, ou dispositivos não tradicionais, como TVs, consoles, sistemas de segurança, etc. Tal conexão permite o compartilhamento de diferentes tipos de dados e o acesso às mais diversas aplicações pertencentes a inúmeros setores.

<br>

**Componentes de rede**

Dentre os elementos que compõe a rede de computadores temos: suários, aplicações, roteadores, switches, servidores, meios físicos de comunicação, links, celulares, tablets e desktops.

Para que um dispositivo, denominado **hospedeiro** ou **sistema final**, possa se conectar à internet, ele precisa de uma **placa de rede** responsável por transmitir os **sinais de comunicação** através de um meio físico (via cabo ou não). A placa, por sua vez, precisa estar conectada a um **elemento de comutação**, como um **roteador** ou **switch**, que então então encaminha os dados para o seu devido receptor, esteja ele na mesma rede ou não. 

Vale ressaltar que os sinais de comunicação são interpretados tanto pelo emissor quanto pelo receptor, permitindo assim que as informações sejam apresentadas aos usuários das aplicações.

<br>

**Arquitetura em camadas**

A **arquitetura em camadas** consiste na estruturação da série de processos que compõe a comunicação entre as redes de computadores em camadas lógicas. Assim, a complexidade de todo o processo e seus inúmeros elementos pode ser decomposta em camadas específicas que são responsáveis por funções específicas, assim simplificando-o. Entre seus principais modelos temos o **OSI** (Open Systems Interconnection) e o **TCP/IP** (Transmission Control Protocol/Internet Protocol), que se diferem na quantidade e especificidade das camadas.

<br>

**Modelos de camadas**

**OSI**

O modelo OSI, criado em 1971, é reconhecido como um modelo de referência, nunca tendo sido implementado. Ele é composto por sete camadas distintas.

1. **Camada física:** transmite bits de dados por meio de um meio físico

2. **Camada de enlace de dados:** estabelece e mantém a comunicação entre dois dispositivos conectados diretamente, garantindo a integridade dos dados

3. **Camada de rede:** encaminha os dados entre diferentes redes, utilizando protocolos de roteamento

4. **Camada de transporte:** garante a entrega dos dados de forma confiável e ordenada, utilizando protocolos como TCP ou UDP

5. **Camada de sessão:** estabelece e manter sessões de comunicação entre dispositivos

6. **Camada de apresentação:** realiza a conversão de dados entre formatos diferentes

7. **Camada de aplicação:** fornece serviços de comunicação específicos para as aplicações

<br>

**TCP/IP**

Já o modelo TCP/IP, que compõe grande parte da internet, conta apenas com quatro camadas.

1. **Camada de Interface de Rede (ou Camada de Acesso à Rede):** Transmite os pacotes de dados entre os dispositivos da rede local (LAN) e traduz os pacotes em sinais elétricos, ópticos ou de rádio. Geralmente é implementada por hardware, como placas de rede e switches.

2. **Camada de Internet (ou Camada de Rede):** Encaminha os pacotes de dados entre redes distintas, utilizando endereçamento IP e protocolos de roteamento, como o protocolo IP (Internet Protocol).

3. **Camada de Transporte:** Garante a entrega confiável dos dados e controla a quantidade de dados enviados em cada transmissão. É composta por dois protocolos principais: **TCP** (Transmission Control Protocol), que garante a entrega confiável dos dados, e **UDP** (User Datagram Protocol), que é utilizado quando a velocidade da transmissão é mais importante do que a confiabilidade.

4. **Camada de Aplicação:** Fornece serviços de comunicação para as aplicações, como email, navegação web, transferência de arquivos, entre outros. Inclui uma grande variedade de protocolos, como HTTP, FTP, SMTP, DNS e muitos outros.

<Br>

**A internet e suas aplicações**

A internet é uma rede de computadores que conecta milhões de dispositivos (também chamados de hospedeiros) por todo o mundo. Tais **hospedeiros** são interconectados por **enlaces de comunicação** (fibra óptica, ondas de rádio, satélite, etc.), cuja **taxa de transmissão** é medida pela **largura da banda** (quantidade de dados que pode ser transmitida por segundo). Para garantir a integridade dos dados, a internet faz o uso de **roteadores** que encontram a melhor **rota** de encaminhamento e transferem os **pacotes** ("pedaços" de dados) entre os hospedeiros até o seu destino final. O processo é gerenciado por **procolos de rede**, que definem as regras de envio e recebimento de dados na internet.

Atualmente, as aplicações que funcionam na internet são companheiras constantes da maioria da população. Dentre elas temos serviços de e-mail, *streaming*, compartilhamento de arquivos, sistemas bancários, etc.. É importante lembrar que algumas dessas aplicações são anteriores ao surgimento da WWW (World Wide Web) e podem ser usados fora dela.

<br>

**Internet e WWW**

A **World Wide Web**, WWW ou apenas Web, é um sistema de documentos em hipermídia que são interligados por uma rede de computadores, geralmente a internet. Ela permite o acesso em interação com os mais diversos conteúdos através de **navegadores**, ou browsers, como Google Chrome, Mozilla Firefox, etc.