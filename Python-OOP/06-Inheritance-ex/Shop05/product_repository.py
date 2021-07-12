from Shop05.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        for el in self.products:
            if el.name == product_name:
                return el

    def remove(self, product_name):
        for el in self.products:
            if el.name == product_name:
                self.products.remove(el)

    def __repr__(self):
        sep = "\n"
        formatted_output = f"{sep.join(f'{el.name}: {el.quantity}' for el in self.products)}"
        return formatted_output
