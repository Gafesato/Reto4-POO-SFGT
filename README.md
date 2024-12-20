# Solucion Reto 4 POO -> Shape y Order Class
---
# Clase Shape
1. Introducción
2. Clases y Métodos Shape
    - Clase `Shape`
    - Clase `Rectangle`
    - Clase `Square`
    - Clase `Triangle`
    - Clase `Line`
    - Clase `Point`
3. Ejemplos
    - Ejemplo 1: Creación de un Cuadrado
    - Ejemplo 2: Creación de un Rectángulo
    - Ejemplo 3: Creación de un Triángulo Escaleno

---

## Introducción

Este código está diseñado para trabajar con diferentes figuras geométricas, como cuadrados, rectángulos y triángulos. Utiliza una jerarquía de clases, donde `Shape` es la clase base y las otras figuras la heredan para implementaciones específicas, como el cálculo de áreas y perímetros. Además se hace uso de todos los conceptos vistos durante el curso de POO, tales como:
1. *Herencia* para evitar la duplicación de código.
2. *Polimorfismo* ya que algunas clases tienen forma única de calcular su área.
3. *Encapsulamiento* en algunos métodos que solo se usan dentro de la clase.
4. *Abstracción* en la definición de las clases de `Line` y `Point`.
5. *Composición* ya que la clase `Line` está compuesta de Puntos, y `Shape` tiene líneas y puntos.

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
## Ejemplos
### Ejemplo 1
```python
p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)

square = Square(1, p1, p2, p3, p4)

print(f"Área del cuadrado: {square.compute_area()}")
print(f"Perímetro del cuadrado: {square.compute_perimeter()}")
print(f"Ángulos internos del cuadrado: {square.compute_inner_angles()}")
```
Resultado:
```bash
Área del cuadrado: 25
Perímetro del cuadrado: 20
Ángulos internos del cuadrado: [90.0, 90.0, 90.0, 90.0]
```
### Ejemplo 2
```python
p1 = Point(0, 0)
p2 = Point(10, 0)
p3 = Point(10, 5)
p4 = Point(0, 5)

rectangle = Rectangle(1, p1, p2, p3, p4)

print(f"Área del rectángulo: {rectangle.compute_area()}")
print(f"Perímetro del rectángulo: {rectangle.compute_perimeter()}")
print(f"Ángulos internos del rectángulo: {rectangle.compute_inner_angles()}")
```
Resultado:
```bash
Área del rectángulo: 50
Perímetro del rectángulo: 30
Ángulos internos del rectángulo: [90.0, 90.0, 90.0, 90.0]
```
### Ejemplo 3
```python
p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 4)

scalene = Scalene(1, p1, p2, p3)

print(f"Área del triángulo escaleno: {scalene.compute_area()}")
print(f"Perímetro del triángulo escaleno: {scalene.compute_perimeter()}")
print(f"Ángulos internos del triángulo escaleno: {scalene.compute_inner_angles()}")
```
Resultado:
```bash
Área del triángulo escaleno: 10.0
Perímetro del triángulo escaleno: 12.0
Ángulos internos del triángulo escaleno: [53.13, 36.87, 90.0]
```
---
---
# Clase Order *Revisted*
1. Introducción
2. Clases y Métodos Order
    - Clase `Order`
    - Clase `MenuItem`
    - Clase `Appetizer`
    - Clase `MainCourse`
    - Clase `Beverage`
    - Clase `Dessert`
    - Clase `Payment`
    - Clase `Card`
    - Clase `Efective`
3. Ejemplo
    - Creación de la orden
    - Añadir los setters
    - Hacer el pago con tarjeta
    - Hacer el pago en efectivo
---
## Introducción

