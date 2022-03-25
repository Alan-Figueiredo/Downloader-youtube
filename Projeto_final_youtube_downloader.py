import os
from pytube import YouTube
from pydub import AudioSegment
from pathlib import *
from os import *
from pytube.cli import on_progress


home = Path.home() # Chamar a pasta User do sistema 
desktop = home / 'desktop' # Abrir a pasta desktop

# Funcão para baixar mp3
def mp3(progresso_mp3):


    progresso_mp3 = YouTube(yt,on_progress_callback=on_progress) # Mostrar barra de progresso
    progresso_mp3.streams.filter(only_audio = True) # Somente audio
    
    print(progresso_mp3.title) # Mostrar titulo do video
    print('baixando...')

    stream = progresso_mp3.streams.get_by_itag(251)
    stream.download(desktop) # Baixar o arquivo "escravo"

    path = Path(desktop)

    for filename1 in listdir(desktop): # Procurar o arquivo na pasta
    
        for filename1 in path.glob('*'): # Procurar o arquivo pela extensão
            if filename1.suffix == '.webm':
                nome1 = str(filename1)

    novo_nome = nome1[:-5]
    AudioSegment.from_file(nome1).export(novo_nome + '.mp3',format='mp3',bitrate='320k') # Converter em MP3
    
    os.remove(nome1)

# Funcão para baixar mp4
def mp4(progresso_mp4):
    progresso_mp4 = YouTube(yt,on_progress_callback=on_progress) # Mostrar barra de progresso

    print(progresso_mp4.title) # Mostrar titulo do video
    print('baixando...')

    progresso_mp4.streams.filter(adaptive=True) # Qualidade 

    #stream = progresso.streams.get_by_itag(22) # Download por "ITAG"
    stream = progresso_mp4.streams.get_highest_resolution()
    stream.download(desktop)

yt = input('Coloque o link aqui: ') # Colocar link do video do youtube

escolha = input('[1] Video [2] Musica: ')

try: 
    if escolha == '1':
        mp3(yt)
    elif escolha == '2':
        mp4(yt)
except: 
    pass
print('Digite uma opção valida')