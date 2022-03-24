import os
from pytube import YouTube
from pydub import AudioSegment
from pathlib import *
from os import *

home = Path.home() # Chamar a pasta User do sistema 
desktop = home / 'desktop' # Abrir a pasta desktop

yt = YouTube(input('Coloque o link aqui: ')) # Colocar link do video do youtube
yt.streams.filter(only_audio = True)

stream = yt.streams.get_by_itag(251)
stream.download(desktop) # Baixar o arquivo "escravo"

path = Path(desktop)

for filename1 in listdir(desktop): # Procurar o arquivo na pasta
   
    for filename1 in path.glob('*'): # Procurar o arquivo pela extensão
        if filename1.suffix == '.webm':
            nome1 = str(filename1)

novo_nome = nome1[:-5]

# Conversão do arquivo para mp3
AudioSegment.from_file(nome1).export(novo_nome + '.mp3',format='mp3',bitrate='320k') 

os.remove(nome1) # Exclui o arquivo escravo
