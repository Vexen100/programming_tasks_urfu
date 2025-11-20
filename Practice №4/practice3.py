class Product:
    """
    Класс для представления товара в онлайн-магазине.
    
    Атрибуты:
        product_id (str): Уникальный идентификатор товара
        name (str): Название товара
        price (float): Цена товара
        quantity (int): Количество товара на складе
        category (str): Категория товара
    """

    def __init__(self, product_id, name, price, quantity, category):
        """
        Инициализирует объект товара.
        
        Параметры:
            product_id: Уникальный идентификатор
            name: Название товара
            price: Стоимость единицы товара
            quantity: Доступное количество на складе
            category: Категория товара (например, "электроника")
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

    def update_price(self, new_price):
        """
        Обновляет цену товара.
        
        Параметры:
            new_price: Новая цена товара
        """
        self.price = new_price

    def update_quantity(self, new_quantity):
        """
        Обновляет количество товара на складе.
        
        Параметры:
            new_quantity: Новое количество товара
        """
        self.quantity = new_quantity

    def info(self):
        """
        Формирует краткую информацию о товаре.
        
        Возвращает:
            str: Строка с названием, ценой и количеством товара
        """
        return f"{self.name} - ${self.price} ({self.quantity} в наличии)"


class ShoppingCart:
    """
    Класс для управления корзиной покупок.
    
    Атрибуты:
        items (dict): Словарь с product_id и количеством товаров
    """

    def __init__(self):
        """
        Инициализирует пустую корзину.
        """
        self.items = {}

    def add_product(self, product, quantity=1):
        """
        Добавляет товар в корзину или увеличивает его количество.
        
        Параметры:
            product: Объект товара (Product)
            quantity: Количество товара для добавления (по умолчанию 1)
        """
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity

    def remove_product(self, product_id):
        """
        Удаляет товар из корзины по идентификатору.
        
        Параметры:
            product_id: Идентификатор удаляемого товара
        
        Возвращает:
            str: Сообщение об успешном удалении или отсутствии товара
        """
        if product_id in self.items:
            del self.items[product_id]
            return "Товар удален!"
        return "Товар не найден!"

    def update_quantity(self, product_id, new_quantity):
        """
        Изменяет количество товара в корзине.
        
        Параметры:
            product_id: Идентификатор товара
            new_quantity: Новое количество товара
        
        Возвращает:
            str: Сообщение об успешном обновлении или ошибке
        """
        if product_id in self.items:
            if new_quantity > 0:
                self.items[product_id] = new_quantity
                return "Количество обновлено!"
            else:
                return self.remove_product(product_id)
        return "Товар не найден!"

    def total_price(self, products):
        """
        Рассчитывает общую стоимость товаров в корзине.
        
        Параметры:
            products: Словарь с объектами товаров
        
        Возвращает:
            float: Общая сумма заказа
        """
        total = 0
        for product_id, quantity in self.items.items():
            product = products[product_id]
            total += product.price * quantity
        return total

    def cart_info(self, products):
        """
        Формирует информацию о корзине.
        
        Параметры:
            products: Словарь с объектами товаров
        
        Возвращает:
            str: Строка с количеством и суммой товаров в корзине
        """
        item_count = sum(self.items.values())
        return f"Товаров: {item_count}, Сумма: ${self.total_price(products)}"


class Customer:
    """
    Класс для представления клиента онлайн-магазина.
    
    Атрибуты:
        customer_id (str): Уникальный идентификатор клиента
        name (str): Имя клиента
        email (str): Email клиента
        order_history (list): История заказов
        cart (ShoppingCart): Текущая корзина покупок
    """

    def __init__(self, customer_id, name, email):
        """
        Инициализирует объект клиента.
        
        Параметры:
            customer_id: Уникальный идентификатор
            name: Имя клиента
            email: Адрес электронной почты
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.order_history = []
        self.cart = ShoppingCart()

    def place_order(self, products):
        """
        Оформляет заказ из текущей корзины.
        
        Параметры:
            products: Словарь с объектами товаров
        
        Возвращает:
            str: Сообщение об успешном оформлении или ошибке
        """
        if not self.cart.items:
            return "Корзина пуста! Добавь товары сначала!"

        total = self.cart.total_price(products)
        order = Order(self.customer_id, self.cart.items, total)
        self.order_history.append(order)
        self.cart = ShoppingCart()
        return f"Заказ #{order.order_id} оформлен! Жди доставки!"

    def customer_info(self):
        """
        Формирует информацию о клиенте.
        
        Возвращает:
            str: Строка с именем клиента и количеством заказов
        """
        orders_count = len(self.order_history)
        return f"Клиент: {self.name}, Заказов: {orders_count}"


class Order:
    """
    Класс для представления заказа.
    
    Атрибуты:
        order_id (str): Уникальный номер заказа
        customer_id (str): Идентификатор клиента
        items (dict): Список товаров в заказе
        total_price (float): Общая стоимость без скидок
        final_price (float): Итоговая стоимость с учетом налогов и скидок
    """

    def __init__(self, customer_id, items, total_price):
        """
        Инициализирует объект заказа.
        
        Параметры:
            customer_id: Идентификатор клиента
            items: Словарь с product_id и количеством товаров
            total_price: Общая стоимость заказа
        """
        self.order_id = f"ORD{abs(hash(str(items))) % 10000:04d}"
        self.customer_id = customer_id
        self.items = items
        self.total_price = total_price
        self.final_price = self.calculate_price()

    def calculate_price(self):
        """
        Рассчитывает итоговую стоимость заказа.
        
        Возвращает:
            float: Итоговая сумма с налогами и скидками
        """
        tax = self.total_price * 0.1
        discount = self.total_price * 0.05 if self.total_price > 100 else 0
        return self.total_price + tax - discount

    def order_info(self):
        """
        Формирует информацию о заказе.
        
        Возвращает:
            str: Строка с номером заказа, итоговой суммой и скидкой
        """
        discount = 5 if self.total_price > 100 else 0
        return f"Заказ #{self.order_id}: ${self.final_price:.2f} (скидка: {discount}%)"
