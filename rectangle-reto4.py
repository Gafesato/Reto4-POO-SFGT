# Hecho por Samuel Fernando Garzón Toro
import math

class Shape:
    def __init__(self, method: int, *args) -> None:
        """Inicializar Shape con vértices o aristas."""
        self.vertices: list["Point"] = []
        self.edges: list["Line"] = []
        self.__method: int = method

        # Inicialización con vértices
        if method == 1:
            for i in range(len(args)):
                vertice: "Point" = args[i]
                self.vertices.append(vertice)
                edge: "Line" = Line(vertice, args[(i + 1) % len(args)])
                self.edges.append(edge)

        # Inicialización con aristas
        elif method == 2:
            for edge in args:
                self.edges.append(edge)
                if edge.start_point not in self.vertices:
                    self.vertices.append(edge.start_point)
                if edge.end_point not in self.vertices:
                    self.vertices.append(edge.end_point)

        else:
            raise ValueError("No se seleccionó ningún método.")

    def get_method(self):
        return self.__method

    def set_method(self, new_method):
        self.__method == new_method

    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")

    def compute_perimeter(self) -> float:
        """Retorna la suma de las longitudes de cada arista de la figura."""
        return sum(edge.length for edge in self.edges)
    
    def compute_inner_angles(self) -> list[float]:
        """Calcula los ángulos en cada vértice."""
        angles = []
        n = len(self.vertices)
        for i in range(n):
            p1 = self.vertices[i - 1]
            p2 = self.vertices[i]
            p3 = self.vertices[(i + 1) % n]

            # Creo la clase Vector para facilitar el cálculo
            # de los ángulos
            v1 = Vector(p2, p1)
            v2 = Vector(p2, p3)

            cos_theta = v1.scalar_product(v2) / (v1.norm() * v2.norm())
            angle = math.degrees(math.acos(cos_theta))
            angles.append(angle)
        return angles

    def __str__(self) -> str:
        """Mostrar una representación agradable de la figura en cuestión."""
        output = "Vértices: "
        for vertice in self.vertices:
            output += f'[({vertice.x},{vertice.y})] '
        output += "\nAristas: "
        for edge in self.edges:
            output += f'[({edge.start_point.x}),({edge.start_point.y})] -> [({edge.end_point.x}),({edge.end_point.y})]]  '
        return output


class Rectangle(Shape):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if len(self.vertices) != 4:
            raise ValueError("Un rectángulo debe tener 4 vértices.")
        if not self._check_is_rectangle():
            raise ValueError("Los vértices dados no forman un rectángulo.")

        x_coords = [vertex.x for vertex in self.vertices]
        y_coords = [vertex.y for vertex in self.vertices]

        self._width = max(x_coords) - min(x_coords)
        self._height = max(y_coords) - min(y_coords)

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def _check_is_rectangle(self) -> bool:
        """Verifica si los vértices forman un rectángulo verificando ángulos internos."""
        angles = self.compute_inner_angles()
        return all(int(angle) == 90 for angle in angles)

    def compute_area(self) -> float:
        return self._width * self._height


class Square(Rectangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if self._width != self._height:
            raise ValueError("Los vértices dados no forman un cuadrado.")

    def compute_area(self) -> float:
        return self._width**2


class Triangle(Shape):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if len(self.vertices) != 3:
            raise ValueError("Un triángulo debe tener solo 3 vértices.")

    def compute_area(self) -> float:
        """Calcula el área con las coordenadas de cada punto del triángulo."""
        x1, x2, x3 = [vertex.x for vertex in self.vertices]
        y1, y2, y3 = [vertex.y for vertex in self.vertices]
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    def _check_triangle_type(self, unique_sides: int) -> bool:
        sides: list[float] = [edge.length for edge in self.edges]
        # Uso set() ya que solo permite valores únicos
        # En caso de que len(set(...)) == unique_sides,
        # es porque hay unique_sides iguales
        # tomo 7 valores de redondeo para verificar bien
        return len(set(round(side, 7) for side in sides)) == unique_sides


class Isosceles(Triangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if not self._check_triangle_type(2):
            raise ValueError("Los vértices dados no forman un triángulo isósceles.")


class Equilateral(Triangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if not self._check_triangle_type(1):
            raise ValueError("Los vértices dados no forman un triángulo equilátero.")


class Scalene(Triangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if not self._check_triangle_type(3):
            raise ValueError("Los vértices dados no forman un triángulo escaleno.")


class TriRectangle(Triangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        if not self._is_right_triangle() and not self._check_triangle_type(3):
            raise ValueError("Los vértices dados no forman un triángulo rectángulo.")

    def _is_right_triangle(self) -> bool:
        """Verifica que el triángulo sea rectángulo usando El Teorema de Pitágoras."""
        c1, c2, hyp = sorted(edge.length**2 for edge in self.edges)
        return round(c1+c2, 7) == round(hyp, 7)


class Line:
    """Abstracción de lo que es una línea en el plano."""
    def __init__(self, start_point: "Point", end_point: "Point") -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.start_point.compute_distance(self.end_point)


class Point:
    """Abstracción de lo que es un punto en el plano."""
    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y

    def compute_distance(self, point: "Point") -> float:
        """Calcula la distancia entre dos puntos."""
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5


class Vector(Line):
    def __init__(self, start_point: "Point", end_point: "Point") -> None:
        super().__init__(start_point, end_point)
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y
        self.vector = Point(self.x, self.y)

    def scalar_product(self, vector2: "Vector") -> float:
        """Devuelve el producto escalar con otro Vector."""
        return (self.x*vector2.x) + (self.y*vector2.y)

    def norm(self) -> float:
        """Retorna la norma del vector."""
        return math.sqrt((self.x)**2 + (self.y)**2)


if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(10, 0)
    p3 = Point(10, 5)
    p4 = Point(0, 5)

    rectangle = Rectangle(1, p1, p2, p3, p4)

    print(f"Área del rectángulo: {rectangle.compute_area()}")
    print(f"Perímetro del rectángulo: {rectangle.compute_perimeter()}")
    print(f"Ángulos internos del rectángulo: {rectangle.compute_inner_angles()}")