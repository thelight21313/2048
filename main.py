from collections import deque
import readchar
import random

class Vector:
    def __init__(self, name: str,
                 rotate_count: int, ):
        self.name = name
        self.rotate_count = rotate_count
        self.return_rotate_count = 4 - rotate_count


class Button:
    def __init__(self, button: str, vector: Vector):
        self.button = button
        self.vector = vector

    def click(self, matrix):
        matrix = matrix.rotate_matrix(self.vector.rotate_count)
        matrix = matrix.move()
        matrix = matrix.rotate_matrix(self.vector.return_rotate_count)
        return matrix


class Matrix:
    def __init__(self, matrix: list):
        self.matrix_list = matrix

    def turn(self, rotate_count):
        for i in range(rotate_count):
            self.matrix_list = [list(x) for x in zip(*self.matrix_list[::-1])]


    def rotate_matrix(self, rotate_count):
        self.turn(rotate_count)
        return self

    @staticmethod
    def delete_zeroes(array):
        array = [x for x in array if x != 0]
        return array

    def move_row_left(self, array):
        array = self.delete_zeroes(array)
        result = []
        i = 0
        while i < len(array):
            if i + 1 < len(array) and array[i] == array[i + 1]:
                result.append(array[i] * 2)
                i += 2
            else:
                result.append(array[i])
                i += 1
        array = result
        array = self.delete_zeroes(array)
        array += [0] * (4-len(array))
        return array

    def move(self):
        self.matrix_list = [self.move_row_left(row) for row in self.matrix_list]
        return self

    def print_matrix(self):
        for _ in self.matrix_list:
            print(_)
        print('')


    def get_rundom_zero(self):
        zerous = [ (r,c) for r, row in enumerate(self.matrix_list) for c, value in enumerate(row) if value == 0]
        if not zerous:
            print('YOU LOSE')
            raise 
        return random.choice(zerous)

    def spawn(self):
        r, c = self.get_rundom_zero()
        values = [2, 4]
        self.matrix_list[r][c] = random.choice(values)
        return self


up_vector = Vector("up", 3)
down_vector = Vector("down", 1)
left_vector = Vector('left', 0)
right_vector = Vector("right", 2)

up = Button(button='up', vector=up_vector)
down = Button(button="down", vector=down_vector)
left = Button(button='left', vector=left_vector)
right = Button(button="right", vector=right_vector)

start_list = [[0] * 4 for _ in range(4)]
matrix = Matrix(start_list)
matrix.spawn()
matrix.print_matrix()
while True:
    key = readchar.readkey()
    last_matrix = [row[:] for row in matrix.matrix_list]
    if key == 'w':
        up.click(matrix)
    if key == 's':
        down.click(matrix)
    if key == 'a':
        left.click(matrix)
    if key == 'd':
        right.click(matrix)
        
    matrix.print_matrix()
    if matrix.matrix_list != last_matrix:
        matrix.spawn()
        matrix.print_matrix()
    if key and last_matrix != matrix:
        matrix.spawn()
    elif key == readchar.key.ESC:
        break
