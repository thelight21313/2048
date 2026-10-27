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
        return self.matrix_list


    def rotate_matrix(self, rotate_count):
        self.matrix_list = self.turn(rotate_count)
        return self

    @staticmethod
    def delete_zeroes(array):
        array = [x for x in array if x != 0]
        return array

    def move_row_left(self, array):
        array = self.delete_zeroes(array)
        for el in range(len(array), 1, -1):
            if array[el] == array[el - 1]:
                array[el] *= 2
                array[el - 1] = 0
        array = self.delete_zeroes(array)
        array += [0] * (4-len(array))
        return array

    def move(self):
        self.matrix_list = [self.move_row_left(row) for row in self.matrix_list]
        return self.matrix_list

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
print(start_list)
while True:
    key = readchar.readkey()
    if key:
        last_matrix = matrix
    if key == 'w':
        up.click(matrix)
        matrix.print_matrix()
    if key == 's':
        down.click(matrix)
        matrix.print_matrix()
    if key == 'a':
        left.click(matrix)
        matrix.print_matrix()
    if key == 'd':
        right.click(matrix)
        matrix.print_matrix()
    if key and last_matrix != matrix:
        matrix.spawn()
    elif key == readchar.key.ESC:
        break