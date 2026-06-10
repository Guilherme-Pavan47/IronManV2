import pygame
import time


def contar_regressiva(tela, fonte):
    largura, altura = tela.get_size()

    for i in range(3, 0, -1):
        tela.fill((0, 0, 0))
        texto = fonte.render(str(i), True, (255, 215, 0))
        tela.blit(texto, (
            largura // 2 - texto.get_width()  // 2,
            altura  // 2 - texto.get_height() // 2,
        ))
        pygame.display.update()
        time.sleep(1)