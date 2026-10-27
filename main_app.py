from collections import deque

class Vector:
    def __init__(self, name: str,
                rotate_count: int,):
        self.name = name
        self.rotate_count = rotate_count
        self.return_rotate_count= 4-rotate_count



class Button:
    def __init__(self, button: str, vector:Vector):
        self.button = button
        self.vector = vector

    def click(self, complex_array: deque):
        for i in range (self.vector.rotate_count):
            Matrix.rotate(complex_array)
        for array in complex_array:
            self.move(array)
        for i in range(self.vector.return_rotate_count):
            Matrix.rotate(complex_array)
        return complex_array

    @staticmethod
    def move(array: deque):
        for el in range(1, len(array)):
            if array[el] == array[el-1]:
                array[el] = el*2
                array[el-1] = 0
        return array


class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

        
    @staticmethod
    def rotate(matrix):
        rotated = [list(x) for x in zip(*matrix[::-1])]
        return rotated


up_vector = Vector("up", 3)
down_vector = Vector("down", 1)
left_vector = Vector('left', 0)
right_vector = Vector("right", 2)

up = Button(button='up',  vector=up_vector)
down = Button(button="down", vector=down_vector)
left = Button(button='left', vector=left_vector)
right = Button(button="right", vector=right_vector)



deque_list = [[0]*4]*4
up.click(deque_list)
print(deque_list)