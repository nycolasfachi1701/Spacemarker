import pygame
import tkinter as tk
from tkinter import simpledialog, messagebox

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
historico_salvos = []
historico_excluidos = []

def get_star_info():
    root = tk.Tk()
    root.withdraw()
    star_name = simpledialog.askstring("Nome da Estrela", "Insira o nome da estrela:")
    return star_name

def salvar_marcacoes():
    historico_salvos.append(marcacoes.copy())
    messagebox.showinfo("Sucesso", "Marcações salvas com sucesso.")
    pygame.time.delay(2000)  # Exibe a mensagem por 2 segundos

def carregar_marcacoes():
    if len(historico_salvos) > 0:
        marcacoes = historico_salvos[-1].copy()
        messagebox.showinfo("Sucesso", "Marcações carregadas com sucesso.")
        pygame.time.delay(2000)  # Exibe a mensagem por 2 segundos
    else:
        messagebox.showerror("Erro", "Nenhuma marcação salva encontrada.")

def excluir_marcacoes():
    if len(marcacoes) > 0:
        historico_excluidos.append(marcacoes.copy())
        marcacoes.clear()
        messagebox.showinfo("Sucesso", "Todas as marcações foram excluídas.")
        pygame.time.delay(2000)  # Exibe a mensagem por 2 segundos
    else:
        messagebox.showerror("Erro", "Nenhuma marcação para excluir.")

# Inicializando o reconhecimento do som
pygame.mixer.init()

play_music("Space_Machine_Power.mp3")

fonte = pygame.font.Font(None, 24)  # Definindo a fonte para o texto

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
            elif event.key == pygame.K_F12:
                excluir_marcacoes()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            star_name = get_star_info()
            marcacoes.append(Marcacao(mouse_position, star_name))

    tela.blit(fundo, (0, 0))  # Desenha o fundo na tela

    # Desenha as marcações na tela
    for i, marcacao in enumerate(marcacoes):
        pygame.draw.circle(tela, (255, 255, 255), marcacao.posicao, 5)
        if i > 0:
            pygame.draw.line(tela, (255, 255, 255), marcacoes[i-1].posicao, marcacao.posicao)
        text_surface = pygame.font.SysFont('Arial', 12).render(f'({marcacao.posicao[0]}, {marcacao.posicao[1]}) - {marcacao.nome}', True, (255, 255, 255))
        tela.blit(text_surface, (marcacao.posicao[0]+10, marcacao.posicao[1]-20))

    # Desenha as finalidades das teclas F10, F11 e F12
    texto_f10 = fonte.render("F10: Salvar Marcações", True, (255, 255, 255))
    tela.blit(texto_f10, (10, 10))

    texto_f11 = fonte.render("F11: Carregar Marcações", True, (255, 255, 255))
    tela.blit(texto_f11, (10, 40))

    texto_f12 = fonte.render("F12: Excluir Todas as Marcações", True, (255, 255, 255))
    tela.blit(texto_f12, (10, 70))

    # Atualização da tela
    pygame.display.update()

pygame.quit()
