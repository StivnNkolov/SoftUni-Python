from collections import deque

pizza_orders = deque(int(el) for el in input().split(", ") if 0 < int(el) <= 10)
employees_values = deque(int(el) for el in input().split(", "))

completed_orders = 0
do_we_have_employees = True
while pizza_orders:
    current_pizza = pizza_orders.popleft()
    current_employee = employees_values.pop()
    if current_pizza <= current_employee:
        completed_orders += current_pizza
    else:
        current_pizza -= current_employee
        completed_orders += current_employee
        pizza_orders.appendleft(current_pizza)
        if not employees_values:
            do_we_have_employees = False
            break

if not do_we_have_employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(map(str, pizza_orders))}")
else:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {completed_orders}")
    print(f"Employees: {', '.join(map(str, employees_values))}")