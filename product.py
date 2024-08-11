class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def create_product(self):
        # Code to create a new product
        pass

    def update_product(self, name, price):
        # Code to update product details
        self.name = name
        self.price = price

    def suspend_product(self):
        # Code to suspend a product
        pass
