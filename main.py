
from pytube import YouTube
import time
import os
print(
    '''/////////////////// Cansado de anuncio papai //////////////'''
)
yt = YouTube(
    str(input("Cole aqui a url do Video: ")))

video = yt.streams.filter(only_audio=True).first()
  
print("Baixando..")

saida = video.download(output_path='MusicasBaixadas')

base, ext = os.path.splitext(saida)
novo_arq = base + '.mp3'
os.rename(saida, novo_arq)
  
print(yt.title + " Baixando com sucesso!")