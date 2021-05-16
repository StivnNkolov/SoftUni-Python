from collections import deque

food_quantity = int(input())
orders = input().split()

orders_queue = deque()

for order in orders:
    orders_queue.append(int(order))

print(max(orders_queue))

while True:
    if not orders_queue:
        print("Orders complete")
        break
    else:
        amount = orders_queue[0]
        if amount > food_quantity:
            print(f"Orders left: {' '.join([str(order) for order in orders_queue])}")
            break
        else:
            food_quantity -= orders_queue.popleft()

