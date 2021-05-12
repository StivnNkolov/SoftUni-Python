start = int(input())
end = int(input())
magic = int(input())

counter = 0
is_found = False

for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic:
            is_found = True
            print(f"Combination N:{counter} ({i} + {j} = {magic})")
            break
    if is_found:
        break
if not is_found:
    print(f"{counter} combinations - neither equals {magic}")
