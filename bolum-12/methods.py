# Class
class Product:
    # method
    # attribute, property
    def __init__(self, name, price, isActive):
        self.name = name
        self.price = price
        self.isActive = isActive

    # method
    def intro(self):
        return f"urun adi: {self.name} urun fiyat: {self.kdv_price()}"
    
    def kdv_price(self):
        return self.price * 1.20

# Instance, Nesne
p1 = Product("Iphone 15", 50000, True)
p2 = Product("Iphone15 Pro", 60000, True)
p3 = Product("Samsung S24", 70000, True)

urunler = [p1,p2,p3]

for i in urunler:
    if i.isActive:
        print(i.intro())
        