from collections import deque

DATURA_VALUE = 40
CHERRY_VALUE = 60
SMOKE_VALUE = 120

bombs_effect = deque(int(el) for el in input().split(", "))
bombs_casing = deque(int(el) for el in input().split(", "))

we_have_bombs = True
we_have_casings = True

datura_count = 0
cherry_count = 0
smoke_count = 0

while datura_count < 3 or cherry_count < 3 or smoke_count < 3:
    if not bombs_casing or not bombs_effect:
        break

    else:
        current_bomb = bombs_effect.popleft()
        current_casing = bombs_casing.pop()
        if current_bomb + current_casing == DATURA_VALUE:
            datura_count += 1
        elif current_bomb + current_casing == CHERRY_VALUE:
            cherry_count += 1
        elif current_bomb + current_casing == SMOKE_VALUE:
            smoke_count += 1
        else:
            current_casing -= 5
            bombs_effect.appendleft(current_bomb)
            bombs_casing.append(current_casing)

if datura_count < 3 or cherry_count < 3 or smoke_count < 3:
    print("You don't have enough materials to fill the bomb pouch.")
else:
    print("Bene! You have successfully filled the bomb pouch!")

if bombs_effect:
    print(f"Bomb Effects: {', '.join(map(str, bombs_effect))}")
else:
    print("Bomb Effects: empty")

if bombs_casing:
    print(f"Bomb Casings: {', '.join(map(str, bombs_casing))}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_count}")
print(f"Datura Bombs: {datura_count}")
print(f"Smoke Decoy Bombs: {smoke_count}")