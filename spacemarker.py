import pygame
import tkinter as tk
from tkinter import simpledialog
import pickle

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("bg.jpg")

def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

class Marcacao:
    def __init__(self, posicao, nome):
        self.posicao = posicao
        self.nome = nome

marcacoes = []

def get_star_name():
    root = tk.Tk()
    root.withdraw()
    star_name = simpledialog.askstring("Nome da Estrela", "Insira o nome da estrela:")
    return star_name

def salvar_marcacoes():
    with open("marcacoes.pickle", "wb") as file:
        pickle.dump(marcacoes, file)
    print("Marcações salvas com sucesso.")

# Função para carregar as marcações salvas
def carregar_marcacoes():
    try:
        with open("marcacoes.pickle", "rb") as file:
            marcacoes = pickle.load(file)
        print("Marcações carregadas com sucesso.")
    except FileNotFoundError:
        print("Arquivo de marcações não encontrado.")

def excluir_marcacoes():
    marcacoes.clear()
    print("Todas as marcações foram excluídas.")

#Inicializando o reconhecimento do som
pygame.mixer.init()

play_music("Space_Machine_Power.mp3")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salvar_marcacoes()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            star_name = get_star_name()
            marcacoes.append(Marcacao(mouse_position, star_name))

    tela.blit(fundo, (0, 0))  # Desenha o fundo na tela

    # Desenha as marcações na tela
    for marcacao in marcacoes:
        pygame.draw.circle(tela, (255, 0, 0), marcacao.posicao, 5)

    # Atualização da tela
    pygame.display.update()

pygame.quit()
