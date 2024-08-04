# PACZINHUU
* IMAGEM COMO CAPA *

## Desenvolvedores do projeto
- Alisson Vinicius (avap2)
- José Francisco (jfcn3)
- Marina Rodas (mrs5)
- Mateus Espíndola (meb)
- Matheus Vieira (mbcv)

## Sobre o jogo
  
O PACZINHHU tem por inspiração o jogo Pac-Man, especialmente em sua mecânica, mas trazendo como elementos seus principais algumas referências da cidade do Recife. Assim, tentando trazer as inspirações recifenses para os projetos, o "come-come" dá lugar para o famoso humorista local, o Ítalo Sena, e os famosos fantasminhas (Pinky, Inky, Blinky e Clyde) se transformam nos protagonistas dos mares de Recife: os tutubas 🦈.

Quanto à mecânica do jogo e aos seus elementos, há uma subdivisão em dois grupos, os quais se tratam dos objetos coletáveis e não coletáveis. Para uma melhor visualização deles, tomemos como referência de análise a imagem a seguir.  

- INSERIR IMAGEM DO JOGO - 

Coletáveis
- **Peixes:** Ao serem coletados, além de conferir um aumento na pontuação no contador de peixes, também dão à Ítalo tem sua velocidade aumentada (de x pixels/s para y pixels/s).
- **Bolhas do mar:** Juntam-se com os quatro peixes para ocupar todo o mapa e são convertidos numa pontuação, quando coletados, no contador de bolhas.
- **Baiacu:** Embora não tão comuns no litoral de Recife, por algumas loucuras que acompanham as mudanças climáticas, eles vieram para em Pernambuco! Esse coletável, além de conferir um aumento na pontuação no contador de baiacus, também dão à Ítalo o estado de _**fúria**_. Quando Ítalo estiver em _**fúria**_, adquire momentaneamente habilidades de exímio caçador de tubarões, tornando os tutubas apenas peixinhos indefesos. Nessa condição, Ítalo tem sua velocidade aumentada (de x pixels/s para y pixels/s) e é capaz de matar os tubarões, enquanto os tubarões que fogem têm sua velocidade diminuída. Quando esses são mortos nessa fase, voltam para a região de início, esperando alguns segundos para retornarem ao jogo.

Não coletáveis
- **Ítalo sena:** Personagem principal e controlável, que será utilizado pelo player para atingir o objetivo do PACZINHUU.
- **Tubarões**: Dois deles serão gerados no mapa com o objetivo de atrapalhar Ítalo de completar sua meta principal. Em caso de colisão com o Ítalo sem estar em fúria, acaba com o jogo do personagem principal.
- **Boias:** Para criar uma espécie de labirinto na fase e delimitar o mapa, foram utilizadas boias de praia. 

## Organização do código 
- criação do esquema

## Ferramentas, Frameworks e Bibliotecas
Para a realização do projeto, utilizou-se de algumas ferramentas e bibliotecas que satisfazessem as necessidades para a criação de um jogo em 2D, com elementos em pixelart. 


- Canva: Recurso de design que foi primordial na criação de todas as sprites dos elementos.
- DALL-E: Essa ferramenta de criação de imagens foi utilizada para a criação do plano de fundo do jogo em pixelart, trazendo a essência que nós queríamos para o cenário. 
- VsCode: A IDE usada para o desenvolvimento do projeto.
- Notion: Plataforma usada para o gerenciamento das atividades feitas ao longo do projeto.
- Discord: Plataforma de comunicação dos integrantes durante o projeto.
- Miro: A criação da organização do código em fluxograma.  

Bibliotecas

Pygame: Essa biblioteca importa módulos Python projetados para o desenvolvimento de jogos, tal como funcionalidades para controle de eventos, manipulação de sons e criação de gráficos, as quais facilitam o processo de criação de um jogo 2D.
Math: Dessa biblioteca foi implementada a função **sqr** no código com o intuito de calcular a distância entre duas instâncias de objetos e, assim,,determinar se eles colidiram ou não. 
Sys: A biblioteca sys foi implementada com o intuito de encerrar o programa corretamente, especialmente com a chamada de sys.exit().
Path: Para uma melhor organização do projeto, separou-se todo código em vários arquivos ".py". Como consequência, para simplificar a navegação desses arquivos, foi implementada a função pathlib da biblioteca. 

## Estrutura da equipe
Ao longo do projeto, todos os integrantes participaram, de alguma maneira, na concepção do jogo. Em relação aos papeis, todos tiveram suas funções específicas, mas também foram proativos em se ajudarem.

| Integrante | Funções específicas |
| :---:        |     :---      | 
| Alisson Vinicius (avap2)   | -     | 
| José Francisco (jfcn3)   | -     |
| Marina Rodas (mrs5)   | -     |
| Mateus Espíndola (meb)   | Criação da classe tubarões, desenvolvimento da mecânica do jogo, criação da matriz do mapa e implementação dos coletáveis das bolhas  |
| Matheus Vieira (mbcv)   | -     |


## Conceitos que foram apresentados durante a disciplina e utilizados no projeto

- poo 

## Desafios e aprendizados
- ver o que fizemos ao longo das planilhas


## Link para a nossa apresentação

## Galeria do jogo








