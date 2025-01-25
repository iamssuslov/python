import logging
from typing import List

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Product:
    def __init__(self, name: str, qty: int, price: float):
        if not isinstance(name, str):
            raise TypeError('Для названия продукта нужен тип str')

        if not isinstance(qty, int):
            raise TypeError('Для кол-ва продукта нужен тип int')

        if not isinstance(price, float):
            raise TypeError('Для цены продукта нужен тип float')

        self.name = name
        self.qty = qty
        self.price = price

    def plus_qty(self, qty: int):
        if qty < 0:
            raise ValueError(f'Вы не можете прибавить отрицательное кол-во товара {self.name}')

        if not isinstance(qty, int):
            raise TypeError('Нужен тип int для кол-ва')

        self.qty += qty
        log.info(f'Количество продукта {self.name} увеличено на {qty} текущее кол-во: {self.qty}')

    def minus_qty(self, qty: int):
        if qty < 0:
            raise ValueError('Вы не можете вычесть отрицательное кол-во продукта')

        if not isinstance(qty, int):
            raise TypeError('Для кол-ва продукта нужен тип int')

        if self.qty - qty < 0:
            raise ValueError('Вы не можете уменьшить кол-во продукта, т.к. его кол-во меньше, чем вы хотите уменьшить')

        self.qty -= qty
        log.info(f'Количество продукта {self.name} уменьшено на {qty}, текущее кол-во: {self.qty}')

    def get_cost(self):
        log.info(f'Общая стоимость продукта {self.name} равна {self.qty * self.price}')


class Warehouse:
    def __init__(self, lst: List[Product]):
        if not isinstance(lst, List):
            raise TypeError('Склад может хранить только список типа Product')

        self.product_list = lst

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError('На склад можно добавить только тип Product')

        self.product_list.append(product)
        log.info(f'Продукт {product.name} добавлен на склад')

    def delete_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError('Со склада можно удалить только тип Product')

        if len(self.product_list) == 0:
            raise ValueError('Вы не можете удалить продукт со склада, т.к. он пустой')

        self.product_list[self.product_list.index(product)].qty = 0
        self.product_list.remove(product)
        log.info(f'Продукт {product.name} удалён со склада')

    def get_all_cost(self):
        log.info(
            f'Общая стоимость всех продуктов равна {sum(product.qty * product.price for product in self.product_list)}')


class Seller:
    def __init__(self, name: str, warehouse: Warehouse):
        if not isinstance(name, str):
            raise TypeError('Для названия продукта нужен тип str')

        if not isinstance(warehouse, Warehouse):
            raise TypeError('Для кол-ва продукта нужен тип int')

        self.name = name
        self.warehouse = warehouse
        self.revenue = 0
        self.__sales_list = []

    def sell_product(self, product: Product, qty: int):
        if not isinstance(product, Product):
            raise TypeError('Со склада можно продать только тип Product')

        if not isinstance(qty, int):
            raise TypeError('Со склада можно продать только целочисленное кол-во продуктов')

        try:
            self.warehouse.product_list[self.warehouse.product_list.index(product)].minus_qty(qty)
            self.__sales_list.append((product, qty))
            self.__calc_revenue()
        except ValueError as e:
            log.error(e)

    def __calc_revenue(self):
        log.info(f'Всего было выручено {sum(product[0].price * product[1] for product in self.__sales_list)} у.е.')

    def get_report(self):
        log.info('Отчёт по продажам:')
        for product in self.__sales_list:
            log.info(
                f'Продукт {product[0].name} был продан в количестве {product[1]} на сумму {product[0].price * product[1]}')


if __name__ == '__main__':
    bread = Product('Хлеб', 5, 15.5)
    milk = Product('Молоко', 8, 40.5)
    dumplings = Product('Пельмени', 3, 371.9)
    lst = [bread, milk, dumplings]
    warehouse = Warehouse(lst)
    seller = Seller('Сергей', warehouse)

    seller.sell_product(bread, 3)
    seller.sell_product(dumplings, 1)
    seller.sell_product(milk, 8)

    battery = Product('Батарейка', 10, 30.0)

    warehouse.product_list[warehouse.product_list.index(milk)].plus_qty(5)
    warehouse.add_product(battery)
    warehouse.delete_product(dumplings)

    seller.get_report()
