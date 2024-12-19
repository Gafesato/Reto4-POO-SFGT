# Menú de Navegación
1. Introducción
2. Clases y Métodos
    - Clase Shape
    - Clase Rectangle
    - Clase Square
    - Clase Triangle
    - Clase Line
    - Clase Point
3. Ejemplos
    - Ejemplo 1: Creación de un Cuadrado
    - Ejemplo 2: Creación de un Rectángulo
    - Ejemplo 3: Creación de un Triángulo Escaleno
4. Conclusiones

---

## Introducción

Este código está diseñado para trabajar con diferentes figuras geométricas, como cuadrados, rectángulos y triángulos. Utiliza una jerarquía de clases, donde `Shape` es la clase base y las otras figuras la heredan para implementaciones específicas, como el cálculo de áreas y perímetros.

---

## Clases y Métodos

### Clase Shape

La clase base que define las propiedades comunes a todas las figuras geométricas. Esta clase maneja la inicialización de los vértices y las aristas de la figura, y tiene métodos para calcular el perímetro y los ángulos internos.

```python
class Shape:
    def __init__(self, method: int, *args) -> None:
        # Inicialización con vértices o aristas
        ...
    def compute_area(self):
        raise NotImplementedError("Subclases deben implementar compute_area()")
    def compute_perimeter(self) -> float:
        return sum(edge.length for edge in self.edges)
    def compute_inner_angles(self) -> list[float]:
        ...
```
### Clase Rectangle

Hereda de `Shape` y se especializa en los rectángulos. Se asegura de que la figura tenga 4 vértices y de que los ángulos internos sean rectos.

```python
class Rectangle(Shape):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        ...
    def compute_area(self) -> float:
        return self._width * self._height

```

### Clase Square

Hereda de `Rectangle` y asegura que todos los lados de este sean iguales, lo que convierte la figura en un cuadrado.

```python
class Square(Rectangle):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        ...
    def compute_area(self) -> float:
        return self._width**2
```

### Clase Triangle

Define el comportamiento de un triángulo y calcula el área utilizando las coordenadas de los vértices. Además, verifica el tipo de triángulo según los lados.

```python
class Triangle(Shape):
    def __init__(self, method: int, *args) -> None:
        super().__init__(method, *args)
        ...
    def compute_area(self) -> float:
        x1, x2, x3 = [vertex.x for vertex in self.vertices]
        ...
```

### Clase Line

Representa una línea en el plano y calcula la longitud entre dos puntos.

```python
class Line:
    def __init__(self, start_point: "Point", end_point: "Point") -> None:
        self.length = self.start_point.compute_distance(self.end_point)

```

### Clase Point

Representa un punto en el plano y proporciona un método para calcular la distancia entre dos puntos.

```python
class Point:
    def __init__(self, x: int=0, y: int=0) -> None:
        self.x = x
        self.y = y
    def compute_distance(self, point: "Point") -> float:
        return ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
```
---
