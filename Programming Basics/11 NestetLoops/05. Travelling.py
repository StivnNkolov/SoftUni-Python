destination = input()


while destination != "End":
    sum = 0
    budget = float(input())
    while sum < budget:
        money = float(input())
        sum += money
    else:
        print(f"Going to {destination}!")

    destination = input()