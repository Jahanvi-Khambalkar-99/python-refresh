class Product:
    
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    
    def describe(self):
        return f"{self.name} : ${self.price}"
    
p1 = Product("Mug", 12, 5)
print(p1.describe())

# self refer to the current object, the specific instance the method is working on
# attribute is a properties of object 
# method describes what object can do 