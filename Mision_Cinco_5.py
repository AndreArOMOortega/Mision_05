# Autor: Andrea Romo Ortega
# Misión 5 :D


import pygame
from random import randint
from math import *


def dibujarCuadradosYCirculos():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
        ventana.fill(BLANCO)
        negro = (0, 0, 0)

        for absisa in range(10, 801, 10):
            pygame.draw.rect(ventana, negro, (absisa, absisa, 800 - 2 * absisa, 800 - 2 * absisa), 1)

        for ordenada in range(10, 391, 10):
            pygame.draw.circle(ventana, negro, (ANCHO // 2, ALTO // 2), ordenada, 2)

        pygame.display.flip()
        reloj.tick(50)

    pygame.quit()


def dibujarCirculos():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    ROSA = (255, 120, 210)

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)
            angulo = 0
            for i in range(1, 13):
                absisa = 150 * cos(angulo)
                ordenada = 150 * sin(angulo)
                pygame.draw.circle(ventana, ROSA, (400 + int(absisa), 400 + int(ordenada)), 150, 2)
                angulo += pi / 6

            pygame.display.flip()
            reloj.tick(50)
    pygame.quit()


def dibujarEstrella():
    ANCHO = 800
    ALTO = 800
    BLANCO = (255, 255, 255)
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            ventana.fill(BLANCO)
            for absisa in range(0, 401, 10):
                random = (randint(0, 255), randint(0, 255), randint(0, 255))
                pygame.draw.line(ventana, random, (400, absisa), (400 + absisa, 400),
                                 1)

                pygame.draw.line(ventana, random, (400, absisa), (400 - absisa, 400),
                                 1)

                pygame.draw.line(ventana, random, (400, 800 - absisa),
                                 (400 + absisa, 400), 1)

                pygame.draw.line(ventana, random, (400, 800 - absisa),
                                 (400 - absisa, 400), 1)

            pygame.display.flip()
            reloj.tick(50)
    pygame.quit()


def aproximarPI(proxdivisor):
    suma = 0
    for d in range(1, n + 1):  # 1, 2, 3...
        fraccion = 1 / d ** 2  # hace la fraccion
        suma += fraccion

    aproxPI = (6 * suma) ** 0.5
    return aproxPI


def saberDivisibles():
    numero = 0
    for divisible in range(1000, 10000):
        if divisible % 37 == 0:
            numero += 1
    return numero


def imprimirPiramides():
    suma = 0
    for cadena in range(1, 10, 1):
        for y in range(cadena + 1, 1, -1):
            suma += (10 ** y) // 100
        print("%d * 8 + %d = %d" % (suma, cadena, suma * 8 + cadena))
    print("\n")
    for t in range(0, 9, 1):
        num = 0
        for m in range(1, t + 1, 1):
            num += 10 ** m
        num += 1
        print("%d * %d = %d" % (num, num, num * num))


def main():
    salir = False
    while not salir:
        print("""Menú Misión 5 
        Selecciona qué quiere hacer.

        1. Dibujar cuadrados y círculos
        2. Dibujar estrella
        3. Dibujar circulos
        4. Aproximar PI
        5. Contar divisibles entre 37
        6. Imprimir pirámides de números
        0. Salir""")
        respuesta = int(input("¿Qué quieres hacer? "))

        if respuesta == 1:
            dibujarCuadradosYCirculos()
        elif respuesta == 2:
            dibujarEstrella()
        elif respuesta == 3:
            dibujarCirculos()
        elif respuesta == 4:
            proxdivisor = int(input("Escribe el valor del divisor final: "))
            print("El valor aproximado de PI es:", aproximarPI(proxdivisor))
        elif respuesta == 5:
            print("Hay", saberDivisibles(), "números divisibles entre 37")
        elif respuesta == 6:
            imprimirPiramides()
        elif respuesta == 0:
            salir = True
        else:
            print("Error")


main()


