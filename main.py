from display import *
from draw import *
import math

translate_matrix = make_translate(-60, 60, 0)
scale_matrix = make_scale(1.2, .8, 0)
rotX_matrix = make_rotX(45)
rotY_matrix = make_rotY(45)
rotZ_matrix = make_rotZ(45)

transformations = [translate_matrix, scale_matrix, rotX_matrix, rotY_matrix, rotZ_matrix]

for x in transformations:
    screen = new_screen()
    color = [255, 255, 255]
    edge_matrix = []
    
    add_edge(edge_matrix, 250, 200, 0, 250, 250, 0)
    add_edge(edge_matrix, 250, 200, 0, 300, 200, 0)
    add_edge(edge_matrix, 250, 250, 0, 300, 250, 0)
    add_edge(edge_matrix, 300, 250, 0, 300, 200, 0)
    draw_lines(edge_matrix, screen, color)

    matrix_mult(x, edge_matrix)
    color = [0, 255, 0]
    draw_lines(edge_matrix, screen, color)
    display(screen)

