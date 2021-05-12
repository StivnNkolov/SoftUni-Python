command = input()

resources_dic = {}

while not command == "stop":
    value = int(input())
    if command not in resources_dic:
        resources_dic[command] = 0
    resources_dic[command] += value
    command = input()

for key, value in resources_dic.items():
    print(f"{key} -> {value}")