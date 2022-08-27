from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, title, count):
        """Увеличивает запас items"""
        pass

    @abstractmethod
    def remove(self, title, count):
        """Уменьшает запас items"""
        pass

    @property
    @abstractmethod
    def get_free_space(self):
        """Возвращает количество свободных мест"""
        pass

    @property
    @abstractmethod
    def items(self):
        """Возвращает содержание склада"""
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self):
        """Возвращает количество уникальных товаров"""
        pass


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count

    def remove(self, title, count):
        result = self._items[title] - count
        if result > 0:
            self._items[title] = result
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20


class Request:
    def __init__(self, data):
        self.data = self._split_data(data)

        self.from_ = self.data[4]
        self.to = self.data[6]
        self.amount = int(self.data[1])
        self.product = self.data[2]

    @staticmethod
    def _split_data(data):
        return data.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"
