n, m = tuple([int(el) for el in tuple(input().split())])

n_set = set()
m_set = set()

for _ in range(n):
    num = int(input())
    n_set.add(num)

for _ in range(m):
    num1 = int(input())
    m_set.add(num1)

unique_items_in_both_sets = n_set & m_set
[print(item) for item in unique_items_in_both_sets]