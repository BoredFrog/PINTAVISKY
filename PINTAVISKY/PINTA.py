#archivo2 - PINTA.py
from matplotlib import colors
from handtrck import *
from random import randint
import cv2
import mediapipe as mp
import numpy as np
import random
#from tkinter
import time 

#global laVariableMilagrosa
#def laFuncionMilagrosa
class textaj():
    def __init__(self, x, y, w, h, color, text='', alpha = 0.5): #se importan los objetos
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.text=text
        self.alpha = alpha
        
    
    def draw(self, img, text_color=(255,255,255), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=0.5, thickness=1):
        alpha = self.alpha
        bg_rec = img[self.y : self.y + self.h, self.x : self.x + self.w]
        white_rect = np.ones(bg_rec.shape, dtype=np.uint8)
        white_rect[:] = self.color
        res = cv2.addWeighted(bg_rec, alpha, white_rect, 1-alpha, 1.0)

        img[self.y : self.y + self.h, self.x : self.x + self.w] = res #posicionar la imagen

        tetx_size = cv2.getTextSize(self.text, fontFace, fontScale, thickness) #el tamaño y el estilo del texto
        text_pos = (int(self.x + self.w/2 - tetx_size[0][0]/2), int(self.y + self.h/2 + tetx_size[0][1]/2)) #la posición del texto
        cv2.putText(img, self.text,text_pos , fontFace, fontScale,text_color, thickness)


    def isOver(self,x,y):
        if (self.x + self.w > x > self.x) and (self.y + self.h> y >self.y):
            return True
        return False


detector = handDetector(detectionCon=0.8) #se importa el detector para las manos

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #se inicializa la camara web 
def make_1080p(): # se ajusta la resolución dependiendo de la calidad de la cámara
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

make_720p()        
change_res(1280, 720)

canvas = np.zeros((720,1280,3), np.uint8) #se crea el canvas
frame = canvas.copy()

px,py = 0,0 #la posición en la que se va a iniciar
color = (255,255,255)
pinceltmñ=5
borradortmñ=20

colors = [ ]
b = int(random.random()*255)-1
g = int(random.random()*255)
r = int(random.random()*255)
print(r,g,b)
colors.append(textaj(0,0,80,100,(255,255,255), alpha=0.5))#blanco
colors.append(textaj(80,0,80,100, (139,131,120), alpha=0.5))#gris
colors.append(textaj(160,0,80,100, (193,205,205), alpha=0.5))#claro
colors.append(textaj(240,0,80,100, (138,54,15), alpha=0.5))#marron
colors.append(textaj(320,0,80,100, (255,0,0), alpha=0.5))#rojo
colors.append(textaj(400,0,80,100, (0,0,255), alpha=0.5))#azul
colors.append(textaj(480,0,80,100,(0,255,0),alpha=0.5))#verde
colors.append(textaj(560,0,80,100, (8,255,230) ,alpha=0.5))#amarillo
colors.append(textaj(640,0,80,100, (208,7,255) ,alpha=0.5))#rosado
colors.append(textaj(720,0,80,100, (51,144,255), alpha=0.5))#naranja
colors.append(textaj(800,0,80,100, (255,1,231) ,alpha=0.5))#morado
colors.append(textaj(880,0,80,100, (82,184,9) ,alpha=0.5))#verde oscuro     
colors.append(textaj(960,0,80,100, (255,255,9), alpha=0.5))#celeste
colors.append(textaj(1040,0,80,100, (0,0,0), "borrador"))
clear = textaj(1120,0,80,100, (0,0,0), "limpiar")

tipopincel = [] 
for i, tpincel in enumerate(range(5,25,5)):
   tipopincel.append(textaj(1200,100+100*i,80,100, color, str(tpincel),alpha=0.5)) 


pizblanca = textaj(50, 100, 1040, 580, (255,255,255),alpha = 0.4) 

#botones en el programa
pincelbt = textaj(1200, 0, 80, 100, color, 'grosor', alpha=0.5)
terminadobt = textaj(1100, 588, 170, 90, (255,255,255), 'terminar', alpha=0.5)

coolingCounter = 20
ocultarpiz = False
ocultarcol = False
ocultarpin = True

start_time = time.time()
drawing = True
time_up= False 


def timer(tiempo):
    start_time = time.time()
    
