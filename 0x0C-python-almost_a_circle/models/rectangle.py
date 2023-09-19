#!/usr/bin/python3
"""Define subclass Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Represent subclass Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize subclass Rectangle."""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width of rectangle."""
        return self.__width

    @property
    def height(self):
        """Get width of rectangle."""
        return self.__height

    @property
    def x(self):
        """Get width of rectangle."""
        return self.__x

    @property
    def y(self):
        """Get width of rectangle."""
        return self.__y

    @width.setter
    def width(self, value):
        """Set width of rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if (value < 0):
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Set height of rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if (value < 0):
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Set x of rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if (value < 0):
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Set y of rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if (value < 0):
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Calculate area of rectangle."""
        return (self.__height * self.__width)

    def display(self):
        """Print in stdout the Rectangle instance with character #."""
        [print("") for i in range(self.y)]
        for j in range(self.height):
            [print(" ", end="") for k in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Print string representation of Rectangle object data."""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Assign an argument to each attribute."""
        if args and len(args) != 0:
            i = 0
            for a in args:
                if i == 0:
                    if a is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = a
                elif i == 1:
                    self.width = a
                elif i == 2:
                    self.height = a
                elif i == 3:
                    self.x = a
                elif i == 4:
                    self.y = a
                i += 1
        elif kwargs and len(kwargs) != 0:
            for p, q in kwargs.items():
                if p == "id":
                    if q is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = q
                elif p == "width":
                    self.width = q
                elif p == "height":
                    self.height = q
                elif p == "x":
                    self.x = q
                elif p == "y":
                    self.y = q

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the string representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
