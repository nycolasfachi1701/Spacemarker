import pygame
import tkinter as tk
from tkinter import simpledialog
import pickle
import winsound

pygame.init()
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Space Marker")
space = pygame.image.load("space.png")
pygame.display.set_icon(space)



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

# Função para salvar as marcações em arquivo
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

# Função para excluir todas as marcações
def excluir_marcacoes():
    marcacoes.clear()
    print("Todas as marcações foram excluídas.")

# Loop principal do jogo
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

    tela.fill((255, 255, 255))  # Preenche a tela com a cor branca

    # Desenhe as marcações na tela
    for marcacao in marcacoes:
        pygame.draw.circle(tela, (255, 0, 0), marcacao.posicao, 5)

    # Atualização da tela
    pygame.display.update()

pygame.quit()
