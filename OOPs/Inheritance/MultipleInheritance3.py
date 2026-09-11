class Customer:
    def __init__(self):
        self.customer_name = ""
        self.mobile = 0
        self.address = ""
        self.email = ""
    def customer_data(self):
        self.customer_name = input("Enter Customer Name: ")
        self.mobile = int(input("Enter Mobile Number: "))
        self.address = input("Enter Customer Address: ")
        self.email = input("Enter Customer Email: ")
    def customer_info(self):
        print("---------------Customer Info---------------")
        print("Customer Name: ",self.customer_name)
        print("Mobile Number: ", self.mobile)
        print("Address: ", self.address)
        print("Email: ", self.email)

class Product:
    def __init__(self):
        self.product_name = ""
        self.price = 0
        self.description = ""
    def product_data(self):
        self.product_name = input("Enter Product Name: ")
        self.price = int(input("Enter Product Price: "))
        self.description = input("Enter Product Description: ")
    def product_info(self):
        print("---------------Product Info---------------")
        print("Product Name: ",self.product_name)
        print("Price: ", self.price)
        print("Description: ", self.description)

class Order(Customer,Product):
    def __init__(self):
        self.order_id = 0
        self.quantity = 0
        self.total_price = 0
        self.order_date = 0
    def order_data(self):
        self.order_id = int(input("Enter Order Id: "))
        self.quantity = int(input("Enter Quantity: "))
        self.total_price = int(input("Enter Total Price: "))
        self.order_date = int(input("Enter Order Date: "))
    def order_info(self):
        print("---------------Order Info---------------")
        print("Order Id: ",self.order_id)
        print("Quantity: ",self.quantity)
        print("Total Price: ",self.total_price)
        print("Order Date: ",self.order_date)

obj1 =  Order()
obj1.order_data()
obj1.product_data()
obj1.customer_data()

obj1.product_info()
obj1.order_info()
obj1.customer_info()