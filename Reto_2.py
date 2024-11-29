class MenuItem:
    def __init__(self, name, price, descuento=0):
        self.name = name
        self.price = price
        self.descuento = descuento

    def ComputePrice(self):
        return self.price - (self.price * self.descuento / 100)


class Beverage(MenuItem):
    def __init__(self, name, price, size, descuento=0):
        super().__init__(name, price, descuento)
        self.size = size


class Appetizer(MenuItem):
    def __init__(self, name, price, vegetarian=False, descuento=0):
        super().__init__(name, price, descuento)
        self.vegetarian = vegetarian


class MainCourse(MenuItem):
    def __init__(self, name, price, country_food, descuento=0):
        super().__init__(name, price, descuento)
        self.country_food = country_food


class Order():
    def __init__(self):
        self.items = []

    def append_item(self, item):
        self.items.append(item)

    def calcular_total(self):
        return sum(item.ComputePrice() for item in self.items)

    def aplicar_descuento(self, porcentaje):
        total = self.calcular_total()
        return total - (total * porcentaje / 100)


# Crear menú con al menos 10 elementos, con descuentos diferentes
menu = [
    Beverage("Coca Cola", 2.5, "Mediano", descuento=5),
    Beverage("Jugo Natural", 3.0, "Grande", descuento=10),
    Beverage("Agua", 1.5, "Pequeño", descuento=0),
    Appetizer("Espaguetis de calabacín", 4.5, True, descuento=15),
    Appetizer("Nachos con Queso", 5.0, False, descuento=5),
    MainCourse("Pizza Napolitana", 8.5, "Italiana", descuento=10),
    MainCourse("Tacos de Birria", 7.0, "Mexicana", descuento=5),
    MainCourse("Big Mac", 9.0, "Americana", descuento=0),
    MainCourse("Lechona", 10.0, "Colombiana", descuento=20),
    MainCourse("Sushi", 12.0, "Japonesa", descuento=0),
]

pedido = Order()
pedido.append_item(menu[9])

print(f"Total del pedido: ${pedido.calcular_total():.2f}")
