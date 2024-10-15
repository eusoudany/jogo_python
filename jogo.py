import random
from pgzero.actor import Actor
from pygame import Rect
from math import sin
import time  # Importa o módulo time

# Configurações iniciais
WIDTH = 800
HEIGHT = 600

# Variáveis de controle
game_started = False
music_on = True

# Criar o ator principal e inimigos
hero = Actor("hero_idle", (400, 300))  # Posição inicial do herói
enemies = [Actor("enemy_idle", (random.randint(100, 700), random.randint(100, 500))) for _ in range(3)]

# Retângulos (áreas) dos botões do menu
button_start = Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 40)
button_music = Rect(WIDTH // 2 - 100, HEIGHT // 2, 200, 40)
button_exit = Rect(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 40)

# Função para alternar música
def toggle_music():
    global music_on
    music_on = not music_on
    if music_on:
        music.play('background_music')
    else:
        music.stop()

# Função para o menu principal
def draw_menu():
    screen.clear()
    screen.draw.text("1. Start Game", center=(WIDTH // 2, HEIGHT // 2 - 50), fontsize=40)
    screen.draw.text("2. Music On/Off", center=(WIDTH // 2, HEIGHT // 2), fontsize=40)
    screen.draw.text("3. Exit", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=40)

# Função para o jogo em execução
def draw_game():
    screen.clear()
    hero.draw()
    for enemy in enemies:
        enemy.draw()

# Detecta cliques do mouse nos botões do menu
def on_mouse_down(pos):
    global game_started
    if button_start.collidepoint(pos):
        game_started = True
    elif button_music.collidepoint(pos):
        toggle_music()
    elif button_exit.collidepoint(pos):
        exit()

# Movimento suave do herói e dos inimigos
def update():
    if game_started:
        if keyboard.left:
            hero.x -= 2
        if keyboard.right:
            hero.x += 2
        if keyboard.up:
            hero.y -= 2
        if keyboard.down:
            hero.y += 2
        
        # Movimento básico dos inimigos
        current_time = time.time() * 1000  # Obtenha o tempo atual em milissegundos
        for enemy in enemies:
            enemy.x += sin(current_time / 500) * 2

# Desenha a tela com base no estado do jogo
def draw():
    if game_started:
        draw_game()
    else:
        draw_menu()
