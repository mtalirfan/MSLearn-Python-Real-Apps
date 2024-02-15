class Square:
    def __init__(self, w: int = 2, h: int = 2):
        self.__height = h
        self.__width = w

    @property
    def side(self):
        if self.__height == self.__width:
            return self.__height
        else:
            return f"height: {self.__height} width: {self.__width}"

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @side.setter
    def side(self, new_side):
        if new_side >= 0:
            self.__height = new_side
            self.__width = new_side
        else:
            raise Exception("value needs to be 0 or larger")

    @width.setter
    def width(self, new_width):
        if new_width >= 0:
            self.__width = new_width
        else:
            raise Exception("value needs to be 0 or larger")

    @height.setter
    def height(self, new_height):
        if new_height >= 0:
            self.__height = new_height
        else:
            raise Exception("value needs to be 0 or larger")


square = Square(5)

print(f"{square.width}x{square.height}")

# square.height = 3  # not a square anymore
print(f"{square.width}x{square.height}")

square.side = 5
print(f"{square.width}x{square.height}")

# square.set_side(-7)
# print(f"{square.width}x{square.height}")

print(square.width)

square.width = 2
# print(square.width)
print(square.side)

square.side = 0

print(square.side)
