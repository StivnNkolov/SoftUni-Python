rows_count = int(input())

rows = []

for r in range(rows_count):
    row = input().split()
    rows.append(row)
    print(row)
print(rows)