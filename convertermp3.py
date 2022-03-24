from os import *
from pydub import AudioSegment
from pathlib import *

home = Path.home()
desktop = home / 'desktop'

path = Path(desktop)

for filename1 in listdir(desktop):
   
    for filename1 in path.glob('*'):
        if filename1.suffix == '.webm':
            nome1 = str(filename1)
           
novo_nome = nome1[:-5]

AudioSegment.from_file(nome1).export(novo_nome + '.mp3',format='mp3',bitrate='320k')