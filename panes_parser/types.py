from typing import Union


class Coordinates:
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Corner:
    def __init__(self, value: Union[int, str], top_left: Coordinates, bottom_left: Coordinates, top_right: Coordinates, bottom_right: Coordinates):
        self.value = value
        self.top_left = top_left
        self.bottom_left = bottom_left
        self.top_right = top_right
        self.bottom_right = bottom_right

