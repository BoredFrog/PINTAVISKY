from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox as mbox
from PIL import Image, ImageTk
from threading import Thread
from time import sleep
import random
import voz
import os
import subprocess 
from tkinter import Tk, Toplevel, Button

#import PINTA

# ESTABLECER FUENTE PARA TITULOS
fuente = "Roboto"
fuenteSize = 20

# PALETA DE COLORES
color_fondo = "#33202A"
color_fondo_claro = "#5F5566"
color_especial = "#FFCD2F"
color_fuente = "#C3979F"
color_verde = "#89937C"



#VARIABLES IMPORTANTES
dibujo = "" #Este es el dibujo seleccionado para dibujar (Respuesta correcta)
arrayDibujos = ["ABEJA","ELEFANTE","JIMMY","GATO","PERRO","YONERWIN","ZAPATO","PINGUINO","TREN","CASCADA","FOSSI","CAPITAN AMERICA","GALLINA","BICICLETA","ANGRY BIRDS","METEORO"] #Array para sacar opciones
puntosP1 = 0
puntosP2 = 0
turno = TRUE #True = P1 ---- False = P2

micEncendido = False
jugadorAcerto = False
botonActivo = True
# FUNCIONES


def nuevaRonda(resultado):
    global puntosP1
    global puntosP2
    #CAMBIAR COLOR DE TEXTOS
    anunciador.config(fg=color_fondo)
    palabraDibujar.config(fg=color_fondo)
    if(resultado):
        if (turno):
            puntosP2 += 1
        else:
            puntosP1 += 1
    #CAMBIAR TEXTO
    label_p1.config(text="P1 - "+str(puntosP1))
    label_p2.config(text="P2 - "+str(puntosP2))
    print("puntos p1 = " + str(puntosP1))
    print("puntos p2 = " + str(puntosP2))

def creditos():
    crearCreditos()
#! PAPIAR ESTO


def pausar():
    global puntosP1
    global puntosP2
    puntosP2 = 0
    puntosP1 = 0
    label_p1.config(text="P1 - "+str(puntosP1))
    label_p2.config(text="P2 - "+str(puntosP2))

def seleccionarPalabra():
    global dibujo
    global anunciador
    global palabraDibujar
    global boton_jugar
    global botonActivo
    sleep(4)
    palabraDibujar.config(fg=color_especial)
    anunciador.config(text="La palabra a dibujar es...")
    palabraDibujar.config(text=dibujo)
    botonActivo = True
    Thread(target=pasarNairuma).start()

def inicializar():
    global arrayDibujos5
    global dibujo
    global turno
    global botonActivo
    #Seleccionar Palabra
    if botonActivo:
        dibujo = random.choice(arrayDibujos)
        print(dibujo)
        anunciador.config(fg=color_fuente)
        if (turno):
            anunciador.config(text="Comienza a jugar... P1!")
            turno = FALSE
        else:
            anunciador.config(text="Comienza a jugar... P2!")
            turno = TRUE
        Thread(target=seleccionarPalabra).start()
        botonActivo = False

def pasarNairuma():
    global wind
    global windo
    sleep(2)
    print("Ahora se cierra la pagina y se abre la de Nairuma")
    #import PINTA as pinta  2DO CHANCE
    
    wind.withdraw()
    global dibujo
    global puntosP1
    global puntosP2
    subprocess.run(["python", "PINTA.py"])
    print("Rauw Alejandro")
    crearVentanisky()

#FUNCIONES DE LA VISTA 2 ################################################################################################
##############################################################################################################

def preRecord():
    Thread(target=grabarVoz).start() #Vainacion

def stopMic():
    global micEncendido
    global botonGrabar
    global micOff
    micEncendido = False
    botonGrabar.config(image=micOff)
    Thread(target=voz.quit()).start()

def grabarVoz():
    global micEncendido
    global botonGrabar
    bloquearTexto()
    if micEncendido:
        #FUNCION APARTE
        stopMic()
        insertarTexto(voz.textoVoz) 
    else:
        voz.textoVoz = ""
        micEncendido = True
        botonGrabar.config(image=micOn)
        Thread(target=voz.grabarVoz()).start()

        #stopMic()

texto_habilitado= True
def bloquearTexto():
    global texto_habilitado
    if(texto_habilitado):
        text.config(state=DISABLED)
        texto_habilitado = False
    else:
        text.config(state=NORMAL)
        texto_habilitado=True

def limpiarTexto():
    text.delete(0,END)

def insertarTexto(texto):
    text.insert(END,texto)

def pasarAnagrey():
    global jugadorAcerto
    sleep(2)
    print("Ahora se cierra la pagina y se abre la de anagrey")
    resultado.config(fg=color_fondo)
    global wind
    wind.deiconify()
    global windo
    windo.destroy()
    nuevaRonda(jugadorAcerto)

