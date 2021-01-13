from tkinter import filedialog
from tkinter import *
import os
import pytube

# Ventana main
ventana = Tk()
ventana.title('akaDownloader')
ventana.minsize(540, 480)
ventana.resizable(0, 0)

# Ruta default
carpeta_default = "C:/Users/danie/Desktop/YoutubeDownloader/videos"
global url, notif_descarga, notif_carpeta

url = StringVar()
notif_descarga = Label(ventana,font=("Calibri",12))
notif_carpeta= Label(ventana,font=("Calibri",8))


# Funciones
def descargar_video():
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

def descargar_playlist():
    playlist_url = url.get()
    playlist = pytube.contrib.playlist.Playlist(playlist_url)
    playlist_list = playlist.video_urls
    for videoUrl in playlist_list:
        try:
            yt = pytube.YouTube(videoUrl)
            titulo = yt.title
            video = yt.streams.first()
            descarga = video.download(carpeta_default)

            archivo_nuevo = titulo
            os.chdir(carpeta_default)
            os.rename(descarga, archivo_nuevo)
            notif_descarga.config(fg="green", text="La descarga fue exitosa")
        except Exception as e:
            print(e)
            notif_descarga.config(fg="red", text="No se completó la descarga")

def descargar_captions():
    return False

def cambiar_carpeta_default():
    global carpeta_default
    carpeta_default = filedialog.askdirectory()
    notif_carpeta.config(fg="green", text=carpeta_default)

# Pantallas
def limpiar():
    contenido = ventana.grid_slaves()
    for c in contenido:
        c.grid_remove()

def home():
    limpiar()

    home_label = Label(ventana, text="Inicio")
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=230,
        pady=7
    )
    home_label.grid(row=0, column=0, columnspan=12)

    Label(ventana, text="Descargar video", fg="red", font=("Calibri", 15, "bold")).grid(sticky=NW,padx=10, row=3)
    Label(ventana, text="Ingrese el link del video a descargar", font=("Calibri", 10, "bold")).grid(sticky=NW, row=4, padx=10, pady=5)
    url = StringVar()
    Entry(ventana, width=50, textvariable=url).grid(sticky=NW, padx=10, row=5)
    Button(ventana,width=20,text="Download",font=("Calibri",12),command=descargar_video).grid(sticky=NW,row=6, padx=10, pady=5)

    Label(ventana, text="Descargar playlist", fg="red", font=("Calibri", 15, "bold")).grid(sticky=NW,padx=10, row=7)
    Label(ventana, text="Ingrese el link del video a descargar", font=("Calibri", 10, "bold")).grid(sticky=NW, row=8, padx=10, pady=5)
    url = StringVar()
    Entry(ventana, width=50, textvariable=url).grid(sticky=NW, padx=10, row=9)
    Button(ventana,width=20,text="Download",font=("Calibri",12),command=descargar_playlist).grid(sticky=NW,row=10, padx=10, pady=5)

    Label(ventana, text="Descargar subtítulos", fg="red", font=("Calibri", 15, "bold")).grid(sticky=NW,padx=11, row=11)
    Label(ventana, text="Ingrese el link del video a descargar", font=("Calibri", 10, "bold")).grid(sticky=NW, row=12, padx=10, pady=5)
    url = StringVar()
    Entry(ventana, width=50, textvariable=url).grid(sticky=NW, padx=10, row=13)
    Button(ventana,width=20,text="Download",font=("Calibri",12),command=descargar_captions).grid(sticky=NW,row=14, padx=10, pady=5)

    #Notification descarga
    notif_descarga = Label(ventana,font=("Calibri",12))
    notif_descarga.grid(sticky=N,pady=1,row=4)

    #Choose path
    Label(ventana,text="Cambiar carpeta de destino",font=("Calibri", 10, "bold")).grid(sticky=NW,row=16, padx=10)
    Button(ventana,width=20,text="Elegir carpeta",font=("Calibri",12),command=cambiar_carpeta_default).grid(sticky=NW,row=17, padx=10, pady=5)

    #Notification Path
    notif_carpeta= Label(ventana,font=("Calibri",8))
    notif_carpeta.grid(sticky=N,row=18,pady=15)


def ayuda():
    limpiar()

    ayuda_label = Label(ventana, text="Ayuda")
    ayuda_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=219,
        pady=7
    )
    ayuda_label.grid(row=0, column=0, columnspan=12)

def info():
    limpiar()

    info_label = Label(ventana, text="Info")
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 20),
        padx=242,
        pady=7
    )
    info_label.grid(row=0, column=0, columnspan=12)

# Cargo pantalla de inicio
home()

# Menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Ayuda", command=ayuda)
menu_superior.add_command(label="Info", command=info)

# Cargo menu
ventana.config(menu=menu_superior)

ventana.mainloop()