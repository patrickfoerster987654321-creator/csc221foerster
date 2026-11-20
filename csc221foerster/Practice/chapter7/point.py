class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def print_point(self):
        print(f'({self.x}, {self.y})')

    def distance(self, other):
        """
            >>> p1 = Point(1, 2)
            >>> p2 = Point(4, 6)
            >>> p1.distance(p2)
            5.0
            >>> p3 = Point(16, 11)
            >>> p2.distance(p3)
            13.0
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5
