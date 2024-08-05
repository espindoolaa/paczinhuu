# PACZINHUU
* IMAGEM COMO CAPA *

## Desenvolvedores do projeto
- Alisson Vinicius (avap2)
- José Francisco (jfcn3)
- Marina Rodas (mrs5)
- Mateus Espíndola (meb)
- Matheus Vieira (mbcv)

## Sobre o jogo
  
O PACZINHUU tem por inspiração o jogo Pac-Man, especialmente em sua mecânica, mas traz como elementos principais algumas referências da cidade do Recife. Assim, tentando trazer as inspirações recifenses para o projeto, o "come-come" dá lugar para o famoso humorista local, Ítalo Sena, e os famosos fantasminhas (Pinky, Inky, Blinky e Clyde) se transformam nos protagonistas dos mares de Recife: os tutubas 🦈.

Quanto à mecânica do jogo e aos seus elementos, subdividiu-se em dois grupos, os quais se tratam dos objetos coletáveis e não coletáveis. Para uma melhor visualização deles, tomemos como referência de análise a imagem a seguir: 

- INSERIR IMAGEM DO JOGO - 

Coletáveis
- **Peixe:** Ao serem coletados, além de conferir um aumento na pontuação no contador de peixes, também conferem a Ítalo um aumento de velocidade (de x pixels/s para y pixels/s).
- **Baiacu:** Embora não tão comuns no litoral de Recife, por algumas loucuras que acompanham as mudanças climáticas, eles vieram parar em Pernambuco! Esse coletável, além de conferir um aumento na pontuação no contador de baiacus, também conferem a Ítalo o estado de _**fúria**_. Quando Ítalo está em _**fúria**_, ele adquire temporariamente habilidades de um exímio caçador de tubarões, tornando os tutubas apenas peixinhos indefesos. Nessa condição, Ítalo tem sua velocidade aumentada (de x pixels/s para y pixels/s) e é capaz de matar os tubarões, enquanto os tubarões que fogem têm sua velocidade diminuída. Quando estes são mortos nessa fase, voltam para a região de início, esperando alguns segundos para retornarem ao jogo.
- **Bolhas do mar:** Juntam-se com os dois peixes e os dois baiacus para ocupar todo o mapa e são convertidos numa pontuação, quando coletados, no contador de bolhas.

**Não coletáveis**
- **Ítalo Sena:** Personagem principal e controlável, que será utilizado pelo player para atingir o objetivo de PACZINHUU.
- **Tubarões**: Dois deles serão gerados no mapa com o objetivo de atrapalhar Ítalo de completar sua meta principal. Em caso de colisão com o Ítalo sem estar em fúria, acaba com o jogo do personagem principal.
- **Boias:** Para criar uma espécie de labirinto na fase e delimitar o mapa, foram utilizadas boias de praia. 

## Organização do código 
Para elucidar melhor sobre a organização utilizada pelo grupo, segue a imagem do Spider Diagram criado. Pelo diagrama é possível ver a interação simultânea entre as diferentes classes que ocorre dentro do nosso código. 

