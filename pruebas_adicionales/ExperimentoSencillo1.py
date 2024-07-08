from psychopy import visual, core, event

# Crear una ventana con fondo blanco
win = visual.Window([800,600], monitor="testMonitor", units="deg", color='white')

# Crear un texto de instrucción en la parte superior de la pantalla
instrucciones = visual.TextStim(win, text="Por favor, pulsa una tecla para continuar", color='black', pos=(0, 4))

# Dibujar el texto en la ventana
instrucciones.draw()

# Mostrar la ventana
win.flip()

# Esperar a que el usuario presione una tecla
key = event.waitKeys()

# Mostrar la tecla presionada por el usuario
print('El usuario presionó: ', key)

# Cerrar la ventana
win.close()