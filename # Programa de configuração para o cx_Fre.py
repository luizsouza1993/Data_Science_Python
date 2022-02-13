# Programa de configuração para o cx_Freeze poder "Buildar"
import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter"], "include_files": ["fundo.png", "lapis.ico"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Editor de Texto",
    version="1.0",
    description="Um editor de texto personalizado",
    options={"build_exe": build_exe_options},
    executables=[Executable(script="# Hangman Game (Jogo da Forca).py", base=base, icon="lapis.ico")]
)

# Fim Config