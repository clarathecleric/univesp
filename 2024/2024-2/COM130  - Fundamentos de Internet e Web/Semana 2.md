#### COM130 - Fundamentos de Internet e Web

## 2. Protocolos fundamentais às aplicações Web

### 2.1. Protocolos de comunicação da internet

**A importância dos protocolos de comunicação**

De forma geral, protocolos são conjuntos de procedimentos que devem ser seguidos para concluir um determinado processo ou atingir alguma finalidade. Eles estão presentes, mesmo que despercebidos, na vida cotidiana.

No contexto da computação, os **protocolos de comunicação** permitem que a conexão entre dois dispositivos ocorra de forma efetiva e confiável, uma vez que a sua ausência possa resultar em incompatibilidades, perda de conteúdo ou interceptação de dados por terceiros.

<br>

**O que é um protocolo?**

*"Um protocolo define o **formato** e a **ordem** das mensagens trocadas entre duas ou mais entidades comunicantes, bem como as ações realizadas na transmissão e/ou recepção dessas mensagens”.*
<div style="text-align: right"> (KUROSE, ROSS, 2021) </div>
<br>

Todo protocolo considera o serviço a ser oferecido, o ambiente onde é executado (incluindo os serviços utilizados pelo próprio protocolo), o vocabulário utilizado para implementá-lo, o formato de cada mensagem do vocabulário e os algoritmos que tentam garantir a troca de tais mensagens e a integridade do serviço oferecido.

Em resumo, protocolos são as padronizações que definem como ocorre a comunicação e utilização do meio físico na infraestrutura da rede, considerando a **semântica** (regras) e **sintaxe** (formato).

<br>

**Procolos fundamentas para a comunicação da internet**

A comunicação de aplicações que utilizam a internet ocorre através de diversos protocolos que variam em sua proximidade ao usuário. Cada uma das camadas da comunicação conta com um ou mais protocolos com base no modelo do qual faz parte. 

A internet é composta por uma miríade de protocolos que realizam funções específicas, dentre eles temos o **HTTP** (HyperText Transfer Protocol) para navegação na web, o **FTP** (File Transfer Protocol) para transferência de arquivos e o **SMTP** (Simple Mail Transfer Protocol) para envio de e-mails. Entretanto, o conjunto de protocolos **TCP/IP** visto anteriormente é o mais prevalente entre eles.

O **IP** (Internet Protocol) opera na camada de rede do modelo TCP/IP, que é responsável pelo **endereçamento lógico**, **determinação de rotas** e **comutação de pacotes de dados**, assim abrangendo toda a comunicação host a host. Ele não estabelece uma conexão na camada de rede, usando roteadores que se utilizam informações de protocolo para encaminhas pacotes/datagramas entre origem e destino. Vale lembrar que o IP não garante a integridade dos dados durante a transmissão, sendo considerado um serviço de melhor esforço quando comparado a outros protocolos.

Já o **TCP** (Transmission Control Protocol) opera na camada de transporte, que é responsável por **aceitar os dados** da camada de aplicação e **dividi-los em unidades menores** se necessário, além de **garantir que todas essas unidades cheguem corretamente ao destino**. O protocolo é responsável pela entrega dos dados sem erros, sem perdas e na ordem correta de forma eficiente, garantindo que as camadas superiores fiquem isoladas das mudanças de tecnologia de hardware. Dá-se o nome de **entidade de transporte** ao hardware/software que executa as funções da camada de transporte e de **segmento** às unidades de dados por ela trocadas.

Diferente da camada de rede, a camada de transporte conecta a origem ao destino, sendo considerada uma camada fim a fim. Ela permite que um programa da máquina de origem "mantenha uma conversa" com um programa semelhante na máquina de destino através de cabeçalhos e mensagens de controle. Esse processo também é chamado de **comunicação lógica**.

Por fim, temos o **UDP** (User Datagram Protocol), considerado um protocolo da internet "simplificado". Tal como o TCP, ele atua na camada de transporte, mas prioriza a velocidade e eficiência da comunicação em detrimento da integridade dos dados envolvidos. Como o IP, é considerado um protocolo de "melhor esforço" que não estabelece uma conexão entre o emissor e o receptor, e pode entregar dados incompletos ou fora de ordem. Cada segmento do UDP é tratado de forma independente dos outros. Seu uso reside principalmente em aplicações cuja comunicação de dados ágil é imprescindível, com maior tolerância a ocasional perda de dados.