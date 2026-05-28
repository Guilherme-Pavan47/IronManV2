import pygame
import random
from recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador

limpar_tela()
inicializarBancoDeDados()
nome_maior, maior_pontos, dataJogada = maior_pontuador()
pygame.init()

while True:
    nome = input("Informe o Nome do Competidor:")
    if len(nome) > 0: 
        break
    else:
        print("Nome Inválido!")
        
tamanho = (1000,700)
pygame.display.set_caption("CJ POR LOCO")
icone  = pygame.image.load("base/iconeMulher.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
branco = (255, 255, 255)
preto = (0, 0, 0)

fundo = pygame.image.load("base/gtasa.jpg")
fundoDead = pygame.image.load("base/seFodeu1.jpg")
fundoStart = pygame.image.load("base/imagemInicialGta1.jpg")

iron = pygame.image.load("base/cj1.png")
iron = pygame.transform.scale(iron, (116,51))
missel = pygame.image.load("base/municao.png")
missel = pygame.transform.scale(missel, (125,50))
missileSound = pygame.mixer.Sound("base/tiro.mp3")
explosaoSound = pygame.mixer.Sound("base/fraseDeMorteCj.mp3")
pygame.mixer.music.load("base/musicaDeFundoGta.mp3")
fonteMenu = pygame.font.SysFont("comicsans",18)

def jogar():
    global pausado
    pausado = False
    posicaoXPersona = 0
    posicaoYPersona = 60
    movimentoYPersona = 0
    velocidadeMovPersona = 5
    posicaoXMissel = 800
    posicaoYMissel = 100
    velocidadeMissel = 2
    pontos = 0
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    dificuldade = 20

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                movimentoYPersona = -velocidadeMovPersona
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                movimentoYPersona = velocidadeMovPersona
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
                movimentoYPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
                movimentoYPersona = 0
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                pausado = not pausado
                if pausado:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

        if pausado:
            fontePausa = pygame.font.SysFont("comicsans", 72, bold=True)
            textoPausa = fontePausa.render("PAUSE", True, (255, 215, 0))
            tela.blit(fundo, (0, 0))
            tela.blit(textoPausa, (tamanho[0]//2 - textoPausa.get_width()//2, tamanho[1]//2 - textoPausa.get_height()//2))
            pygame.display.update()
            relogio.tick(60)
            continue

        posicaoYPersona = posicaoYPersona + movimentoYPersona
        if posicaoYPersona < 0:
            posicaoYPersona = 0
        elif posicaoYPersona > 649:
            posicaoYPersona = 649

        posicaoXMissel = posicaoXMissel - velocidadeMissel
        if posicaoXMissel < -125:
            pygame.mixer.Sound.play(missileSound)
            posicaoXMissel = 800
            pontos = pontos + 1
            velocidadeMissel = velocidadeMissel + 1
            posicaoYMissel = random.randint(0, 675)

        tela.fill(branco)
        tela.blit(fundo, (0, 0))
        tela.blit(iron, (posicaoXPersona, posicaoYPersona))
        tela.blit(missel, (posicaoXMissel, posicaoYMissel))
        texto = fonteMenu.render("Pontos: " + str(pontos), True, branco)
        tela.blit(texto, (700, 15))
        fonteDica = pygame.font.SysFont("comicsans", 14)
        textoDica = fonteDica.render("Press Space to Pause Game", True, (200, 200, 200))
        tela.blit(textoDica, (700, 40))

        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona + 116))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona + 51))
        pixelsMisselX = list(range(posicaoXMissel, posicaoXMissel + 125))
        pixelsMisselY = list(range(posicaoYMissel, posicaoYMissel + 25))
        if len(list(set(pixelsMisselY).intersection(set(pixelsPersonaY)))) > dificuldade:
            if len(list(set(pixelsMisselX).intersection(set(pixelsPersonaX)))) > dificuldade:
                escreverDados(nome, pontos)
                dead()
            else:
                print("Ainda Vivo, mas por pouco!")
        else:
            print("Ainda Vivo")

        pygame.display.update()
        relogio.tick(60)

def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    larguraButtonStart = 649
    alturaButtonStart  = 40
    
    
    while True:
        for evento in pygame.event.get():
            
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35
                

                
            elif evento.type == pygame.MOUSEBUTTONUP:
                
                if startButton.collidepoint(evento.pos):
                    
                    larguraButtonStart = 649
                    alturaButtonStart  = 40
                    jogar()
                

                
            
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        startButton = pygame.draw.rect(tela, branco, (10,10, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (25,12))

        pygame.display.update()
        relogio.tick(60)



def bemVindo():
    larguraButtonStart = 200
    alturaButtonStart  = 50
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 190
                    alturaButtonStart  = 45
            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 200
                    alturaButtonStart  = 50
                    jogar()
                    
    

        tela.blit(fundoStart, (0, 0))

       
        fonteTitulo = pygame.font.SysFont("comicsans", 42, bold=True)
        fonteNormal = pygame.font.SysFont("comicsans", 22)
        fontePequena = pygame.font.SysFont("comicsans", 18)

        titulo = fonteTitulo.render("Bem-vindo ao Jogo!", True, branco)
        tela.blit(titulo, (tamanho[0]//2 - titulo.get_width()//2, 60))

        
        textoNome = fonteNormal.render(f"Jogador: {nome}", True, (148, 0, 211))
        tela.blit(textoNome, (tamanho[0]//2 - textoNome.get_width()//2, 150))

        
        mecanica = [
            "Como jogar:",
            "- Use as setas CIMA e BAIXO para mover o personagem.",
            "- Desvie dos mísseis que vêm em sua direção.",
            "- Cada míssil desviado vale 1 ponto.",
            "- A velocidade aumenta a cada míssil desviado.",
            "- O jogo termina quando você for atingido!"
        ]
        for i, linha in enumerate(mecanica):
            cor = (0, 0, 255) if i == 0 else (0, 0, 255)
            textoLinha = fonteNormal.render(linha, True, cor)
            tela.blit(textoLinha, (tamanho[0]//2 - textoLinha.get_width()//2, 230 + i * 35))

        
        pygame.draw.line(tela, (100, 100, 100), (100, 460), (900, 460), 2)
        textoMelhor = fontePequena.render(
            f"🏆 Melhor Jogador: {nome_maior}  |  Pontos: {maior_pontos}  |  Data: {dataJogada}",
            True, (255, 0, 0)
        )
        tela.blit(textoMelhor, (tamanho[0]//2 - textoMelhor.get_width()//2, 480))

        
        startButton = pygame.draw.rect(
            tela, (0, 180, 0),
            (tamanho[0]//2 - larguraButtonStart//2, 560, larguraButtonStart, alturaButtonStart),
            border_radius=20
        )
        startTexto = fonteNormal.render("Iniciar Partida", True, branco)
        tela.blit(startTexto, (tamanho[0]//2 - startTexto.get_width()//2, 570))

        pygame.display.update()
        relogio.tick(60)
           
bemVindo()