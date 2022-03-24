from os import *
from pytube import YouTube
from pathlib import *

home = Path.home() # Chamar a pasta User do sistema 
desktop = home / 'desktop' # Abrir a pasta desktop

yt = YouTube(input('Coloque o link aqui: '))
yt.streams.filter(only_audio = True)

stream = yt.streams.get_by_itag(251)
stream.download(desktop)
