import json

# Загрузка данных из файла
with open("orders_july_2023.json", "r") as file:
    orders = json.load(file)

# 1. Какой номер самого дорого заказа за июль?
max_price = 0
max_price_order = None
for order_num, order_data in orders.items():
    if order_data['price'] > max_price:
        max_price = order_data['price']
        max_price_order = order_num

# 2. Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_quantity_order = None
for order_num, order_data in orders.items():
    if order_data['quantity'] > max_quantity:
        max_quantity = order_data['quantity']
        max_quantity_order = order_num

# 3. В какой день в июле было сделано больше всего заказов?
date_counts = {}
for order_data in orders.values():
    date = order_data['date']
    date_counts[date] = date_counts.get(date, 0) + 1
most_orders_date = max(date_counts, key=date_counts.get)

# 4. Какой пользователь сделал самое большое количество заказов за июль?
user_order_counts = {}
for order_data in orders.values():
    user_id = order_data['user_id']
    user_order_counts[user_id] = user_order_counts.get(user_id, 0) + 1
most_orders_user = max(user_order_counts, key=user_order_counts.get)

# 5. У какого пользователя самая большая суммарная стоимость заказов за июль?
user_total_spent = {}
for order_data in orders.values():
    user_id = order_data['user_id']
    user_total_spent[user_id] = user_total_spent.get(user_id, 0) + order_data['price']
highest_spending_user = max(user_total_spent, key=user_total_spent.get)

# 6. Какая средняя стоимость заказа была в июль?
total_price = sum(order_data['price'] for order_data in orders.values())
average_order_price = total_price / len(orders)

# 7. Какая средняя стоимость товаров в июль?
total_items = sum(order_data['quantity'] for order_data in orders.values())
average_item_price = total_price / total_items

# Вывод результатов
print(f"1. Номер самого дорого заказа: {max_price_order}")
print(f"2. Номер заказа с самым большим количеством товаров: {max_quantity_order}")
print(f"3. День с наибольшим количеством заказов: {most_orders_date}")
print(f"4. Пользователь с наибольшим количеством заказов: {most_orders_user}")
print(f"5. Пользователь с наибольшей суммарной стоимостью заказов: {highest_spending_user}")
print(f"6. Средняя стоимость заказа: {average_order_price:.2f}")
print(f"7. Средняя стоимость товара: {average_item_price:.2f}")
