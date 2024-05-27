#Task 1:


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")

# Example usage
if __name__ == "__main__":
    product1 = Product("001", "Laptop", 999.99)
    product2 = Product("002", "Smartphone", 699.99)

    product1.display_product_info()
    print()
    product2.display_product_info()




#Task 2:


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")


class Book(Product):
    def __init__(self, product_id, name, price, author, genre):
        super().__init__(product_id, name, price)
        self.author = author
        self.genre = genre

    def display_product_info(self):
        super().display_product_info()
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")


class Electronic(Product):
    def __init__(self, product_id, name, price, brand, specs):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.specs = specs

    def display_product_info(self):
        super().display_product_info()
        print(f"Brand: {self.brand}")
        print(f"Specifications: {self.specs}")


class Clothing(Product):
    def __init__(self, product_id, name, price, size, color):
        super().__init__(product_id, name, price)
        self.size = size
        self.color = color

    def display_product_info(self):
        super().display_product_info()
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")


# Example usage
if __name__ == "__main__":
    book = Book("B001", "The Great Gatsby", 12.99, "F. Scott Fitzgerald", "Classic")
    electronic = Electronic("E001", "Laptop", 999.99, "Apple", "15-inch, Intel Core i7, 16GB RAM")
    clothing = Clothing("C001", "T-Shirt", 19.99, "Medium", "Blue")

    book.display_product_info()
    print()
    electronic.display_product_info()
    print()
    clothing.display_product_info()




#Task 3:


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_product_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")


class Book(Product):
    def __init__(self, product_id, name, price, author, genre):
        super().__init__(product_id, name, price)
        self.author = author
        self.genre = genre

    def display_product_info(self):
        super().display_product_info()
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")


class Electronic(Product):
    def __init__(self, product_id, name, price, brand, specs):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.specs = specs

    def display_product_info(self):
        super().display_product_info()
        print(f"Brand: {self.brand}")
        print(f"Specifications: {self.specs}")


class Clothing(Product):
    def __init__(self, product_id, name, price, size, color):
        super().__init__(product_id, name, price)
        self.size = size
        self.color = color

    def display_product_info(self):
        super().display_product_info()
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")


# Example usage
if __name__ == "__main__":
    book = Book("B001", "The Great Gatsby", 12.99, "F. Scott Fitzgerald", "Classic")
    electronic = Electronic("E001", "Laptop", 999.99, "Apple", "15-inch, Intel Core i7, 16GB RAM")
    clothing = Clothing("C001", "T-Shirt", 19.99, "Medium", "Blue")

    book.display_product_info()
    print()
    electronic.display_product_info()
    print()
    clothing.display_product_info()




#Task 4:


class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")


class Book(Product):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")


class Electronic(Product):
    def __init__(self, product_id, name, price, brand, specs):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.specs = specs

    def display_info(self):
        super().display_info()
        print(f"Brand: {self.brand}")
        print(f"Specifications: {self.specs}")


class Clothing(Product):
    def __init__(self, product_id, name, price, size, color):
        super().__init__(product_id, name, price)
        self.size = size
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Size: {self.size}")
        print(f"Color: {self.color}")


# Example usage
if __name__ == "__main__":
    book = Book("B001", "The Great Gatsby", 12.99, "F. Scott Fitzgerald")
    electronic = Electronic("E001", "Laptop", 999.99, "Apple", "15-inch, Intel Core i7, 16GB RAM")
    clothing = Clothing("C001", "T-Shirt", 19.99, "Medium", "Blue")

    print("Book Information:")
    book.display_info()
    print("\nElectronic Information:")
    electronic.display_info()
    print("\nClothing Information:")
    clothing.display_info()
