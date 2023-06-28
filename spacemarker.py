import pygame
import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import math

pygame.init()
largura_tela = 800
altura_tela = 500
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Space Marker")
fundo = pygame.image.load("bg.jpg")
icone = pygame.image.load("space-0.png")
pygame.display.set_icon(icone)

def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

class Marcacao:
    def __init__(self, posicao, nome):
        self.posicao = posicao
        self.nome = nome

marcacoes = []
historico_salvos = []
historico_excluidos = []

def get_star_info():
    root = tk.Tk()
    root.withdraw()
    star_name = simpledialog.askstring("Nome da Estrela", "Insira o nome da estrela:")
    return star_name

def salvar_marcacoes():
    try:
        with open("marcacoes.pickle", "wb") as file:
            pickle.dump(marcacoes, file)
        historico_salvos.append(marcacoes.copy())
        messagebox.showinfo("Sucesso", "Marcações salvas com sucesso.")
        pygame.time.delay(3000)
    except IOError:
        messagebox.showerror("Erro", "Erro ao salvar as marcações.")

def carregar_marcacoes():
    try:
        with open("marcacoes.pickle", "rb") as file:
            marcacoes = pickle.load(file)
        historico_excluidos.append(marcacoes.copy())
        coordenadas_salvas = "\n".join([f"({m.posicao[0]}, {m.posicao[1]}) - {m.nome}" for m in marcacoes])
        messagebox.showinfo("Sucesso", f"Marcações carregadas com sucesso:\n{coordenadas_salvas}")
        pygame.time.delay(3000)
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo de marcações não encontrado.")

def excluir_marcacoes():
    marcacoes.clear()
    messagebox.showinfo("Sucesso", "Todas as marcações foram excluídas.")
    pygame.time.delay(3000)

pygame.mixer.init()
play_music("Space_Machine_Power.mp3")
fonte = pygame.font.Font(None, 24)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salvar_marcacoes()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                salvar_marcacoes()
                running = False
            elif event.key == pygame.K_F10:
                salvar_marcacoes()
            elif event.key == pygame.K_F11:
                carregar_marcacoes()
                if len(historico_excluidos) > 0:
                    marcacoes = historico_excluidos[-1].copy()
            elif event.key == pygame.K_F12:
                excluir_marcacoes()
                if len(historico_salvos) > 0:
                    marcacoes = historico_salvos[-1].copy()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            star_name = get_star_info()
            marcacoes.append(Marcacao(mouse_position, star_name))

    tela.blit(fundo, (0, 0))
    for i, marcacao in enumerate(marcacoes):
        pygame.draw.circle(tela, (255, 255, 255), marcacao.posicao, 5)
        if i > 0:
            pygame.draw.line(tela, (255, 255, 255), marcacoes[i-1].posicao, marcacao.posicao)
            dist_x = abs(marcacao.posicao[0] - marcacoes[i-1].posicao[0])
            dist_y = abs(marcacao.posicao[1] - marcacoes[i-1].posicao[1])
            distance = math.sqrt(dist_x**2 + dist_y**2)
            text_surface = pygame.font.SysFont('Arial', 12).render(f'({marcacao.posicao[0]}, {marcacao.posicao[1]}) - {marcacao.nome} | Distância: {distance:.2f}', True, (255, 255, 255))
            tela.blit(text_surface, (marcacao.posicao[0]+10, marcacao.posicao[1]-20))

    texto_f10 = fonte.render("F10: Salvar Marcações", True, (255, 255, 255))
    tela.blit(texto_f10, (10, 10))

    texto_f11 = fonte.render("F11: Carregar Marcações", True, (255, 255, 255))
    tela.blit(texto_f11, (10, 40))

    texto_f12 = fonte.render("F12: Excluir Todas as Marcações", True, (255, 255, 255))
    tela.blit(texto_f12, (10, 70))

    pygame.display.update()

with open("marcacao.txt", "w") as file:
    for i, historico in enumerate(historico_salvos):
        file.write(f"Histórico {i+1}:\n")
        for marcacao in historico:
            file.write(f"({marcacao.posicao[0]}, {marcacao.posicao[1]}) - {marcacao.nome}\n")

pygame.quit()
