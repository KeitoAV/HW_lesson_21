from classes import Request, Store, Shop


def main(store, shop):
    while True:
        print('Пример ввода запроса == Доставить 3 мороженое из склад в магазин ==')
        print('Чтобы завершить работу введите == стоп ==')
        user_input = input('Введите запрос: ').lower()

        if user_input == 'стоп':
            break

        try:
            request = Request(user_input)
        except Exception as e:
            print(f'Некорректный запрос: {e}')
            print(f'Пример правильного запроса:'
                  f'Доставить 3 мороженое из склад в магазин')
            continue

        from_ = store if request.from_ == 'склад' else shop
        to = shop if request.to == 'магазин' else store

        if request.product in from_.items:
            print(f"Нужный товар есть в {request.from_}")
        else:
            print(f"В {request.from_} нет такого товара")
            continue

        if from_.items[request.product] >= request.amount:
            print(f"Нужное количество есть в {request.from_}")
        else:
            print(f"В {request.from_} не хватает {request.amount - from_.items[request.product]}")
            continue

        if to.get_free_space >= request.amount:
            print(f"В {request.to} достаточно места")
        else:
            print(f"В {request.to} не хватает места: {request.amount - to.get_free_space}")
            continue

        if request.to == "магазин" and to.get_unique_items_count == 5 and request.product not in to.items:
            print("Количество уникальных товаров в магазине не должно быть > 5")
            continue

        from_.remove(request.product, request.amount)
        print(f"Курьер забрал {request.amount} {request.product} из пункта {request.from_}")
        print(f"Курьер везёт {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}")
        to.add(request.product, request.amount)
        print(f"Курьер доставил {request.amount} {request.product} из пункта {request.to}")

        print("*" * 50)
        print(f"На складе хранится:")
        for title, count in store.items.items():
            print(f"{title}: {count}")
        print(f"\nСвободного места - {store.get_free_space}")
        print("*" * 50)
        print(f"В магазине хранится:")
        for title, count in shop.items.items():
            print(f"{title}: {count}")
        print(f"\nСвободного места - {shop.get_free_space}")
        print("*" * 50)


if __name__ == '__main__':
    store = Store()
    shop = Shop()

    goods_quantity = {
        "торт": 10,
        "шоколад": 10,
        "мороженое": 10,
        "зефир": 10,
        "печенье": 10,
        "пастила": 10
    }
    store.items = goods_quantity
    main(store, shop)
