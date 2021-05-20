from collections import deque
from datetime import datetime, timedelta

END_COMMAND = "End"

robots_info = input().split(";")

starting_time = datetime.strptime(input(), "%H:%M:%S")
starting_time = starting_time + timedelta(seconds=1)

robots = deque([])
available_robots = deque([])

for robot in robots_info:
    curr_robot = {}
    robot = robot.split("-")
    curr_robot["name"] = robot[0]
    curr_robot["process_time"] = int(robot[1])
    curr_robot["available_at"] = starting_time
    robots.append(curr_robot)
    available_robots.append(curr_robot)

products = deque([])

product_input = input()
while not product_input == END_COMMAND:
    products.append(product_input)
    product_input = input()

while len(products) > 0:
    curr_product = products.popleft()
    if available_robots:
        curr_r = available_robots.popleft()
        update_time = curr_r["process_time"]
        curr_r["available_at"] = starting_time + timedelta(seconds=update_time)
        robot_from_robots = [el for el in robots if el == curr_r][0]
        robot_from_robots["available_at"] = starting_time + timedelta(seconds=update_time)

        print(f"{curr_r['name']} - {curr_product} [{starting_time.strftime('%H:%M:%S')}]")
    else:

        for r in robots:
            if starting_time >= r["available_at"]:
                available_robots.append(r)
        if not available_robots:
            products.append(curr_product)
        else:

            curr_r = available_robots.popleft()
            update_time = curr_r["process_time"]
            curr_r["available_at"] = starting_time + timedelta(seconds=update_time)
            robot_from_robots = [el for el in robots if el == curr_r][0]
            robot_from_robots["available_at"] = starting_time + timedelta(seconds=update_time)
            print(f"{curr_r['name']} - {curr_product} [{starting_time.strftime('%H:%M:%S')}]")

    starting_time = starting_time + timedelta(seconds=1)
