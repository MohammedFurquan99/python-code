class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show(self):
        print("Brand:", self.brand)
        print("Color:", self.color)


car1 = Car("BMW", "Black")
car2 = Car("Audi", "White")

car1.show()
car2.show()