import os, sys
import platform
import ctypes
import shutil
import tkinter as tk

from tkinter import BooleanVar, ttk, messagebox
from PIL import Image, ImageTk
from src.utils.get_paths import get_path_from_context
from src.functions.blocker import restrict_sites
from src.utils.logs import logger
from app.app_styles import AppConfig, AppColors, AppButtonColors

class AppInitializer:
    def __init__(self, config: AppConfig):
        self.config = config
        self.app_window = tk.Tk()
        self.app_window.title("Bloqueador de Apostas")
        self.app_window.geometry("410x470")
        self.app_window.configure(background=AppColors.CINZA_CLARO.value)
        self.app_window.resizable(width=False, height=False)

        # Setup frames
        self.setup_frames()

        # Setup components
        self.setup_frame_logo()
        self.setup_frame_body()

    def setup_frames(self):
        self.app_frame_logo = tk.Frame(
            self.app_window,
            width=self.config.window_width,
            height=60,
            bg=AppColors.CINZA_CLARO.value,
            relief="flat",
        )
        self.app_frame_logo.grid(row=0, column=0, columnspan=2, sticky="nsew")

        # Body Frame
        self.blocklist_path = self.get_or_create_blocklist_path()
        self.app_frame_body = tk.Frame(
            self.app_window,
            width=self.config.window_width,
            height=self.config.window_height - 60,
            bg=AppColors.CINZA_CLARO.value,
            relief="flat",
        )
        self.app_frame_body.grid(row=1, column=0, columnspan=2, sticky="nsew")

    def run(self):
        """Inicia a execução da aplicação."""
        self.app_window.focus_force()
        self.app_window.after(100, lambda: logger.info("Bem-vindo(a) ao Bloqueador de Bets. A aplicação está em execução."))
        self.app_window.mainloop()
        logger.info("Aplicação encerrada.")

    def get_or_create_blocklist_path(self):
        """Obtém o caminho do arquivo de lista bloqueada e cria caso não exista."""
        file_path = get_path_from_context("blocklist.txt")
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                file.write("")
        return file_path

    def setup_frame_logo(self):
        """Configura o frame de logo na janela principal."""
        logo = Image.open(get_path_from_context("assets/block.png")).resize((40, 40))
        self.logo_image = ImageTk.PhotoImage(logo)

        app_label_img = tk.Label(
            self.app_frame_logo,
            height=60,
            image=self.logo_image,
            bg=AppColors.CINZA_CLARO.value,
        )
        app_label_img.place(x=20, y=0)

        # Logo text
        app_label_logo = tk.Label(
            self.app_frame_logo,
            text="Bloqueador de Apostas",
            height=1,
            anchor="ne",
            font=("Ivy", 20),
            bg=AppColors.CINZA_CLARO.value,
            fg=AppColors.PRETO.value,
        )
        app_label_logo.place(x=70, y=12)

        # Divider line
        app_label_line = tk.Label(
            self.app_frame_logo,
            height=1,
            width="445",
            anchor="nw",
            font=("Ivy", 1),
            bg=AppColors.VERDE.value,
        )
        app_label_line.place(x=0, y=57)

    def setup_frame_body(self):
        # Blocklist label
        blocklist = tk.Label(
            self.app_frame_body,
            text="Lista de bets bloqueadas",
            height=1,
            font=("Ivy", 12),
            bg=AppColors.CINZA_CLARO.value,
            fg=AppColors.PRETO.value,
        )
        blocklist.place(x=18, y=20)

        # Blocklist listbox
        lstbox_blocklist = tk.Listbox(
            self.app_frame_body,
            width=40,
            height=14,
            bg=AppColors.BRANCO.value,
            fg=AppColors.PRETO.value,
        )
        lstbox_blocklist.place(x=20, y=50)
        lstbox_blocklist.insert(tk.END, *self.get_sites_from_blocklist())

        # Progress bar
        progress_bar = ttk.Progressbar(
            self.app_frame_body, orient="horizontal", length=360, mode="determinate"
        )
        progress_bar.place(x=20, y=330)

        # Checkbox for agreement
        _chk_choice = BooleanVar()
        check_box = tk.Checkbutton(
            self.app_frame_body,
            text="Ao clicar em 'Bloquear Sites', você concorda em comunicar a sua rede de apoio possíveis situações de jogo compulsivo.",
            variable=_chk_choice,
            fg=AppColors.PRETO.value,
            font=("Ivy", 8),
            wraplength=360,
            anchor="w",
            justify="left",
        )
        check_box.place(x=15, y=360)

        # Buttons
        if platform.system() == "Windows":
            block_button = tk.Button(
                self.app_frame_body,
                text="Bloquear Firewall",
                width=15,
                height=2,
                bg=AppColors.VERDE.value,
                fg=AppColors.BRANCO.value,
                command=lambda: restrict_sites(
                    _chk_choice, lstbox_blocklist, progress_bar, self.app_window
                ),
                relief="flat",
            )
            block_button.place(x=270, y=52)

        copy_hosts_button = tk.Button(
            self.app_frame_body,
            text="Bloquear DNS",
            width=15,
            height=2,
            bg=AppButtonColors.AZUL.value,
            fg=AppColors.BRANCO.value,
            command=copy_hosts,
            relief="flat",
        )
        copy_hosts_button.place(
            x=270, y=100
        )  # Mantém a posição correta para evitar sobreposição

        support_button = tk.Button(
            self.app_frame_body,
            text="Configurações",
            width=15,
            height=2,
            bg=AppButtonColors.LARANJA.value,
            fg=AppColors.BRANCO.value,
            relief="flat",
        )
        support_button.place(x=270, y=148)  # Ajustado para evitar sobreposição

    def get_sites_from_blocklist(self) -> list:
        with open(self.blocklist_path, "r") as file:
            sites = file.readlines()
        return [site.strip() for site in sites if site.strip()]

