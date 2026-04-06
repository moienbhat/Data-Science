class Product:
    count = 0
    def __init__(self , name, price):
        self.name = name 
        self.price = price

    def get_info(self):
        return(f"Name : {self.name} , Price : {self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"Total Products : {cls.count}")

    @staticmethod
    def calc_discount(price, discount):
        return price - (price*discount/100)
    
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 30000)

print(p1.calc_discount(p1.price, 10))

Product.get_count()