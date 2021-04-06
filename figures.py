class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_figure(self):
        return f'Rectangle({self.x}, {self.y}, {self.width}, {self.height}).'


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def get_figure(self):
        return f'Circle({self.x}, {self.y}, {self.r}).'
