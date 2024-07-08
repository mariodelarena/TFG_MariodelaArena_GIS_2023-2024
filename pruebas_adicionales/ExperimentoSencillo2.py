from psychopy import visual, core, event

# Crear una ventana con fondo blanco
win = visual.Window([800,600], monitor="testMonitor", units="deg", color='white')

# Crear opciones de menú
opciones = ['Opción 1', 'Opción 2', 'Opción 3']
texto_opciones = visual.TextStim(win, text='\n'.join(opciones), color='black', pos=(0, 4))

# Dibujar el menú en la ventana
texto_opciones.draw()

# Mostrar la ventana
win.flip()

# Esperar a que el usuario presione una tecla
key = event.waitKeys(keyList=['1', '2', '3'])

# Mostrar la tecla presionada por el usuario
print('El usuario seleccionó: ', key)

# Dependiendo de la opción seleccionada, abrir una ventana diferente
if key[0] == '1':
    # Abrir ventana para la opción 1
    print('Abriendo ventana para la opción 1...')
elif key[0] == '2':
    # Abrir ventana para la opción 2
    print('Abriendo ventana para la opción 2...')
elif key[0] == '3':
    # Abrir ventana para la opción 3
    print('Abriendo ventana para la opción 3...')

# Cerrar la ventana
win.close()