![Spider Diagram Template (1)](https://github.com/user-attachments/assets/c5b3d844-6f97-40df-bf71-b1c5a91ed5a9)

- **main.py:** Nesse arquivo é onde tudo acontece: telas de menu inicial, da história do jogo, das instruções, do looping do jogo, da vitória e do game over são chamadas aqui.
- **classe_botoes.py:** Classe responsável pela criação de instâncias de botões na tela que, ao entrarem numa certa interação, mudam a tela do jogo. 
- **classe_baiacu.py:** Classe responsável pela criação dos objetos baiacu no jogo.
- **classe_bolha.py:** Classe responsável pela criação das bolhas do mar.
- **classe_italo.py:** Classe responsável pela criação do objeto Ítalo Sena.
- **classe_peixe.py:** Classe responsável pela criação do objeto Ítalo Sena.
- **classe_tubaroes.py:** Classe responsável pela criação do objeto Ítalo Sena.
- **constantes.py:** Arquivo que contém variáveis constantes que foram usadas no projeto, como o tamanho de tela, velocidade dos personagens, etc.  
- **labirinto.py:** Gera uma máscara de colisão na imagem das boias, evitando que o Ítalo e os tubarões saiam das delimitações.

## Ferramentas, Frameworks e Bibliotecas
Para a realização do projeto, utilizou-se de algumas ferramentas e bibliotecas que satisfazessem as necessidades para a criação de um jogo em 2D, com elementos em pixelart. 

**Ferramentas**
- **Canva:** Recurso de design que foi primordial na criação de todas as sprites dos elementos.
- **DALL-E:** Ferramenta de IA especializada em imagens que foi usada para a criação do plano de fundo do jogo em pixelart, trazendo a essência que nós queríamos para o cenário. 
- **VSCode:** A IDE utilizada para o desenvolvimento do projeto.
- **Notion:** Plataforma usada para o gerenciamento das atividades feitas ao longo do projeto.
- **Discord:** Plataforma de comunicação dos integrantes durante o projeto.
- **Miro:** A criação da organização do código em fluxograma.  

**Bibliotecas**

- **Pygame:** Essa biblioteca importa módulos Python projetados para o desenvolvimento de jogos, tal como funcionalidades para controle de eventos, manipulação de sons e criação de gráficos, - as quais facilitam o processo de criação de um jogo 2D.
- **Math:** Dessa biblioteca foi implementada a função **sqrt** no código com o intuito de calcular a distância entre duas instâncias de objetos e, assim, determinar se eles colidiram ou não. 
- **Sys:** A biblioteca sys foi implementada com o intuito de encerrar o programa corretamente, especificamente com a chamada de sys.exit().
- **Path:** Para uma melhor organização do projeto, separou-se todo código em vários arquivos ".py". Como consequência, para simplificar a navegação desses arquivos, foi implementada a função **Pathlib** da biblioteca. 

## Estrutura da equipe
Ao longo do projeto, todos os integrantes participaram, de alguma maneira, na concepção do jogo. Em relação aos papeis, todos tiveram suas funções específicas, mas também foram proativos em se ajudarem.

| Integrante | Funções específicas |
| :---:        |     :---      | 
| Alisson Vinicius (avap2)   | Ajustes na movimentação do player, sistema de colisão do player com as paredes e estruturação do mapa     | 
| José Francisco (jfcn3)   | Classe dos coletáveis, animação da personagem, ajuda no plano de jogo e no seu respectivo mapa, auxílio no projeto como um todo focado no frontend    |
| Marina Rodas (mrs5)   | Criação da classe dos botões, implementação do mecanismo de colisão, criação da arte das paredes e desenvolvimento das telas iniciais     |
| Mateus Espíndola (meb)   | Criação da classe tubarões, desenvolvimento da mecânica do jogo, criação da matriz do mapa, implementação dos coletáveis das bolhas e desenvolvimento do relatório  |
| Matheus Vieira (mbcv)   | Criação da classe do Ítalo, criação das placas que contam os coletáveis, desenvolvimento da lógica da classe do baiacu     |


## Conceitos que foram apresentados durante a disciplina e utilizados no projeto
Ao decorrer da estruturação lógica do jogo, todos os conceitos apresentados durante a disciplina foram imprescindíveis. Assim, todo o projeto envolve operações lógicas básicas, comandos condicionais para a realização de movimentação conforme a interação das classes e, especialmente, laços de repetição, os quais foram a essência para desempenhar um jogo. Ademais, a aprendizagem de programação orientada à objetos junta aos conceitos de listas, tuplas e dicionários foi fundamental, uma vez que possibilita a criação objetos no código e da sua manipulação, bem como os conhecimentos de modularização possibilitaram uma organização maior do projeto como um todo. 

## Desafios e aprendizados

Nossos maiores desafios foram, sem dúvidas, lidar com a divisão ineficiente das tarefas do projeto, a modularização do código, a utilização da biblioteca PyGame e, em especial, a compreensão e implementação do conteúdo de orientação a objetos, visto a inexperiência da equipe nesse tipo de projeto. Ao mesmo tempo, além de não conhecer as ferramentas de programação já citadas, também não era do conhecimento da equipe o Git/GitHub, que exigiu certo esforço do grupo para entender os conceitos e, assim, sermos capazes de estruturar melhor o código tendo o conhecimento de branches. 

Colocando em perspectiva o desenvolvimento do projeto, ficou muito claro que a nossa delegação de funções inicial, subdividida em classes para cada um integrante e sem reuniões periódicas, seria uma estratégia que não funcionaria e, provavelmente, exigiria muito esforço do grupo para juntar todo o trabalho posteriormente e garantir a coesão adequada. Tendo em vista tais dificuldades, redefinimos nossas estratégias de organização, e o projeto começou a fluir muito mais quando iniciamos a modularizar os códigos e a realizar reuniões diárias até a sua finalização. Assim, embora alguns empecilhos por falta de conhecimento (técnicos ou não) nosso tenham aparecido ao longo do nosso desenvolvimento, todos tiveram disposição e curiosidade para aprender, e solucionar os problemas juntos.

Por fim, é imprescindível dizer que, embora todo o estresse dos bugs que surgiram no caminho, foi um trabalho importantíssimo no nosso crescimento como futuros profissionais, uma vez que foi a primeira vez de todos trabalhando juntos num único projeto de programação a fim de entregar algo jogável e engraçado para a disciplina, como também fundamental na solidificação dos conceitos que aprendemos ao longo da disciplina, pondo em prática tudo que havíamos visto de maneira divertida. Agradecemos, especialmente, ao professor da disciplina, Juliano Iyoda, e a todos os monitores que fizeram esse projeto ser possível: César Cavalcanti, Thomaz Cabral e Welton Felix.

Esperamos que se divirtam com o PACZINHUU! :)

## [Link para a nossa apresentação]()

## Galeria do jogo








