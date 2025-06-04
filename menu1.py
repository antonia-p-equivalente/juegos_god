# menu.py
import pygame
import subprocess
from control_usb import leer_boton

pygame.init()
pantalla = pygame.display.set_mode((480, 320))  # Ajusta si tu pantalla es diferente
fuente = pygame.font.Font(None, 40)

juegos = ['juego1.py', 'juego2.py']
seleccion = 0
corriendo = True

def dibujar_menu():
    pantalla.fill((0, 0, 0))
    for i, juego in enumerate(juegos):
        color = (255, 255, 0) if i == seleccion else (150, 150, 150)
        texto = fuente.render(juego, True, color)
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
        subprocess.run(["python3", juegos[seleccion]])
    elif evento == "MENU":
        corriendo = False

    pygame.time.wait(100)