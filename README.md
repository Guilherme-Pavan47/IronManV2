## Guilherme Luiz Pavan Vial RA: 1139397
## Lorenzo Martinelli Pomatti RA: 1139572

## História

## As ruas de Los Santos nunca foram fáceis, mas essa noite está diferente. CJ, o lendário morador do Grove Street, se viu no lugar errado na hora errada. Enquanto caminhava pela cidade, os inimigos avistaram ele e abriram fogo sem piedade — mísseis e balas cruzando o céu noturno em sua direção. Sem arma, sem carro e sem saída, CJ só tem uma opção: correr e desviar. A cada tiro que passa, a adrenalina aumenta. A cada segundo que sobrevive, os inimigos ficam mais rápidos e mais furiosos. A lua cheia ilumina a cidade enquanto um avião passa silencioso no céu — indiferente ao caos lá embaixo.

## Até quando CJ vai aguentar?
## Desvie. Sobreviva. Seja o maior pontuador de Los Santos.


## Tecnologias Utilizadas: 

## Python 3.14
## Linguagem principal do projeto. Responsável por toda a lógica do jogo, controle de fluxo, funções e estrutura do código.

## Pygame-CE 2.5.7
## Biblioteca principal para desenvolvimento do jogo. Utilizada para:
## Criar e gerenciar a janela do jogo
## Renderizar imagens, personagens e cenários na tela
## Capturar eventos do teclado e mouse
## Reproduzir sons e música de fundo
## Controlar os FPS com o Clock
## Detectar colisão entre o personagem e os mísseis


## Pyttsx3
## Biblioteca de síntese de voz. Utilizada para narrar em voz alta o nome do maior pontuador e a pontuação ao final de cada partida, tornando o game over mais dramático e imersivo.

## JSON
## Formato de arquivo utilizado para salvar e carregar o histórico de partidas no arquivo log.dat. Armazena nome do jogador, pontuação, data e hora de cada jogo disputado.

## Os
## Módulo nativo do Python utilizado para limpar o terminal antes do jogo iniciar, compatível tanto com Windows (cls) quanto com Linux/Mac (clear).

## Data e Hora
## Módulo nativo do Python utilizado para registrar automaticamente a data e hora exata de cada partida jogada, exibindo essas informações no ranking.

## Time
## Módulo Python nativo usado para criar pausas no código, como a contagem regressiva de 3, 2, 1 exibida antes de cada partida começar.

## Math
## Módulo nativo do Python utilizado para calcular os ângulos da curva de Bézier, permitindo que o avião de fundo rotacione suavemente conforme percorre sua trajetória no céu.

## Curva de Bézier (algoritmo matemático)
## Algoritmo matemático implementado manualmente no jogo para definir a trajetória curva do avião que atravessa o céu como elemento de paisagem, dando mais realismo e profundidade ao cenário.

## Random
## Módulo nativo do Python utilizado para gerar posições aleatórias no eixo vertical para cada míssil disparado. A cada tiro que passa pela tela, o próximo aparece em uma altura diferente e imprevisível, tornando o jogo mais desafiador e imprevisível a cada rodada.