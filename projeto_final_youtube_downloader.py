import os
from pytube import *
from pydub import AudioSegment
from pathlib import *
from os import *
from pytube.cli import on_progress
from tkinter import filedialog
import time 

erro = 'erro ao baixar... '

print('escolha um diretorio: ')
time.sleep(1)

diretorio = filedialog.askdirectory() # Função para escolher o diretorio do download
os.system('cls')

path = Path(diretorio) # Variavel para o caminho do sistema

print(f'Pasta de destino: {diretorio}')

while True:

    home = Path.home() # Chamar a pasta User do sistema 
    desktop = home / 'desktop' # Abrir a pasta desktop

    # Funcão para baixar mp3
    def mp3(progresso_mp3):

        
        progresso_mp3 = YouTube(yt,on_progress_callback=on_progress) # Mostrar barra de progresso
        progresso_mp3.streams.filter(only_audio = True) # Somente audio
        
        print(f'Titulo do video: {progresso_mp3.title}') # Mostrar titulo do video
        print('Baixando...')

        stream = progresso_mp3.streams.get_by_itag(140)
        stream.download(diretorio) # Baixar o arquivo "escravo"

        print()
        print('Convertendo...')

        path = Path(diretorio)       
        lista = [filename1 for filename1 in list(path.glob('*')) if filename1.suffix =='.mp4' ] # Logica para procurar pela extensão.

        nome1 = str(lista[0])
        novo_nome = nome1[:-4]

        AudioSegment.from_file(nome1).export(novo_nome + '.mp3',format='mp3',bitrate='320k') # Converter em MP3
        
        os.remove(nome1)
        print('Conversão realizada com sucesso! ')

    # Funcão para baixar mp4   
    def mp4(progresso_mp4):

        progresso_mp4 = YouTube(yt,on_progress_callback=on_progress) # Mostrar barra de progresso

        print(f'Titulo do video: {progresso_mp4.title}') # Mostrar titulo do video
        print('Baixando...')

        progresso_mp4.streams.filter(adaptive=True) # Qualidade 

        #stream = progresso.streams.get_by_itag(22) # Download por "ITAG"
        stream = progresso_mp4.streams.get_highest_resolution()
        stream.download(diretorio)

        print()
        print('Download realizado com sucesso! ')

    # Função para baixar playlists 
    def playlist(progresso_playlist_mp3,progresso_playlist_mp4):

        if escolha == '1':
        
            for links in progresso_playlist_mp3.video_urls:
                try:
                    stream = YouTube(links,on_progress_callback=on_progress)
                    stream.streams.filter(only_audio=True)

                    print(f'Titulo do video: {stream.title}')
                    print('Baixando...')

                    stream_download = stream.streams.get_by_itag(140)
                    stream_download.download(diretorio)
                               
                    print()
                    print('Convertendo...')

                    lista = [filename1 for filename1 in list(path.glob('*')) if filename1.suffix =='.mp4' ] # Logica para procurar pela extensão.

                    nome1 = str(lista[0])
                    novo_nome = nome1[:-4]
                    
                    AudioSegment.from_file(nome1).export(novo_nome + '.mp3',format='mp3',bitrate='320k')
                    os.remove(nome1)
                    print('Conversão realizada com sucesso! ')

                except:
                    print(f'{stream.title}{erro.capitalize()}')

        elif escolha == '2':

            for links in progresso_playlist_mp4.video_urls:

                stream = YouTube(links,on_progress_callback=on_progress)

                print(f'Titulo do video: {stream.title} ')
                print('Baixando...')
                stream.streams.filter(adaptive=True)

                stream_download = stream.streams.get_highest_resolution()
                stream_download.download(diretorio)

                print()
                print('Download realizado com sucesso! ')
                

    try:

        print('Escolha o método de download. ')   
        escolha = input('[1] Musica [2] Video: ')
        escolha2 = input('[1] Playlist [2] Link unico: ')

        if escolha2 == '2':
            yt = input('Coloque o link aqui: ')  
        else:
            playlist1 = Playlist(input('Coloque o link aqui: '))

        if escolha == '1':
            if escolha2 == '1':
                playlist(playlist1,playlist1)

            elif escolha2 == '2':
                mp3(yt)
                
        elif escolha == '2':
            if escolha2 == '1':
                playlist(playlist1,playlist1)

            elif escolha2 == '2':
                mp4(yt)
        
        print()
        escolha1 = input('Deseja continuar?[s][n]')

        if escolha1 == 's':
            continue
        else:
            break
    except:
        print('Digite uma opção valida.')
