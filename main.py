import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import BooleanVar
from tkinter import ttk  # Importando o módulo ttk
import logging
import socket

import ctypes
import shutil

#import from functions/firewall.py
from functions.firewall import bloquear_no_firewall
from functions.blocker import bloquear_sites

# Configuração de log
logging.basicConfig(level=logging.DEBUG, filename='bloqueador.log', 
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Caminho do arquivo de blacklist
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

class Cores:
    CO0 = "#f0f3f5"  # Cinza claro
    CO1 = "#feffff"  # Branco
    CO2 = "#3fb5a3"  # Verde
    CO3 = "#f25f5c"  # Vermelho
    CO4 = "#403d3d"  # Preto
    AZUL = "#3f9dfb"  # Azul para o botão
    VERDE = "#3fb5a3"  # Verde para o botão
    BRANCO = "#ffffff"  # Branco para a fonte
    LARANJA = "orange"  # Laranja para o botão

# Configuração da janela principal
janela = tk.Tk()
janela.title("Bloqueador de Apostas")
janela.geometry("410x460")  # Aumente a altura da janela para a barra de progresso
janela.configure(background=Cores.CO1)
janela.resizable(width=False, height=False)

# Caminho do arquivo de blacklist
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
sites_file = os.path.join(diretorio_atual, "blacklist.txt")

# Função para solicitar permissão de administrador
def solicitar_permissao():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        # Se não for administrador, solicita permissão
        ctypes.windll.shell32.ShellExecuteW(None, "runas", os.sys.executable, " ".join(os.sys.argv), None, 1)
        return False

def copiar_hosts():
    """Copia o arquivo ./hosts para C:\Windows\System32\drivers\etc\hosts."""
    if solicitar_permissao():
        try:
            # Caminho do arquivo de origem e destino
            origem = os.path.join(diretorio_atual, "hosts")
            destino = r"C:\Windows\System32\drivers\etc\hosts"
            
            # Copiando o arquivo
            shutil.copyfile(origem, destino)
            messagebox.showinfo("Sucesso", "Arquivo hosts copiado com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao copiar o arquivo hosts: {e}")
            logging.error(f"Erro ao copiar o arquivo hosts: {e}")


def carregar_blacklist():
    """Carrega a lista de sites bloqueados do arquivo blacklist.txt."""
    try:
        with open(sites_file, "r") as file:
            sites = file.readlines()
            if not sites:
                messagebox.showinfo("Informação", "A lista de sites bloqueados está vazia.")
            else:
                for site in sites:
                    site = site.strip()  # Remove espaços em branco
                    if site:  # Adiciona apenas se não estiver vazio
                        lista.insert(tk.END, site)
    except FileNotFoundError:
        logging.error("Arquivo de blacklist não encontrado. Criando um novo arquivo.")
        with open(sites_file, "w") as file:
            file.write("")  # Cria um novo arquivo se não existir
        messagebox.showerror("Erro", "Arquivo de blacklist não encontrado. Um novo arquivo foi criado.")
        carregar_blacklist()

def regra_existente(dominio):
    """Verifica se a regra de bloqueio já existe no firewall."""
    try:
        regra_nome = f'Bloqueio de {dominio}'
        output = os.popen('netsh advfirewall firewall show rule name="{}"'.format(regra_nome)).read()
        return regra_nome in output
    except Exception as e:
        logging.error(f"Erro ao verificar regra: {e}")
        return False

def bloquear_por_dominio(dominio):
    """Adiciona uma entrada ao arquivo hosts para bloquear um domínio."""
    try:
        if regra_existente(dominio):
            logging.info(f"O domínio {dominio} já está bloqueado.")
            return True

        with open(r"C:\Windows\System32\drivers\etc\hosts", "a") as hosts_file:
            hosts_file.write(f"0.0.0.0 {dominio}\n")
        
        logging.info(f"Domínio {dominio} bloqueado com sucesso.")
        return True
    except Exception as e:
        logging.error(f"Falha ao bloquear {dominio} no arquivo hosts: {e}")
        return False

# Frames
frame_logo = tk.Frame(janela, width=410, height=60, bg=Cores.CO1, relief="flat")
frame_logo.grid(row=0, column=0, columnspan=2, sticky="nsew")

frame_corpo = tk.Frame(janela, width=410, height=400, bg=Cores.CO1, relief="flat")
frame_corpo.grid(row=1, column=0, columnspan=2, sticky="nsew")

# Configurando frame logo
imagem = Image.open(os.path.join(diretorio_atual, "assets/block.png"))
imagem = imagem.resize((40, 40))
image = ImageTk.PhotoImage(imagem)

l_image = tk.Label(frame_logo, height=60, image=image, bg=Cores.CO1)
l_image.place(x=20, y=0)

l_logo = tk.Label(frame_logo, text="Bloqueador de Apostas", height=1, anchor="ne", font=('Ivy', 20), bg=Cores.CO1, fg=Cores.CO4)
l_logo.place(x=70, y=12)

l_linha = tk.Label(
    frame_logo, 
    text="Bloqueador de Apostas", 
    height=1, 
    width="445", 
    anchor="nw", 
    font=('Ivy', 1), 
    bg=Cores.CO2
)
l_linha.place(x=0, y=57)

# Configurando frame corpo font negrito
l_blacklist = tk.Label(
    frame_corpo, 
    text="Lista de bets bloqueadas", 
    height=1, font=('Ivy', 12),
    bg=Cores.CO1, 
    fg=Cores.CO4, 
    anchor="w", 
    justify="left",
    wraplength=380
)
l_blacklist.place(x=18, y=20)

# Lista de sites bloqueados
lista = tk.Listbox(
    frame_corpo, width=40, height=14, bg=Cores.CO0, fg=Cores.CO4
)
lista.place(x=20, y=50)

# Barra de Progresso
progresso = ttk.Progressbar(
    frame_corpo, orient="horizontal", length=360, mode="determinate"
)
progresso.place(x=20, y=330)

# Checkbox para concordar em participar da rede de apoio
checkbox_var = BooleanVar()
checkbox = tk.Checkbutton(
    frame_corpo,
    text="Ao clicar em 'Bloquear Sites', você concorda em comunicar a sua rede de apoio possíveis situações de jogo compulsivo.",
    variable=checkbox_var,
    bg=Cores.CO1,
    fg=Cores.CO4,
    font=('Ivy', 8),
    wraplength=380,
    anchor="w",
    justify="left"
)
checkbox.place(x=16, y=290)

# Botão de bloquear site
b_bloquear = tk.Button(
    frame_corpo, text="Bloquear Firewall", width=15, height=2,
    bg=Cores.VERDE, fg=Cores.BRANCO, command=lambda: bloquear_sites(checkbox_var, lista, progresso, janela), relief="flat"
)
b_bloquear.place(x=270, y=50)

# Chame a função copiar_hosts em algum lugar do seu código, como em um botão
botao_copiar_hosts = tk.Button(
    frame_corpo, text="Bloquear DNS", width=15, height=2,
    bg=Cores.AZUL, fg=Cores.BRANCO, command=copiar_hosts, relief="flat"
)
botao_copiar_hosts.place(x=270, y=100)

# Chame a função copiar_hosts em algum lugar do seu código, como em um botão
botao_apoio = tk.Button(
    frame_corpo, text="Configurações", width=15, height=2,
    bg=Cores.LARANJA, fg=Cores.BRANCO, relief="flat"
)
botao_apoio.place(x=270, y=150)

# Carregar a blacklist na inicialização
carregar_blacklist()

# Iniciar o loop da interface
janela.mainloop()
