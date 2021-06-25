from collections import deque


def best_list_pureness(values, k):
    values = deque(values)
    k = min(len(values), k)
    best_rotation = 0
    best_pureness = 0
    for rotation in range(k + 1):
        current_pureness = sum(el * values.index(el) for el in values)
        if best_pureness < current_pureness:
            best_pureness = current_pureness
            best_rotation = rotation
        values.appendleft(values.pop())

    return f"Best pureness {best_pureness} after {best_rotation} rotations"




test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
