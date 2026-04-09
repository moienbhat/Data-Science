#Protected(class and subclasses) and private(inside the class) attributes

class BankAccount:
    def __init__(self, name, balance, customer_id):
        self.name = name        #Public
        self._balance = balance  #Protected
        self.__customer_id = customer_id


    def get_balance(self):   #getter function to access protected attribute
        return self._balance
    
    def set_balance(self, new_amount):   #setter function to modify protected attribute
        self._balance = new_amount



    def get_customer_id(self):   #getter function to access private attribute
        return self.__customer_id
    
    def set_customer_id(self, new_id):  #setter function to modify private attribute
        self.__customer_id = new_id


acc1 = BankAccount("John", 12000, 23) 
print(acc1.name)
print(acc1.get_balance())

acc1.set_balance(10000)
print(acc1.get_balance())

acc1.set_customer_id(43)
print(acc1.get_customer_id())
        