# ICONO DE ENVIO
def enviarTexto():
    global dibujo
    global puntosJugador1
    global puntosJugador2
    global jugadorAcerto
    print("El dibujo que intentas adivinar es " + str(dibujo))
    respuesta = text.get()
    respuesta = respuesta.upper()
    if (respuesta == dibujo):
        resultado.config(text="Correcto! Tu equipo obtiene un punto!",fg=color_fuente)
        jugadorAcerto = TRUE
        #COMPROBACION PARA SUMAR PUNTOS
    else:
        resultado.config(text="Incorrecto... La palabra era: " + dibujo,fg=color_fuente)
        jugadorAcerto = FALSE
    #TIMER
    Thread(target=pasarAnagrey).start()
    limpiarTexto()
    #sleep(4) ESTO SE LLAMA EN OTRA FUNCION CON THREAD Y LUEGO PASAR A LA VISTA DE ANAGREY Y SUMAR PUNTOS    
#? ----------------------------------------------------------------------------------------------------------------------------------------------

def crearCreditos():

    # INICIALIZAR LA VENTANA
    windc = Toplevel(wind)
    windc.geometry("1200x660")
    windc.title("PINTAVISKY - Creditos")

    windc.config(background=color_fondo)

    my_frame = Frame(windc,bg=color_fondo)
    my_frame.pack(pady=20)

    titulo = Label(my_frame, text="DESARROLLADO POR:", font=("showcard gothic", 45,"italic"), fg=color_especial, bg=color_fondo,justify=LEFT)
    titulo.pack()

    willy = Label(my_frame, text="William Serpente", font=("fuente", 45), fg="#7698DA", bg=color_fondo,justify=LEFT)
    willy.pack(pady=40)

    nai = Label(my_frame, text="Nairuma Fernández", font=("fuente", 45), fg="#92C940", bg=color_fondo,justify=LEFT)
    nai.pack(pady=40)

    ana = Label(my_frame, text="Anagrey Briceño", font=("fuente", 45), fg="#FD2468", bg=color_fondo,justify=LEFT)
    ana.pack(pady=40)

    

def crearVentanisky():

    # INICIALIZAR LA VENTANA
    global windo
    global wind
    windo = Toplevel(wind)
    windo.geometry("1200x660")
    windo.title("PINTAVISKY")

# IMAGENES
    global micOff
    img_micOff = Image.open('./assets/microfono.png')
    img_micOff = img_micOff.resize((100, 100))
    micOff = ImageTk.PhotoImage(img_micOff)

    global micOn
    img_micOn = Image.open('./assets/micOn.png')
    img_micOn = img_micOn.resize((100, 100))
    micOn = ImageTk.PhotoImage(img_micOn)

    global interrogacion
    img_interrogacion = Image.open('./assets/interrogacion.png')
    img_interrogacion = img_interrogacion.resize((200, 200))
    interrogacion = ImageTk.PhotoImage(img_interrogacion)

    global enviar
    img_enviar = Image.open('./assets/enviar.png')
    img_enviar = img_enviar.resize((150, 150))
    enviar = ImageTk.PhotoImage(img_enviar)

    windo.config(background=color_fondo)

    my_frame = Frame(windo)
    my_frame.pack(pady=20)

    titulo = Label(my_frame, text="Adivina cuál fue el dibujo...", font=("showcard gothic", 45,"italic"), fg=color_especial, bg=color_fondo,justify=LEFT)
    titulo.pack()

    my_frameBase = Frame(windo)
    my_frameBase.pack()

    img_center = Label(my_frameBase,image=interrogacion,bg=color_fondo)
    img_center.pack()

    my_frame2 = Frame(windo,bg=color_fondo)
    my_frame2.pack(pady=20)

    global text
    text = Entry(my_frame2, bg=color_fondo_claro, font=(fuente, 32,"bold"), insertbackground=color_fondo, width=20,justify=CENTER, fg=color_especial,selectbackground=color_verde)
    text.pack(side=LEFT)

    global botonGrabar
    botonGrabar = Button(my_frame2, bd=0, font=(fuente, 12), image=micOff, fg="black",bg=color_fondo, command=preRecord, cursor="hand2")
    botonGrabar.pack(side=LEFT, padx=10)

    global botonEnviar
    botonEnviar = Button(my_frame2, bd=0, font=(fuente, 12), image=enviar, fg="black",bg=color_fondo,activebackground=color_fondo, command=enviarTexto, cursor="hand2")
    botonEnviar.pack(side=LEFT, padx=10)

    my_frame3 = Frame(windo)
    my_frame3.pack(pady=10)

    global resultado
    resultado = Label(my_frame3, text="Correcto! Tu equipo obtiene un punto!", font=(fuente, 40,"italic"), fg=color_fondo, bg=color_fondo)
    resultado.pack(side=RIGHT)

    my_frame4 = Frame(windo)
    my_frame4.pack(pady=10)

    #global descripcion
    #descripcion = Label(my_frame4, text="P2                                                             ", font=("showcard gothic", 50,"italic"), fg=color_fuente, bg=color_fondo,justify=LEFT)
    #descripcion.pack(side=LEFT)



    #my_menu = Menu(windo)
    #windo.config(menu=my_menu)

    #windo.mainloop()

