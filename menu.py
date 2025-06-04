import pygame
import subprocess
from control_usb import leer_boton

pygame.init()
pantalla = pygame.display.set_mode((480, 320))
fuente = pygame.font.Font(None, 40)

juegos = ['juego1.py', 'juego2.py']
seleccion = 0   # ← Esta línea es clave
corriendo = True