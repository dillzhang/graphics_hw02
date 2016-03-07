import math


def make_translate(x, y, z):
    returner = new_matrix(4, 4)
    returner = ident(returner)
    returner[0][3] = x
    returner[1][3] = y
    returner[2][3] = z
    return returner


def make_scale(x, y, z):
    return [[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]]
    

def make_rotX(theta):
    returner = new_matrix(4, 4)
    returner = ident(returner)
    returner[1][1] = math.cos(math.radians(theta))
    returner[1][2] = math.sin(math.radians(theta)) * -1
    returner[2][1] = math.sin(math.radians(theta))
    returner[2][2] = math.cos(math.radians(theta))
    return returner


def make_rotY(theta):
    returner = new_matrix(4, 4)
    returner = ident(returner)
    returner[0][0] = math.cos(math.radians(theta))
    returner[0][2] = math.sin(math.radians(theta)) * -1
    returner[2][0] = math.sin(math.radians(theta))
    returner[2][2] = math.cos(math.radians(theta))
    return returner


def make_rotZ(theta):
    returner = new_matrix(4, 4)
    returner = ident(returner)
    returner[0][0] = math.cos(math.radians(theta))
    returner[0][1] = math.sin(math.radians(theta)) * -1
    returner[1][0] = math.sin(math.radians(theta))
    returner[1][1] = math.cos(math.radians(theta))
    return returner


def new_matrix(rows=4, cols=4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m


def print_matrix(matrix):
    for i in matrix:
        print "[" + ", ".join(str(j) for j in i) + "]"


def ident(matrix):
    returner = []
    for i in range(len(matrix)):
        temp = [0] * len(matrix)
        temp[i] = 1
        returner.append(temp)
    return returner


def scalar_mult(matrix, x):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= x


#m1 * m2 -> m2
def matrix_mult(m1, m2):
    for i in range(len(m2)):
        temp = [0] * len(m2[i])
        for j in range(len(m2[i])):
            temp[j] = (m1[j][0] * m2[i][0]) + (m1[j][1] * m2[i][1]) + (m1[j][2] * m2[i][2]) + (m1[j][3] * m2[i][3])
        m2[i] = temp

