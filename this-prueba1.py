from tkinter import filedialog
from tkinter import *
import tkinter as tk
import os
import pytube

# Ventana main
ventana = Tk()
ventana.title('akaDownloader')
ventana.minsize(540, 420)
ventana.resizable(0, 0)
ventana.iconbitmap('C:/Users\danie\Desktop\YoutubeDownloader\logo.ico')
ventana.configure(bg='#2E2D2C')

# Ruta default
carpeta_default = "C:/Users/danie/Desktop/YoutubeDownloader/videos"

# Funciones
def descargar_video_video():
    try:
        video_url = url.get()
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        titulo = youtube.title
        descarga = video.download(carpeta_default)

        archivo_nuevo = titulo+'.mp4'
        os.chdir(carpeta_default)
        os.rename(descarga, archivo_nuevo)
        notif_descarga.config(fg="green", text="La descarga fue exitosa")
    except Exception as e:
        print(e)
        notif_descarga.config(fg="red", text="No se completó la descarga")

def descargar_video_audio():
    try:
        video_url = url.get()
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.filter(only_audio=True).first()
        titulo = youtube.title
        descarga = video.download(carpeta_default)

        archivo_nuevo = titulo+'.mp3'
        os.chdir(carpeta_default)
        os.rename(descarga, archivo_nuevo)
        notif_descarga.config(fg="green", text="La descarga fue exitosa")
    except Exception as e:
        print(e)
        notif_descarga.config(fg="red", text="No se completó la descarga")

def descargar_playlist_video():
    playlist_url = url.get()
    playlist = pytube.contrib.playlist.Playlist(playlist_url)
    playlist_list = playlist.video_urls
    for videoUrl in playlist_list:
        try:
            yt = pytube.YouTube(videoUrl)
            titulo = yt.title
            video = yt.streams.first()
            descarga = video.download(carpeta_default)

            archivo_nuevo = titulo+'.mp4'
            os.chdir(carpeta_default)
            os.rename(descarga, archivo_nuevo)
            notif_descarga.config(fg="green", text="La descarga fue exitosa")
        except Exception as e:
            print(e)
            notif_descarga.config(fg="red", text="No se completó la descarga")

def descargar_playlist_audio():
    playlist_url = url.get()
    playlist = pytube.contrib.playlist.Playlist(playlist_url)
    playlist_list = playlist.video_urls
    for videoUrl in playlist_list:
        try:
            yt = pytube.YouTube(videoUrl)
            titulo = yt.title
            video = yt.streams.filter(only_audio=True).first()
            descarga = video.download(carpeta_default)

            archivo_nuevo = titulo+'.mp3'
            os.chdir(carpeta_default)
            os.rename(descarga, archivo_nuevo)
            notif_descarga.config(fg="green", text="La descarga fue exitosa")
        except Exception as e:
            print(e)
            notif_descarga.config(fg="red", text="No se completó la descarga")

def descargar_captions():
    return False

def cambiar_carpeta_default():
    carpeta_default = filedialog.askdirectory()
    notif_carpeta.config(fg="green", text=carpeta_default)

# Pantalla main
home_label = Label(ventana, text="akaDownloader")
home_label.config(
    fg="red",
    # bg="black",
    bg="#1F1E1D",
    font=("Arial", 20),
    padx=176,
    pady=7
)
home_label.grid(row=0, column=0, columnspan=12)

Label(ventana, text="Descargar video", fg="red", font=("Calibri", 15, "bold"), bg='#2E2D2C').grid(sticky=NW, padx=200, row=3, column = 0)
Label(ventana, text="Ingrese el link del video a descargar", font=("Calibri", 10, "bold"), bg='#2E2D2C', fg='white').grid(sticky=NW, row=4, padx=10, pady=5)
url = StringVar()
Entry(ventana, width=50, textvariable=url).grid(sticky=NW, padx=10, row=5)
# Button(ventana, width=20,text="Download",font=("Calibri",12),command=descargar_video).grid(sticky=NW, row=6, padx=10, pady=5) this
Button(ventana, width=15,text="Descargar video",font=("Calibri",12),command=descargar_video_video).grid(sticky=NW, row=6, padx=10, pady=5)
Button(ventana, width=15,text="Descargar audio",font=("Calibri",12),command=descargar_video_audio).grid(sticky=NW, row=6, padx=150, pady=5)

Label(ventana, text="Descargar playlist", fg="red", font=("Calibri", 15, "bold"), bg='#2E2D2C').grid(sticky=NW, padx=190, row=7)
Label(ventana, text="Ingrese el link de la playlist a descargar", font=("Calibri", 10, "bold"), bg='#2E2D2C', fg='white').grid(sticky=NW, row=8, padx=10, pady=5)
url = StringVar()
Entry(ventana, width=50, textvariable=url).grid(sticky=NW, padx=10, row=9)
# Button(ventana, width=20,text="Download",font=("Calibri",12),command=descargar_playlist_video).grid(sticky=NW, row=10, padx=10, pady=5)
Button(ventana, width=15,text="Descargar video",font=("Calibri",12),command=descargar_playlist_video).grid(sticky=NW, row=10, padx=10, pady=5)
Button(ventana, width=15,text="Descargar audio",font=("Calibri",12),command=descargar_playlist_audio).grid(sticky=NW, row=10, padx=150, pady=5)

Label(ventana, text="Descargar subtítulos", fg="red", font=("Calibri", 15, "bold"), bg='#2E2D2C').grid(sticky=NW, padx=180, row=11)
Label(ventana, text="Ingrese el link del video a descargar los subtítulos", font=("Calibri", 10, "bold"), bg='#2E2D2C', fg='white').grid(sticky=NW, row=12, padx=10, pady=5)
url = StringVar()
Entry(ventana, width=50, textvariable=url).grid(sticky=NW, padx=10, row=13)
# Button(ventana, width=20,text="Download",font=("Calibri",12),command=descargar_captions).grid(sticky=NW, row=14, padx=10, pady=5)
Button(ventana, width=15,text="Descargar",font=("Calibri",12),command=descargar_captions).grid(sticky=NW, row=14, padx=10, pady=5)

#Notification descarga
notif_descarga = Label(ventana,font=("Calibri",12), bg='#2E2D2C')
notif_descarga.grid(sticky=NW, padx=180, pady=1,row=19)

#Choose path
Label(ventana,text="Cambiar carpeta de destino",font=("Calibri", 10, "bold"), bg='#2E2D2C', fg='white').grid(sticky=NW,row=16, padx=10)
Button(ventana,width=15,text="Elegir carpeta",font=("Calibri",12),command=cambiar_carpeta_default).grid(sticky=NW,row=17, padx=10, pady=5)

#Notification Path
notif_carpeta= Label(ventana,font=("Calibri",8), bg='#2E2D2C')
notif_carpeta.grid(sticky=NW,row=18,pady=15, padx=10)

footer_label = Label(ventana, text="Seguime en mis redes sociales")
footer_label.config(
    fg="white",
    bg="black",
    font=("Arial", 9),
    padx=182,
    pady=2
)
footer_label.grid(sticky=S, row=20, column=0, columnspan=12)

social_label = Label(ventana, text="git @akalautaro | linkedin Lautaro Celli | twitter @akalautaro")
social_label.config(
    height = 1,
    fg="orange", 
    bg="black", 
    padx = 53,
    font = ("Consolas", 10)
)
social_label.grid(sticky=S,row=21, column=0, columnspan=12)

ventana.mainloop()