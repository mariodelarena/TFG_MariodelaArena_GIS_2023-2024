# Importación de las librerias necesarias para el experimento.

from psychopy import visual, core, event
from psychopy.hardware.emotiv import *
# Creación de ventana
win = visual.Window([1000,800], monitor="testMonitor", units="deg", color='white')

# Creación de los textos
titulo = visual.TextStim(win, text="Actividad de Meditación", font='Times New Roman', color='black', pos=(0, 3), height=1.5)
texto_explicativo = visual.TextStim(win, text="Esta actividad de meditación consciente te ayudará a relajarte. Por favor, siéntate en un lugar cómodo y tranquilo para realizar este ejercicio.", color='black', pos=(0, 0), height=0.6)

# Creación del botón
boton_continuar = visual.Rect(win, width=4, height=1.5, fillColor='blue', lineColor='blue', pos=(0, -5))
texto_boton = visual.TextStim(win, text="Comenzar", color='white', pos=(0, -5), height=0.8)

# Implementación de la cabecera de la UBU
imagen = visual.ImageStim(win, image="cabeceraSalud.png", pos=(0, 8))
autor = visual.TextStim(win, text="Mario de la Arena del Hoyo", font='Times New Roman', color='black', pos=(8, -10), height=1)

# Creación de objeto de ratón para poder utilizarlo
mouse = event.Mouse(win=win)

# Implementación visual de los elementos creados
titulo.draw()
texto_explicativo.draw()
imagen.draw()
boton_continuar.draw()
texto_boton.draw()
autor.draw()

# Mostrar la ventana
win.flip()

# Esperar a que el usuario haga clic en el botón para continuar
while True:
    if mouse.isPressedIn(boton_continuar):
        break

# Cerrar la ventana
win.close()

# Creación de una nueva ventana con un temporizador
win_temporizador = visual.Window([1000,800], monitor="testMonitor", units="deg", color='white')
temporizador = core.CountdownTimer(10)

# Creación de texto para el temporizador
texto_temporizador = visual.TextStim(win_temporizador, text="", color='black', pos=(0, 0), height=1.2)

texto_relajacion = visual.TextStim(win_temporizador, text="Cierra los ojos y relájate", color='black', pos=(0, -4), height=0.8)

emotiv_recording = EmotivRecord(win_temporizador, "emotiv_recording")

# Funcionamiento del temporizador
while temporizador.getTime() > 0:
    # Actualizar el texto del temporizador
    texto_temporizador.text = str(int(temporizador.getTime()))
    # Dibujar el texto del temporizador y el texto de relajación
    texto_temporizador.draw()
    texto_relajacion.draw()
    # Mostrar la ventana
    win_temporizador.flip()

# Cerrar la ventana del temporizador
win_temporizador.close()

emotiv_recording.stopRecording()

# Creación de ventana
win_preg = visual.Window([1000, 800], monitor="testMonitor", units="deg", color='white')

# Creación de los textos y botones
pregunta1 = "¿Te han interrumpido durante la actividad?"
pregunta2 = "¿Cómo te encuentras después de haber realizadola actividad?"
pregunta1_texto = visual.TextStim(win_preg, text=pregunta1, color='black', pos=(0, 3), height=1)
pregunta2_texto = visual.TextStim(win_preg, text=pregunta2, color='black', pos=(0, 3), height=1)

boton_Si = visual.Rect(win_preg, width=4, height=1.5, fillColor='blue', lineColor='blue', pos=(-4, -4))
texto_Si = visual.TextStim(win_preg, text="Sí", color='white', pos=(-4, -4), height=0.8)
boton_No = visual.Rect(win_preg, width=4, height=1.5, fillColor='blue', lineColor='blue', pos=(4, -4))
texto_No = visual.TextStim(win_preg, text="No", color='white', pos=(4, -4), height=0.8)

# Creación de objeto de ratón
mouse_pregunta1 = event.Mouse(win=win_preg)
mouse_pregunta2 = event.Mouse(win=win_preg)

# Lista para almacenar respuestas
respuestas = []

# Mostrar elementos y obtener respuesta a la pregunta 1
pregunta1_texto.draw()
boton_Si.draw()
texto_Si.draw()
boton_No.draw()
texto_No.draw()
win_preg.flip()

while True:
    if mouse_pregunta1.isPressedIn(boton_Si):
        respuestas.append("Sí")
        break
    elif mouse_pregunta1.isPressedIn(boton_No):
        respuestas.append("No")
        break

# Mostrar elementos y obtener respuesta a la pregunta 2
pregunta2_texto.draw()
boton_MuyMal = visual.Rect(win_preg, width=4, height=1.5, fillColor='blue', lineColor='blue', pos=(-10, -4))
texto_MuyMal = visual.TextStim(win_preg, text="Muy Mal", color='white', pos=(-10, -4), height=0.8)

boton_Mal = visual.Rect(win_preg, width=4, height=1.5, fillColor='blue', lineColor='blue', pos=(-5, -4))
texto_Mal = visual.TextStim(win_preg, text="Mal", color='white', pos=(-5, -4), height=0.8)

boton_Normal = visual.Rect(win_preg, width=4, height=1.5, fillColor='blue', lineColor='blue', pos=(0, -4))
texto_Normal = visual.TextStim(win_preg, text="Normal", color='white', pos=(0, -4), height=0.8)

boton_Bien = visual.Rect(win_preg, width=4, height=1.5, fillColor='blue', lineColor='blue', pos=(5, -4))
texto_Bien = visual.TextStim(win_preg, text="Bien", color='white', pos=(5, -4), height=0.8)

boton_MuyBien = visual.Rect(win_preg, width=4, height=1.5, fillColor='blue', lineColor='blue', pos=(10, -4))
texto_MuyBien = visual.TextStim(win_preg, text="Muy Bien", color='white', pos=(10, -4), height=0.8)

# Implementación visual de los elementos creados
pregunta2_texto.draw()
boton_MuyMal.draw()
texto_MuyMal.draw()
boton_Mal.draw()
texto_Mal.draw()
boton_Normal.draw()
texto_Normal.draw()
boton_Bien.draw()
texto_Bien.draw()
boton_MuyBien.draw()
texto_MuyBien.draw()
win_preg.flip()

        
while True:
    if mouse_pregunta2.isPressedIn(boton_MuyMal):
        respuestas.append("Muy Mal")
        break
    if mouse_pregunta2.isPressedIn(boton_Mal):
        respuestas.append("Mal")
        break
    if mouse_pregunta2.isPressedIn(boton_Normal):
        respuestas.append("Normal")
        break
    if mouse_pregunta2.isPressedIn(boton_Bien):
        respuestas.append("Bien")
        break
    if mouse_pregunta2.isPressedIn(boton_MuyBien):
        respuestas.append("Muy bien")
        break
# Cerrar la ventana
win_preg.close()

# Imprimir las respuestas
print("Respuestas:")
for i, respuesta in enumerate(respuestas, start=1):
    print(f"Pregunta {i}: {respuesta}")