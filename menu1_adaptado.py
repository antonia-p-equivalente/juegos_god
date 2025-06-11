# menu adaptado para juegos en carpetas específicas
import pygame
import subprocess
from control_usb import leer_boton
import os

pygame.init()
pantalla = pygame.display.set_mode((480, 320))
fuente = pygame.font.Font(None, 40)

# Nombres de carpetas y archivos principales por juego
juegos = [
    ("anathema", "anathema_adaptado_botones.py"),
    ("juego2", "main.py")
]

seleccion = 0
corriendo = True

def dibujar_menu():
    pantalla.fill((0, 0, 0))
    for i, (nombre, _) in enumerate(juegos):
        color = (255, 255, 0) if i == seleccion else (150, 150, 150)
        texto = fuente.render(nombre, True, color)
        pantalla.blit(texto, (100 + i * 200, 150))
    pygame.display.flip()

while corriendo:
    dibujar_menu()
    evento = leer_boton()

    if evento == "LEFT":
        seleccion = (seleccion - 1) % len(juegos)
    elif evento == "RIGHT":
        seleccion = (seleccion + 1) % len(juegos)
    elif evento == "A":
        carpeta, archivo = juegos[seleccion]
        ruta = os.path.join(carpeta, archivo)
        if os.path.exists(ruta):
            subprocess.run(["python3", ruta])
        else:
            print(f"No se encontró el archivo: {ruta}")
    elif evento == "MENU":
        corriendo = False

    pygame.time.wait(100)
