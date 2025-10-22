class Product:
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def update_price(self, new_price):
        self.price = new_price

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    def info(self):
        return f"{self.name} - ${self.price} ({self.quantity} в наличии)"


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity

    def remove_product(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            return f"Товар удален!"
        return "Товар не найден!"

    def update_quantity(self, product_id, new_quantity):
        if product_id in self.items:
            if new_quantity > 0:
                self.items[product_id] = new_quantity
                return "Количество обновлено!"
            else:
                return self.remove_product(product_id)
        return "Товар не найден!"

    def total_price(self, products):
        total = 0
        for product_id, quantity in self.items.items():
            product = products[product_id]
            total += product.price * quantity
        return total

    def cart_info(self, products):
        item_count = sum(self.items.values())
        return f"Товаров: {item_count}, Сумма: ${self.total_price(products)}"


class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.order_history = []
        self.cart = ShoppingCart()

    def place_order(self, products):
        if not self.cart.items:
            return "Корзина пуста! Добавь товары сначала!"

        total = self.cart.total_price(products)
        order = Order(self.customer_id, self.cart.items, total)
        self.order_history.append(order)
        self.cart = ShoppingCart()
        return f"Заказ #{order.order_id} оформлен! Жди доставки!"

    def customer_info(self):
        orders_count = len(self.order_history)
        return f"Клиент: {self.name}, Заказов: {orders_count}"


class Order:
    def __init__(self, customer_id, items, total_price):
        self.order_id = f"ORD{abs(hash(str(items))) % 10000:04d}"
        self.customer_id = customer_id
        self.items = items
        self.total_price = total_price
        self.final_price = self.calculate_price()

    def calculate_price(self):
        tax = self.total_price * 0.1
        discount = self.total_price * 0.05 if self.total_price > 100 else 0
        return self.total_price + tax - discount

    def order_info(self):
        discount = 5 if self.total_price > 100 else 0
        return f"Заказ #{self.order_id}: ${self.final_price:.2f} (скидка: {discount}%)"
