from display import *
from draw import *
import math

screen = new_screen()
color = [0, 0, 0]
edge_matrix = []
add_edge(edge_matrix, 0, 2, 0, 500, 0, 0)
add_edge(edge_matrix, 0, 2, 0, 500, 4, 0)
add_edge(edge_matrix, 500, 0, 0, 500, 4, 0)

scale_matrix = make_scale(0.978, 0.978, 1)
rotZ_matrix = make_rotZ(2.5)
trans_matrix = make_translate(10, 4, 0)
matrix_mult(trans_matrix, scale_matrix)
matrix_mult(scale_matrix, rotZ_matrix)
master_matrix = rotZ_matrix

for x in range(45):
    color[1] = (color[1] + 5) % 255 
    matrix_mult(master_matrix, edge_matrix)
    draw_lines(edge_matrix, screen, color)

display(screen)

