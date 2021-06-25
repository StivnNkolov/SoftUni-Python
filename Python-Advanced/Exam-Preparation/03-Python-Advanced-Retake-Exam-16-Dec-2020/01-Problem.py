from collections import deque

males_data = deque(int(el) for el in input().split())
females_data = deque(int(el) for el in input().split())

matches = 0

while females_data and males_data:
    current_female = females_data.popleft()
    current_male = males_data.pop()

    if current_female <= 0:
        males_data.append(current_male)
        continue
    if current_male <= 0:
        females_data.appendleft(current_female)
        continue

    if current_female % 25 == 0:
        females_data.popleft()
        males_data.append(current_male)
        continue

    if current_male % 25 == 0:
        males_data.pop()
        females_data.appendleft(current_female)
        continue

    if current_male == current_female:
        matches += 1

    else:
        current_male -= 2
        males_data.append(current_male)


print(f"Matches: {matches}")
if not males_data:
    print("Males left: none")
else:
    top = males_data.reverse()
    print(f"Males left: {', '.join([str(el) for el in males_data])}")
if not females_data:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(list(map(str, females_data)))}")