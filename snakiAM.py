
""" Juego de la Viborita (Snake Game)
Autor: Andy y Gael Waso
Fecha: 30/oct/2025

Este programa implementa un pequeño juego de la viborita usando la librería turtle.
El jugador mueve la serpiente con las flechas del teclado para comer la comida roja
y crecer, evitando chocar contra las paredes o su propio cuerpo.


"""


"""NUESTRA VERSION MODIFICADA DE VIBORITA
Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""
"""CAMBIOS GAEL WASO, AGREGAR FUNCION CHOICE"""
from random import randrange,choice
from turtle import *

from freegames import square, vector
"""


->  Randrange es para generar numeros aleatoriamente de donde estara la comida
-> turtle es la libreria
-> vector es direccion mas direccion



NOTA: la comida siempre comienza en 0,0 por que despues le generará un numero aleatorio
las coordenadas están en X y Y
el aim es donde va a caminar
y la snake comienza en 10,0


"""

"""CAMBIOS GAEL WASO, AGREGAR LISTA DE COLORES"""
colors =['black','green','blue','yellow','purple']
"""--------FIN CAMBIOS GAEL WASO----------"""

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)




"""CAMBIOS GAEL WASO, ELEGIR COLORES RANDOM"""
snake_color = choice(colors)
available_food_colors = [c for c in colors if c != snake_color]
food_color = choice(available_food_colors)
"""-----FIN CAMBIOS GAEL WASO------"""





def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

""" para que no se slga de los limites"""


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()


#CAMBIOS GAEL WASO, AGREGAR COLOR RANDOM A VIBORA Y COMIDA

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)



    update()
    ontimer(move, 100)

"""
"""
"""
"""
"""
 COMEINZAN LOS CAMBIOS DE ANDY
"""
"""
"""
""" 
"""

def move_food():
    """Mueve la comida a una nueva posición aleatoria cada segundo."""
    food.x = randrange(-15, 15) * 10
    food.y = randrange(-15, 15) * 10
    ontimer(move_food, 1000)









setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()

"""
"""
"""
CAMBIO DE ANDY CON EL MOVE FOOD
"""
"""
"""
move_food()
done()
