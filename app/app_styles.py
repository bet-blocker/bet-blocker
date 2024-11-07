import platform
from enum import Enum

class AppConfig:
    def __init__(self):
        if platform.system() == "Windows":
            self.window_width = 410
            self.window_height = 470
        elif platform.system() == "Macos": 
            self.window_width = 850
            self.window_height = 400
        else:  
            self.window_width = 420
            self.window_height = 480

class AppButtonColors(Enum):
    AZUL = "#3f9dfb"
    VERDE = "#3fb5a3"
    BRANCO = "#ffffff"
    LARANJA = "orange"

class AppColors(Enum):
    CINZA_CLARO = "#f0f3f5"
    BRANCO = "#feffff"
    VERDE = "#3fb5a3"
    VERMELHO = "#f25f5c"
    PRETO = "#403d3d"