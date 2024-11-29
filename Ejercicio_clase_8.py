import math
import numpy as np

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()

    def compute_length(self):
        x1, y1 = self.start
        x2, y2 = self.end
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def compute_slope(self):
        x1, y1 = self.start
        x2, y2 = self.end
        if x2 - x1 == 0:
            return 90.0 if y2 > y1 else -90.0
        slope_rad = math.atan((y2 - y1) / (x2 - x1))
        return math.degrees(slope_rad)

    def compute_horizontal_cross(self):
        x1, y1 = self.start
        x2, y2 = self.end
        if y1 == y2:
            return None
        x_cross = x1 - (y1 * (x2 - x1)) / (y2 - y1)
        return (x_cross, 0)

    def compute_vertical_cross(self):
        x1, y1 = self.start
        x2, y2 = self.end
        if x1 == x2:  # Línea paralela al eje Y
            return None
        y_cross = y1 - (x1 * (y2 - y1)) / (x2 - x1)
        return (0, y_cross)

    def display_info(self):
        print(f"Línea de {self.start} a {self.end}:")
        print(f"  Longitud: {self.length:.2f}")
        print(f"  Pendiente desde la horizontal: {self.slope:.2f}°")
        h_cross = self.compute_horizontal_cross()
        v_cross = self.compute_vertical_cross()
        print(f"  Intersección con el eje X: {h_cross if h_cross else 'No existe'}")
        print(f"  Intersección con el eje Y: {v_cross if v_cross else 'No existe'}")


class Rectangle:
    def __init__(self, line1, line2, line3, line4):
        self.lines = [line1, line2, line3, line4]
        if not self.is_rectangle():
            raise ValueError("Las líneas no forman un rectángulo.")

    def is_rectangle(self):
        if self.lines[0].start != self.lines[3].end or \
           self.lines[0].end != self.lines[1].start or \
           self.lines[1].end != self.lines[2].start or \
           self.lines[2].end != self.lines[3].start:
            return False
        return True

    def area(self):
        side_lengths = [line.length for line in self.lines]
        return side_lengths[0] * side_lengths[1]

    def display_info(self):
        print("Información del rectángulo:")
        for i, line in enumerate(self.lines, start=1):
            print(f"\nLínea {i}:")
            line.display_info()
        print(f"\nÁrea del rectángulo: {self.area():.2f}")


line1 = Line((0, 0), (4, 0))
line2 = Line((4, 0), (4, 3))
line3 = Line((4, 3), (0, 3))
line4 = Line((0, 3), (0, 0))

rectangle = Rectangle(line1, line2, line3, line4)
rectangle.display_info()
