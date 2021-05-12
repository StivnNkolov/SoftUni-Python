first = int(input())
second = int(input())

print(f"Before:")
print(f"a = {first}")
print(f"b = {second}")

second, first = first, second
print(f"After:")
print(f"a = {first}")
print(f"b = {second}")