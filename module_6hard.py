import math

class Figure:
    def __init__(self, color=(0, 0, 0), *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = True

        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    @property
    def sides_count(self):
        return 0

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return isinstance(r, int) and isinstance(g, int) and isinstance(b, int) and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides) and len(new_sides) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    def __init__(self, color=(0, 0, 0), *sides):
        self.__radius = 0
        super().__init__(color, *sides)

        if len(sides) == 1:
            self.__radius = sides[0] / (2 * math.pi)
            self.set_sides(2 * math.pi * self.__radius)
        elif len(sides) == 0:
            self.__sides = [1]

    @property
    def sides_count(self):
        return 1

    def get_square(self):
        return math.pi * (self.__radius ** 2)

class Triangle(Figure):
    def __init__(self, color=(0, 0, 0), *sides):
        super().__init__(color, *sides)

    @property
    def sides_count(self):
        return 3

    def get_square(self):
        if len(self.__sides) == 3:
            s = sum(self.__sides) / 2
            return (s * (s - self.__sides[0]) * (s - self.__sides[1]) * (s - self.__sides[2])) ** 0.5
        return 0

class Cube(Figure):
    def __init__(self, color=(0, 0, 0), side_length=1):
        super().__init__(color, side_length)

        self.__sides = [side_length] * self.sides_count

    @property
    def sides_count(self):
        return 12

    def get_volume(self):
        return self.__sides[0] ** 3

    def get_sides(self):
        return self.__sides

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
