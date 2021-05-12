target = 10000

steps_she_make = 0

while steps_she_make < target:
    steps = input()
    if steps == "Going home":
        steps = int(input())
        steps_she_make += steps
        break
    steps_she_make += int(steps)

diff = abs(target - steps_she_make)
if steps_she_make >= target:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")