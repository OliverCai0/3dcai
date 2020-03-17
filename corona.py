from display import *
from draw import *
from parser import *
from matrix import *
from copy import deepcopy
import math
import random

screen = new_screen()
gray = [ 128,128,128]
red = [255,0,0]
orange = [255,165,0]
edges = []
transform = new_matrix()

def return_line_coordinates(x0,y0,x1,y1):
    p = []
    if x0 > x1:
        x0,x1 = x1,x0
        y0,y1= y1,y0
    if x0 == x1:
        for y in range( y1 - y0):
            p.append([x0,y0 + y])
        return p
    m = (y1 - y0)/(x1 - x0)
    for x in range(x1 - x0):
        p.append([x,(y0 + m * x)])
    return p

#red stuff on cell surface
rs = new_matrix(0,0)
#base
add_edge(rs,0,0,0,0,4,0)
add_edge(rs,0,0,0,4,2,0)
add_edge(rs,4,2,0,0,4,0)
add_point(rs,1,2,9)

five_m = make_scale(3,3,3)
matrix_mult(five_m,rs)

one = return_line_coordinates(rs[0][0],rs[0][1],
                              rs[1][0],rs[1][1])
two = return_line_coordinates(rs[2][0],rs[2][1],
                              rs[3][0],rs[3][1])
three = return_line_coordinates(rs[4][0],rs[4][1],
                                rs[5][0],rs[5][1])

for cor_set in [one,two,three]:
    for cor in cor_set:
        add_edge(rs,rs[6][0],rs[6][1],rs[6][2],cor[0],cor[1],0)

five_m = make_scale(2,2,2)
matrix_mult(five_m,rs)

x_limit = [50,450]
y_limit = [50,450]

for i in range(100):
    x = random.randint(50,400)
    y = random.randint(50,400)
    t = make_translate(x,y,0)
    redshit_copy = deepcopy(rs)
    matrix_mult(t,redshit_copy)
    draw_lines(redshit_copy,screen,red)
    #print_matrix(redshit_copy)

o_s = new_matrix(0,0)
add_sphere(o_s,0,0,0,5)

for i in range(50):
    x = random.randint(50,400)
    y = random.randint(50,400)
    t = make_translate(x,y,0)

    o_s_copy = deepcopy(o_s)
    matrix_mult(t,o_s_copy)
    draw_lines(o_s_copy,screen,orange)


#draw_lines(rs,screen,red)
parse_file( 'corona', edges, transform, screen, gray )
