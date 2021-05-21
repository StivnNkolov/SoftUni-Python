from collections import deque

price_for_each_bullet = int(input())
number_of_barrels = int(input())

bullets = deque([int(el) for el in input().split()])
locks = deque([int(el) for el in input().split()])
initial_money_for_the_task = int(input())

locks1 = ([])
while locks:
    what_we_need = locks.pop()
    locks1.append(what_we_need)

all_bullets_shot = 0
bull_in_current_barrel = 0

job_done = True

while locks1:
    curr_lock = locks1.pop()
    curr_bullet = bullets.pop()
    all_bullets_shot += 1
    bull_in_current_barrel += 1

    if curr_bullet <= curr_lock:
        print("Bang!")
    else:
        print("Ping!")
        locks1.append(curr_lock)

    if bullets:
        if bull_in_current_barrel == number_of_barrels:
            bull_in_current_barrel = 0
            print("Reloading!")
    else:
        if locks1:
            job_done = False
            break


money_he_earned = initial_money_for_the_task - (all_bullets_shot * price_for_each_bullet)

if job_done:
    print(f"{len(bullets)} bullets left. Earned ${money_he_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks1)}")