while True:

    if coolingCounter:
        coolingCounter-=1

    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (1280, 720))
    frame = cv2.flip(frame, 1)

    if drawing:
        detector.findHands(frame)
        positions = detector.findposition(frame, draw=False)
        upFingers = detector.fingersup(frame)

        elapsed_time = time.time() - start_time
        if elapsed_time > 25:
            drawing = False
            time_up = True 

        if time_up:
            elapsed_time_text = "Tiempo agotado" 
            print("Funciono")
            cap.release()
            cv2.destroyAllWindows()
        else:
            elapsed_time_text = f"Tiempo: {elapsed_time:.2f}s"


    if upFingers: #dependiendo de los dedos que se encuentren en posición, se realizarán las siguientes acciones
        x,y = positions [8][0], positions[8][1]
        if upFingers[1] and upFingers[2] and not pizblanca.isOver(x, y):
            px, py = 0, 0

            if not ocultarcol:
                for cb in colors:
                    if cb.isOver(x, y):
                        color = cb.color
                        cb.alpha = 0
                    else:
                        cb.alpha = 0.5

            if not ocultarpin:
                for pincel in tipopincel:
                    if pincel.isOver(x, y):
                        pinceltmñ = int(pincel.text)
                        pincel.alpha = 0
                    else:
                        pincel.alpha = 0.5

            if clear.isOver(x, y):
                clear.alpha = 0
                canvas = np.zeros((720,1280,3), np.uint8)
            else:
                clear.alpha = 0.5
  

            if pincelbt.isOver(x, y) and not coolingCounter:
                coolingCounter = 10
                pincelbt.alpha = 0
                ocultarpin = False if ocultarpin else True
                pincelbt.text = 'pinceles' if ocultarpin else 'ocultar'
            else:
                pincelbt.alpha = 0.5    

            if terminadobt.isOver(x, y):

                print("fUNCIONO")
                cap.release()
                cv2.destroyAllWindows()
                


        elif upFingers[1] and not upFingers[2]:
            if pizblanca.isOver(x, y) and not ocultarpiz:
                cv2.circle(frame, positions[8], pinceltmñ, color,-1) 
                if px == 0 and py == 0: 
                    px, py = positions[8]
                if color == (0,0,0):
                    cv2.line(canvas, (px,py), positions[8], color,borradortmñ)
                    
                else:
                    cv2.line(canvas, (px,py), positions[8], color,pinceltmñ)
                px, py = positions[8]
        
        else:
            px, py = 0, 0  

        
        frame=cv2.bitwise_or(frame,canvas)

        """if upFingers[1] and upFingers[2]:
            if guardarbt.isOver(x, y) and not coolingCounter:
                coolingCounter = 10
                guardarbt.alpha = 0  
                i+=1
                cv2.imwrite("C:/Users/ESCRITORIO/Desktop/imagen%s.jpg" % i, canvas )
        
        else:
            guardarbt.alpha = 0.5    
        """
    pincelbt.color = color
    pincelbt.draw(frame)
    cv2.rectangle(frame, (pincelbt.x, pincelbt.y), (pincelbt.x + pincelbt.w, pincelbt.y + pincelbt.h), (255,255,255), 2)

    terminadobt.draw(frame)
    cv2.rectangle(frame, (terminadobt.x, terminadobt.y), (terminadobt.x + terminadobt.w, terminadobt.y + terminadobt.h), (255, 255, 255), 2)
 

    if not ocultarpiz:       
        pizblanca.draw(frame) 
        canvasGray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
        _, imgInv = cv2.threshold(canvasGray, 20, 255, cv2.THRESH_BINARY_INV)
        imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
        frame = cv2.bitwise_and(frame, imgInv)
        frame = cv2.bitwise_or(frame, canvas)

    if not ocultarcol: 
        for c in colors:
            c.draw(frame)
            cv2.rectangle(frame, (c.x, c.y), (c.x +c.w, c.y+c.h), (255,255,255), 2)

        clear.draw(frame)
        cv2.rectangle(frame, (clear.x, clear.y), (clear.x +clear.w, clear.y+clear.h), (255,255,255), 2)      

   
    if not ocultarpin:
        for pincel in tipopincel:
            pincel.draw(frame)
            cv2.rectangle(frame, (pincel.x, pincel.y), (pincel.x + pincel.w, pincel.y + pincel.h), (255,255,255),2)


    cv2.putText(frame, elapsed_time_text, (1020, 707), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    

    #cv2.imshow('canvas', canvas)
    cv2.imshow("virtual board",frame) 
    if (cv2.waitKey(1)  & 0xFF == ord('q')):
            break
    
cap.release()
cv2.destroyAllWindows()