## Auxiliares
def request_admin_grant():
    if ctypes.windll.shell32.IsUserAnAdmin():
        return True
    else:
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", os.sys.executable, " ".join(os.sys.argv), None, 1
        )
        return False

# Requisitar permissão de administrador no Linux
def request_sudo_grant() -> None:
    # Testando se o usuário executou o processo como root
    if os.geteuid() != 0:
        os.execvp('sudo', ['sudo', 'python3'] + sys.argv)

    return True

# Requisitar permissão de administrador no MacOS
def request_doas_grant() -> bool:
    pass # todo

def copy_hosts():
    match platform.system():
        case "Windows":
            copy_windows_hosts()

        case "Linux":
            copy_linux_hosts()

        case "Darwin":
            copy_macos_hosts()

        case _:
            print("Sistema operacional não reconhecido!")

def copy_windows_hosts():
    """Copia o arquivo ./hosts para C:\Windows\System32\drivers\etc\hosts."""
    if request_admin_grant():
        try:
            origem = get_path_from_context("hosts")
            destino = r"C:\Windows\System32\drivers\etc\hosts"
            shutil.copyfile(origem, destino)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao copiar o arquivo hosts: {e}")
            logger.error(f"Erro ao copiar o arquivo hosts: {e}")

def copy_linux_hosts():
    """Copia o arquivo ./hosts para /etc/hosts"""
    request_sudo_grant()
    try:
        origem = get_path_from_context("hosts")
        with open("/etc/hosts", "a") as destino:
            with open(origem, "r") as host_para_bloquear:
                destino.write("\n\n")
                destino.write(host_para_bloquear.read())

    except Exception as e:
        messagebox.showerror("Erro", f"Falha ao copiar o arquivo hosts: {e}")
        logger.error(f"Erro ao copiar o arquivo hosts: {e}")

# To do
def copy_macos_hosts():
    pass
