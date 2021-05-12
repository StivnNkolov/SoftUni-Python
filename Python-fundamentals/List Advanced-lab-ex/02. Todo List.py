to_do_notes = input()
my_list = [0] * 10

while not to_do_notes == "End":
    importance, task = to_do_notes.split("-")
    importance = int(importance) - 1
    my_list[importance] = task
    to_do_notes = input()

new_list = []
for task in my_list:
    if not task == 0:
        new_list.append(task)
print(new_list)