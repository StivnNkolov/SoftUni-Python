suma = input()

deposit = 0
tottal_sum = 0

while suma != "NoMoreMoney":
    deposit = float(suma)
    if deposit < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {float(suma):.2f}")
    tottal_sum += deposit
    suma = input()
print(f"Total: {tottal_sum:.2f} ")


