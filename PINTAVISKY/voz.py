import speech_recognition as sr
from time import sleep

r= sr.Recognizer()

go = 0
textoVoz = ""

def quit():
    global go
    print("Saliendo...")
    go = 0

def grabarVoz():
    global go
    global textoVoz
    go = 1
    print("Hola")
    while go:
        try:
            sleep(0.01)
            with sr.Microphone() as source:
                print("Habla...")
                r.adjust_for_ambient_noise(source) #Esto si es importante para colocarlo Anagrey
                audio = r.listen(source)
         
                text= r.recognize_google(audio)
                print("Funciona el try/catch")
                print("Has dicho: {}".format(text))
                textoVoz += format(text)
                    #   FUTURO UPDATE CAMBIAR PRINT A UNA GLOBAL VARIABLE Y LUEGO HACER REFERENCIA A ESTA EN METAVISKY.PY
                    #   OTRA OPCION: LLAMAR FUNCION Y PASARLE DE VALOR EL PRINT DE ARRIBA
                    #   FUTURO UPDATE CAMBIAR PRINT A UNA GLOBAL VARIABLE Y LUEGO HACER REFERENCIA A ESTA EN METAVISKY.PY
        except:
            pass

