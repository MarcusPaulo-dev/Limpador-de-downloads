from pathlib import Path
from shutil import rmtree
import winshell

# limpar arquivos da pasta de dowloads
pastadown = Path('C:/Users/Marcus/Downloads')
for arq in pastadown.iterdir():
    if arq.is_file():
        arq.unlink()
    elif arq.is_dir():
        rmtree(arq)

# limpar arquivos da lixeira
try:
    winshell.ShellRecycleBin.empty(False,False)
except:
    pass