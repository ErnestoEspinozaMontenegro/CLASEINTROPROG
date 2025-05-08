import pygame
import sys

# Inicializar pygame
pygame.init()

# Constantes de pantalla
ANCHO = 800
ALTO = 400
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Mario Bros")

# Colores
AZUL = (135, 206, 235)
ROJO = (255, 0, 0)
VERDE = (34, 139, 34)
NEGRO = (0, 0, 0)

# Reloj para controlar los FPS
clock = pygame.time.Clock()
FPS = 60

# Mario (jugador)
mario = pygame.Rect(70, 300, 40, 50)  # x, y, ancho, alto
velocidad_x = 0
velocidad_y = 0
en_el_suelo = True
GRAVEDAD = 0.5
FUERZA_SALTO = -10

# Suelo
suelo = pygame.Rect(0, 350, ANCHO, 50)

# Función principal del juego
def juego():
    global velocidad_x, velocidad_y, en_el_suelo

    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        # Teclas presionadas
        teclas = pygame.key.get_pressed()
        velocidad_x = 0

        if teclas[pygame.K_LEFT]:
            velocidad_x = -5
        if teclas[pygame.K_RIGHT]:
            velocidad_x = 5
        if teclas[pygame.K_SPACE] and en_el_suelo:
            velocidad_y = FUERZA_SALTO
            en_el_suelo = False

        # Movimiento
        mario.x += velocidad_x
        mario.y += velocidad_y
        velocidad_y += GRAVEDAD

        # Colisión con el suelo
        if mario.colliderect(suelo):
            mario.y = suelo.y - mario.height
            velocidad_y = 0
            en_el_suelo = True

        # Dibujar fondo y objetos
        PANTALLA.fill(AZUL)
        pygame.draw.rect(PANTALLA, VERDE, suelo)
        pygame.draw.rect(PANTALLA, ROJO, mario)

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Ejecutar el juego
juego()
