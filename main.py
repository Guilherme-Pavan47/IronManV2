import pygame
import random
import pyttsx3
from recursos.funcoes import (
    inicializarBancoDeDados,
    limpar_tela,
    escreverDados,
    maior_pontuador,
)

# ── Inicialização geral ────────────────────────────────────────────────────────
limpar_tela()
inicializarBancoDeDados()

nome_maior, maior_pontos, dataJogada, horaJogada = maior_pontuador()

pygame.init()

while True:
    nome = input("Informe o Nome do Competidor: ")
    if len(nome) > 0:
        break
    else:
        print("Nome Inválido!")

tamanho = (1000, 700)
pygame.display.set_caption("CJ POR LOCO")
icone = pygame.image.load("base/iconeMulher.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela    = pygame.display.set_mode(tamanho)
branco  = (255, 255, 255)
preto   = (0,   0,   0)

fundo      = pygame.image.load("base/gtasa.jpg")
fundoDead  = pygame.image.load("base/seFodeu1.jpg")
fundoStart = pygame.image.load("base/imagemInicialGta1.jpg")

lua    = pygame.image.load("base/lua5.png")
iron   = pygame.image.load("base/cj1.png")
iron   = pygame.transform.scale(iron,   (116, 51))
missel = pygame.image.load("base/municao.png")
missel = pygame.transform.scale(missel, (125, 50))

missileSound  = pygame.mixer.Sound("base/tiro.mp3")
explosaoSound = pygame.mixer.Sound("base/fraseDeMorteCj.mp3")
pygame.mixer.music.load("base/musicaDeFundoGta.mp3")

fonteMenu    = pygame.font.SysFont("comicsans", 18)
fonteBotao   = pygame.font.SysFont("comicsans", 20)


# ── Jogo ───────────────────────────────────────────────────────────────────────
def jogar():
    pausado = False
    posicaoXPersona      = 0
    posicaoYPersona      = 60
    movimentoYPersona    = 0
    velocidadeMovPersona = 5
    posicaoXMissel       = 800
    posicaoYMissel       = 100
    velocidadeMissel     = 2
    pontos               = 0

    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)

    tamanhoLua   = 150
    pulsando     = 0.0
    direcaoPulso = 1

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
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

        # Pulso da lua
        pulsando += 0.15 * direcaoPulso
        if pulsando >= 8:
            direcaoPulso = -1
        elif pulsando <= 0:
            direcaoPulso = 1
        tamanhoAtualLua   = int(tamanhoLua + pulsando)
        luaRedimensionada = pygame.transform.scale(lua, (tamanhoAtualLua, tamanhoAtualLua))

        # Pausa
        if pausado:
            fontePausa = pygame.font.SysFont("comicsans", 72, bold=True)
            textoPausa = fontePausa.render("PAUSE", True, (255, 215, 0))
            tela.blit(fundo, (0, 0))
            tela.blit(luaRedimensionada, (tamanho[0] - tamanhoAtualLua - 10, 10))
            tela.blit(textoPausa, (
                tamanho[0] // 2 - textoPausa.get_width()  // 2,
                tamanho[1] // 2 - textoPausa.get_height() // 2,
            ))
            pygame.display.update()
            relogio.tick(60)
            continue

        # Movimento
        posicaoYPersona += movimentoYPersona
        posicaoYPersona  = max(0, min(posicaoYPersona, 649))

        posicaoXMissel -= velocidadeMissel
        if posicaoXMissel < -125:
            pygame.mixer.Sound.play(missileSound)
            posicaoXMissel    = 800
            pontos           += 1
            velocidadeMissel += 1
            posicaoYMissel    = random.randint(0, 650)

        # Desenho
        tela.fill(branco)
        tela.blit(fundo, (0, 0))
        tela.blit(luaRedimensionada, (tamanho[0] - tamanhoAtualLua - 10, 10))
        tela.blit(iron,   (posicaoXPersona, posicaoYPersona))
        tela.blit(missel, (posicaoXMissel,  posicaoYMissel))

        texto = fonteMenu.render("Pontos: " + str(pontos), True, branco)
        tela.blit(texto, (tamanho[0] // 2 - texto.get_width() // 2, 15))

        fonteDica = pygame.font.SysFont("comicsans", 14)
        textoDica = fonteDica.render("Press Space to Pause Game  |  Press ESC to close the game", True, (200, 200, 200))
        tela.blit(textoDica, (tamanho[0] // 2 - textoDica.get_width() // 2, 40))

        # Colisão
        retPersona = pygame.Rect(posicaoXPersona, posicaoYPersona, 116, 51)
        retMissel  = pygame.Rect(posicaoXMissel,  posicaoYMissel,  125, 25)

        if retPersona.colliderect(retMissel):
            escreverDados(nome, pontos)
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(explosaoSound)
            return pontos

        pygame.display.update()
        relogio.tick(60)


# ── Tela de morte ──────────────────────────────────────────────────────────────
def dead(pontos_partida):
    nome_m, pts_m, data_m, hora_m = maior_pontuador()

    fonteInfo    = pygame.font.SysFont("comicsans", 22, bold=True)
    fontePequena = pygame.font.SysFont("comicsans", 18)

    # Mede o texto do botão para o botão se ajustar ao conteúdo
    labelBotao  = fonteBotao.render("Reiniciar o Jogo", True, preto)
    padding     = 30
    largura_btn = labelBotao.get_width()  + padding * 2
    altura_btn  = labelBotao.get_height() + 14
    btn_x       = tamanho[0] // 2 - largura_btn // 2
    btn_y       = 490

    def desenhar():
        tela.blit(fundoDead, (0, 0))

        btn_rect = pygame.Rect(btn_x, btn_y, largura_btn, altura_btn)
        pygame.draw.rect(tela, branco, btn_rect, border_radius=15)
        tela.blit(labelBotao, (
            btn_x + padding,
            btn_y + 7,
        ))

        textoSua = fonteInfo.render(f"Sua pontuação: {pontos_partida} pontos", True, (255, 215, 0))
        tela.blit(textoSua, (tamanho[0] // 2 - textoSua.get_width() // 2, 555))

        textoMelhor = fontePequena.render(
            f"🏆  Maior Pontuador: {nome_m}  |  Pontos: {pts_m}  |  Data: {data_m}  |  Hora: {hora_m}",
            True, (255, 50, 50),
        )
        tela.blit(textoMelhor, (tamanho[0] // 2 - textoMelhor.get_width() // 2, 605))

        textoDica = fontePequena.render("Pressione ESC para fechar o jogo", True, (200, 200, 200))
        tela.blit(textoDica, (tamanho[0] // 2 - textoDica.get_width() // 2, 660))

        pygame.display.update()
        return btn_rect

    # Mostra a tela antes de falar
    btn_rect = desenhar()

    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(f"Game over! O maior pontuador é {nome_m} com {pts_m} pontos!")
    engine.runAndWait()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            elif evento.type == pygame.MOUSEBUTTONUP:
                if btn_rect.collidepoint(evento.pos):
                    return True

        btn_rect = desenhar()
        relogio.tick(60)


# ── Tela de boas-vindas ────────────────────────────────────────────────────────
def bemVindo():
    largura_btn  = 200
    altura_btn   = 50
    fonteNormal  = pygame.font.SysFont("comicsans", 22)
    fonteTitulo  = pygame.font.SysFont("comicsans", 42, bold=True)
    fontePequena = pygame.font.SysFont("comicsans", 18)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                btn_rect = pygame.Rect(tamanho[0] // 2 - largura_btn // 2, 560, largura_btn, altura_btn)
                if btn_rect.collidepoint(evento.pos):
                    largura_btn = 190
                    altura_btn  = 45

            elif evento.type == pygame.MOUSEBUTTONUP:
                btn_rect = pygame.Rect(tamanho[0] // 2 - largura_btn // 2, 560, largura_btn, altura_btn)
                if btn_rect.collidepoint(evento.pos):
                    largura_btn = 200
                    altura_btn  = 50
                    return

        tela.blit(fundoStart, (0, 0))

        titulo = fonteTitulo.render("Bem-vindo ao Jogo!", True, branco)
        tela.blit(titulo, (tamanho[0] // 2 - titulo.get_width() // 2, 60))

        textoNome = fonteNormal.render(f"Jogador: {nome}", True, (148, 0, 211))
        tela.blit(textoNome, (tamanho[0] // 2 - textoNome.get_width() // 2, 150))

        mecanica = [
            "Como jogar:",
            "- Use as setas CIMA e BAIXO para mover o personagem.",
            "- Desvie dos mísseis que vêm em sua direção.",
            "- Cada míssil desviado vale 1 ponto.",
            "- A velocidade aumenta a cada míssil desviado.",
            "- O jogo termina quando você for atingido!",
        ]
        for i, linha in enumerate(mecanica):
            txt = fonteNormal.render(linha, True, (0, 0, 255))
            tela.blit(txt, (tamanho[0] // 2 - txt.get_width() // 2, 230 + i * 35))

        pygame.draw.line(tela, (100, 100, 100), (100, 460), (900, 460), 2)

        textoMelhor = fontePequena.render(
            f"🏆 Melhor Jogador: {nome_maior}  |  Pontos: {maior_pontos}  |  Data: {dataJogada}",
            True, (255, 0, 0),
        )
        tela.blit(textoMelhor, (tamanho[0] // 2 - textoMelhor.get_width() // 2, 480))

        btn_rect = pygame.Rect(tamanho[0] // 2 - largura_btn // 2, 560, largura_btn, altura_btn)
        pygame.draw.rect(tela, (0, 180, 0), btn_rect, border_radius=20)
        startTexto = fonteNormal.render("Iniciar Partida", True, branco)
        tela.blit(startTexto, (tamanho[0] // 2 - startTexto.get_width() // 2, 570))

        textoDica = fontePequena.render("Pressione ESC para fechar o jogo", True, (200, 200, 200))
        tela.blit(textoDica, (tamanho[0] // 2 - textoDica.get_width() // 2, 650))

        pygame.display.update()
        relogio.tick(60)


# ── Loop raiz ──────────────────────────────────────────────────────────────────
bemVindo()
while True:
    pontos_finais = jogar()
    reiniciar = dead(pontos_finais)
    if not reiniciar:
        break