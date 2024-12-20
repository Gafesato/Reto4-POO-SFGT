class Order:
    """Representation of a restaurant order."""

    def __init__(self) -> None:
        self.menu_items: list[MenuItem] = []

    def add_item(self, item: "MenuItem") -> None:
        """Add items to the list."""
        self.menu_items.append(item)

    def show(self) -> list[str]:
        """
        Returns a readable list of items.

        Converts each item in the order to a string.
        """
        return [str(item) for item in self.menu_items]

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

    def apply_discount(self, discount: float) -> float:
        """
        Applies a discount to the total order cost.

        Args:
            discount: The discount percentage as a decimal (e.g., 0.1 for 10%).

        Returns:
            The total cost after applying the discount.
        """
        total = self.calculate_total_price()
        if discount <= 1:
            new_total = total * (1-discount)
        elif discount > 1:
            new_total = total * discount
        return round(new_total, 2)


class MenuItem:
    """Representation of a menu item."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        if self.price < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.quantity = quantity
        if self.quantity <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")

    def get_total_price(self) -> float:
        """Calculates and returns the total price of this item."""
        return self.price * self.quantity

    def change_price(self, fee: float) -> None:
        """
        Adjusts the price of an item.

        Args:
            fee: A multiplier factor to adjust the price.
        """
        self.price *= fee

    def __str__(self) -> str:
        """Returns the name of the MenuItem as a string."""
        return self.name


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


class Payment:
    def __init__(self):
        pass

    def pay(self, quantity):
        raise NotImplementedError("Subclases deben implementar pay()")


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


if __name__ == '__main__':
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

    # Método de pago 1
    card = Card()
    card.set_number('1234567891234567')
    card.set_cvv('707')

    # Método de pago 2
    billetito = Efective(100)

    # Pago con efectivo
    payment_method = 'efective'
    if payment_method == 'efective':
        # Como se pagó con efectivo, se aplica una multa del 3%
        # Por usar billetes xd (MedioAmbiente Friendly)
        total_order = order.calculate_total_price()
        print(f"Total de orden sin descuento: {total_order}")
        total = order.apply_discount(1.03)
        print("-> Aplica para multa!!! Felicitaciones.")
        billetito.pay(total)

    # Pago con tarjeta
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