- Continuando con el ejercicio de simulación de la orden de un restaurante, en este reto se incluyen formas de pago, se practica el **encapsulamiento** y además se aplican descuentos de una manera especial. Para poner en uso este concepto de POO, se agregan los métodos getters y setters para los atributos privados de las clases que heredan de `MenuItem`.
---
## Clases y Métodos
### Clase `Order`
Se modificó el método `calculate_total_price` para que si hay en la orden un plato principal, se aplique un descuento a la bebida y al postre en caso de estar también presentes en la orden.
```python
def calculate_total_price(self) -> float:
    """
    Calculates the total cost of the order.

    Returns the sum of the total price of all items.
    Also applies potential discounts based on the 
    order composition.
    """
    bill: float = 0
    beverage_discount: bool = False
    dessert_discount: bool = False
    for item in self.menu_items:
        if "MainCourse" == repr(item):
            beverage_discount, dessert_discount = True, True
            # Aplicar el descuento
        if "Beverage" == repr(item) and beverage_discount:
            item.change_price(0.2)
            beverage_discount = False
        if "Dessert" == repr(item) and dessert_discount:
            item.change_price(0.4)
            dessert_discount = False
            bill += item.get_total_price()
            
        return round(bill, 2)
```
### Clase `MenuItem`
En el anterior reto de la clase usé el método `__str__` para cada subclase, lo cual contradice el principio DRY. Por lo que solo lo dejé en la Clase `MenuItem`. En cada clase que hereda de esta, agregué el método `__repr__` para saber si el objeto en cuestión es Appetizer, MainCourse... Útil para crear los descuentos como vimos en la clase `Order`. Ahora solo voy a mostrar el código de cada clase.
```python
def __str__(self) -> str:
    """Returns the name of the MenuItem as a string."""
    return self.name
```
### Clase `Appetizer`
```python
class Appetizer(MenuItem):
    """Representation of an appetizer."""

    def __init__(
        self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__for_sharing = None

    def get_for_sharing(self) -> object:
        return self.__for_sharing

    def set_for_sharing(self, for_sharing: bool) -> None:
        if type(for_sharing) == bool:
            self.__for_sharing = for_sharing
            if for_sharing:
                self.change_price(0.95)
        else:
            print("La entrada solo puede ser o no ser para compartir.")

    def __repr__(self) -> str:
        """Creates the unique name of the Class."""
        return "Appetizer"
```
### Clase `MainCourse`
```python
class MainCourse(MenuItem):
    """Representation of a main course."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__is_meet = None

    def get_is_meet(self) -> object:
        return self.__is_meet

    def set_is_meet(self, is_meet: bool) -> None:
        if type(is_meet) == bool:
            self.__is_meet = is_meet
            if is_meet:
                self.change_price(1.05)
        else:
            print("El plato principal solo puede tener o no tener carne.")

    def __repr__(self) -> str:
        """Creates the unique name of the Class."""
        return "MainCourse"
```
### Clase `Beverage`
```python
class Beverage(MenuItem):
    """Representation of a beverage."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__size = None
        self.__has_sugar = None

    def get_size(self) -> object:
        return self.__size

    def set_size(self, size: int) -> None:
        if size > 0:
            self.__size = size
        else:
            print("El tamaño debe ser positivo.")

    def get_has_sugar(self) -> object:
        return self.__has_sugar

    def set_has_sugar(self, has_sugar: bool) -> None:
        if type(has_sugar) == bool:
            self.__has_sugar = has_sugar
            if has_sugar:
                self.change_price(1.05)
        else:
            print("La bebida solo puede tener o no tener azúcar.")

    def __repr__(self) -> str:
        """Creates the unique name of the Class."""
        return "Beverage"

```
### Clase `Dessert`
```python
class Dessert(MenuItem):
    """Representation of a dessert."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__on_season = None

    def get_on_season(self) -> object:
        return self.__on_season

    def set_on_season(self, on_season: bool) -> None:
        if type(on_season) == bool:
            self.__on_season = on_season
            if on_season:
                self.change_price(0.95)
        else:
            print("El postre solo puede ser o no ser de temporada.")

    def __repr__(self) -> str:
        """Creates the unique name of the Class."""
        return "Dessert"
```
### Clase `Payment`
```python
class Payment:
    def __init__(self):
        pass

    def pay(self, quantity):
        raise NotImplementedError("Subclases deben implementar pay()")
```
### Clase `Card`
```python
class Card(Payment):
    def __init__(self):
        super().__init__()
        self.__number = None
        self.__cvv = None

    def set_number(self, number):
        if len(number) == 16:
            self.__number = number
            return True
        else:
            print("El número de tarjeta debe tener 16 dígitos.")
            False

    def get_number(self):
        return self.__number

    def set_cvv(self, cvv):
        if len(cvv) == 3:
            self.__cvv = cvv
            return True
        else:
            False

    def get_cvv(self):
        return self.__cvv

    def pay(self, quantity):
        print(f"Pagando {quantity} con tarjeta {self.__number[-4:]}")
```
### Clase `Efective`
```python
class Efective(Payment):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def pay(self, bill):
        if self.amount >= bill:
            print(f"Pago realizado en efectivo ({bill}) con éxito.")
            print(f"Cambio: {round(self.amount - bill, 2)}")
        else:
            print(f"Fondos insuficientes. Faltan {bill - self.amount}")
```
---
## Ejemplo
### Creación de la orden
```python
order = Order()

# Orden Principal
mc1 = MainCourse(name="Steak", price=15.00, quantity=1)
mc2 = MainCourse(name="Vegetarian Pasta", price=12.00, quantity=2)
ap1 = Appetizer(name="Nachos", price=5.50, quantity=2)
ap2 = Appetizer(name="Garlic Bread", price=3.50, quantity=1)
ap3 = Appetizer(name="Spring Rolls", price=4.00, quantity=3)
bv1 = Beverage(name="Coca Cola", price=2.50, quantity=2)
bv2 = Beverage(name="Orange Juice", price=3.00, quantity=1)
bv3 = Beverage(name="Latte", price=4.00, quantity=1)
ds1 = Dessert(name="Cheesecake", price=6.00, quantity=1)
ds2 = Dessert(name="Chocolate Cake", price=5.50, quantity=1)

order_list = [mc1, mc2, ap1, ap2, ap3, bv1, bv2, bv3, ds1, ds2]
for i in range(len(order_list)):
    order.add_item(order_list[i])

# Mostrar los elementos en la orden
print("Items en la orden:")
print(order.show())
for item in order.show():
    print(f" -> {item}")
```
Resultado:
```bash
Items en la orden:
['Steak', 'Vegetarian Pasta', 'Nachos', 'Garlic Bread', 'Spring Rolls', 'Coca Cola', 'Orange Juice', 'Latte', 'Cheesecake', 'Chocolate Cake']
 -> Steak
 -> Vegetarian Pasta
 -> Nachos
 -> Garlic Bread
 -> Spring Rolls
 -> Coca Cola
 -> Orange Juice
 -> Latte
 -> Cheesecake
 -> Chocolate Cake
```
### Añadir los setters
```python
# Añadir los elementos especiales a la orden
mc1.set_is_meet(True)
mc2.set_is_meet(False)
bv1.set_size(2)
bv2.set_size(1)
bv3.set_size(1)
bv1.set_has_sugar(True)
bv2.set_has_sugar(True)
bv3.set_has_sugar(False)
ap1.set_for_sharing(True)
ap2.set_for_sharing(False)
ap3.set_for_sharing(False)
ds1.set_on_season(True)
ds1.set_on_season(False)
```
### Hacer el pago con tarjeta
Instanciamos...
```python
# Método de pago 1
card = Card()
card.set_number('1234567891234567')
card.set_cvv('707')

# Método de pago 2
billetito = Efective(100)
```
```python
card = Card()
card.set_number('1234567891234567')
card.set_cvv('707')
payment_method = 'card'
if payment_method == 'card':
    # Como se pagó con tarjeta, se aplica descuento del 2%
    total_order = order.calculate_total_price()
    print(f"Total de orden sin descuento: {total_order}")
    total = order.apply_discount(0.02)
    print("-> Aplica para descuento del 2%!!!")
    card.pay(total)
```
Resultado:
```bash
Total de orden sin descuento: 81.68
-> Aplica para descuentos!!!
Pagando 77.88 con tarjeta 4567
```
### Hacer el pago con efectivo
```python
payment_method = 'efective'
if payment_method == 'efective':
    # Como se pagó con efectivo, se aplica una multa del 3%
    # Por usar billetes xd (MedioAmbiente Friendly)
    total_order = order.calculate_total_price()
    print(f"Total de orden sin descuento: {total_order}")
    total = order.apply_discount(1.03)
    print("-> Aplica para multa!!! Felicitaciones.")
    billetito.pay(total)
```
Resultado: 
```bash
Total de orden sin descuento: 78.0
-> Aplica para multa!!! Felicitaciones.
Pago realizado en efectivo (80.34) con éxito.
Cambio: 19.66
```
