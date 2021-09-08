from random import randint
import pygame
from pygame import font
from pygame import display
from pygame.image import load
from pygame.transform import scale
from pygame.sprite import Sprite, Group, GroupSingle, groupcollide
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame.time import Clock


pygame.init()

tamanho = 800, 600
fonte = font.SysFont('comicsans', 50)
fonte_perdeu = font.SysFont('comicsans', 300)

superficie = display.set_mode(
    size=tamanho,
    display=0
)
display.set_caption(
    'Mentorama detonando o Python'
)

fundo = scale(
    load('images/praia.jpg'),
    tamanho
)


class Mentorama(Sprite):
    def __init__(self, bomba):
        super().__init__()

        self.image = load('images/mentorama_small.png')
        self.rect = self.image.get_rect()
        self.bomba = bomba
        self.velocidade = 2

    def tacar_bomba(self):
        if len(self.bomba) < 15:
            self.bomba.add(
                Bomba(*self.rect.center)
            )

    def update(self):
        keys = pygame.key.get_pressed()

        bomba_fonte = fonte.render(
            f'Bombas: {15 - len(self.bomba)}',
            True,
            (255, 255, 255)
        )
        superficie.blit(bomba_fonte, (20, 20))

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidade


class Bomba(Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = load('images/bomba.png')
        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def update(self):
        self.rect.x += 1

        if self.rect.x > tamanho[0]:
            self.kill()


class Python(Sprite):
    def __init__(self):
        super().__init__()

        self.image = load('images/python.png')
        self.rect = self.image.get_rect(
            center=(800, randint(20, 580))
        )

    def update(self):
        global perdeu
        self.rect.x -= 0.1

        if self.rect.x == 0:
            self.kill()
            perdeu = True


grupo_python = Group()
grupo_bomba = Group()
mentorama = Mentorama(grupo_bomba)
grupo_mentorama = GroupSingle(mentorama)

grupo_python.add(Python())

clock = Clock()
mortes = 0
round = 0
perdeu = False

while True:
    # Loop de eventos

    clock.tick(120)  # FPS

    if round % 120 == 0:
        if mortes < 20:
            grupo_python.add(Python())
        for i in range(int(mortes / 20)):
            grupo_python.add(Python())

    # Espaço dos eventos
    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYUP:
            if evento.key == K_SPACE:
                mentorama.tacar_bomba()

    if groupcollide(grupo_bomba, grupo_python, True, True):
        mortes += 1

    # Espaço do display
    superficie.blit(fundo, (0, 0))

    fonte_mortes = fonte.render(
            f'Python: {mortes}',
            True,
            (255, 255, 255)
    )

    superficie.blit(fonte_mortes, (20, 70))

    grupo_mentorama.draw(superficie)
    grupo_python.draw(superficie)
    grupo_bomba.draw(superficie)

    grupo_mentorama.update()
    grupo_python.update()
    grupo_bomba.update()

    if perdeu:
        deu_ruim = fonte_perdeu.render(
            'Voce perdeu',
            True,
            (255, 255, 255)
        )
        superficie.blit(deu_ruim, (200, 200))
        display.update()
        pygame.time.delay(10000)

    round += 1
    display.update()
