rows_on_the_field = int(input())

rows = []
for inp in range(rows_on_the_field):
    row = [int(num) for num in input().split()]
    rows.append(row)

allAtt = input().split()
destroyed_ships = 0
for att in allAtt:
    currentAtt = [int(num) for num in att.split("-")]
    row_index = currentAtt[0]
    col_index = currentAtt[1]
    if rows[row_index][col_index] > 0:
        rows[row_index][col_index] -= 1
        if rows[row_index][col_index] == 0:
            destroyed_ships += 1
print(destroyed_ships)