#crearVentana()

# INICIALIZAR LA VENTANA
def crearVentana():
    global wind
    wind = Tk()
    wind.geometry("1200x660")
    wind.title("PINTAVISKY")

# IMAGENES
    logo = Image.open('./assets/logo.png')
    logo = logo.resize((600, 200))
    logo = ImageTk.PhotoImage(logo)

    botonNew = Image.open('./assets/botonNew.png')
    botonNew = botonNew.resize((150, 150))
    botonNew = ImageTk.PhotoImage(botonNew)

    botonPausa = Image.open('./assets/botonPausa.png')
    botonPausa = botonPausa.resize((150, 150))
    botonPausa = ImageTk.PhotoImage(botonPausa)

    botonCred = Image.open('./assets/botonCreditos.png')
    botonCred = botonCred.resize((150, 150))
    botonCred = ImageTk.PhotoImage(botonCred)

    #img_micOn = Image.open('./assets/micOn.png')
    #img_micOn = img_micOn.resize((100, 100))
    #micOn = ImageTk.PhotoImage(img_micOn)


    #img_enviar = Image.open('./assets/enviar.png')
    #img_enviar = img_enviar.resize((100, 100))
    #enviar = ImageTk.PhotoImage(img_enviar)




    wind.config(background=color_fondo)

    my_frame = Frame(wind)
    my_frame.pack(pady=20)

    loguito= Label(my_frame, image=logo, font=(fuente, 35,"bold"), fg=color_verde, bg=color_fondo, pady=20)
    loguito.pack()

    my_frameBase = Frame(wind,bg=color_fondo)
    my_frameBase.pack()

    global boton_pausa
    boton_pausa = Button(my_frameBase,bd=0,image=botonPausa, font=(fuente, 12), fg=color_verde, bg=color_fondo,activebackground=color_fondo, command=pausar, cursor="hand2")
    boton_pausa.pack(side=LEFT)

    global boton_jugar
    boton_jugar = Button(my_frameBase,bd=0,image=botonNew, font=(fuente, 12), fg=color_verde, bg=color_fondo,activebackground=color_fondo, command=inicializar, cursor="hand2")
    boton_jugar.pack(side=LEFT,padx=90)

    global boton_cred
    boton_cred = Button(my_frameBase,bd=0,image=botonCred, font=(fuente, 12), fg=color_verde, bg=color_fondo,activebackground=color_fondo, command=creditos, cursor="hand2")
    boton_cred.pack(side=LEFT)

    my_frame2 = Frame(wind,bg=color_fondo)
    my_frame2.pack(pady=20)

    global label_p1
    label_p1 = Label(my_frame2,text="P1 - "+str(puntosP1), bg=color_fondo_claro, font=(fuente, 32,"bold"), width=20,justify=CENTER, fg=color_fuente)
    label_p1.pack(side=LEFT)

    global label_p2
    label_p2 = Label(my_frame2,text="P2 - "+str(puntosP2), bg=color_fondo_claro, font=(fuente, 32,"bold"),width=20,justify=CENTER, fg=color_fuente)
    label_p2.pack(side=RIGHT)

    #botonGrabar = Button(my_frame2, bd=0, font=(fuente, 12), image=micOff, fg="black", command=preRecord, cursor="hand2")
    #botonGrabar.pack(side=LEFT, padx=10)

    my_frame3 = Frame(wind)
    my_frame3.pack(pady=10)

    global anunciador
    anunciador = Label(my_frame3, text="Comienza a jugar... P1!", font=(fuente, 40,"italic"), fg=color_fondo, bg=color_fondo)
    anunciador.pack(side=RIGHT)

    my_frame4 = Frame(wind)
    my_frame4.pack()

    global palabraDibujar
    palabraDibujar = Label(my_frame4, text="ABEJA", font=("showcard gothic", 45,"italic"), fg=color_fondo, bg=color_fondo,justify=LEFT)
    palabraDibujar.pack(side=LEFT)



    my_menu = Menu(wind)
    wind.config(menu=my_menu)

    wind.mainloop()


crearVentana()


#################### CREACION DE LA VISTA 2 ##################################################################################################
###########################################################################################################################################

