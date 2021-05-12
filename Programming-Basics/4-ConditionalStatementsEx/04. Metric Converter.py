# Входните данни се състоят от три реда, въведени от потребителя:
# •	Първи ред: число за преобразуване - реално число;
# •	Втори ред: входна мерна единица – текст;
# •	Трети ред: изходна мерна единица (за резултата) – текст.

number = float(input())
enter_metric = input()
out_metric = input()
final_number = 0
if enter_metric == "mm":
    if out_metric == "cm":
        final_number = number / 10
    elif out_metric == "m":
        final_number = number / 1000
elif enter_metric == "cm":
    if out_metric == "m":
        final_number = number / 100
    elif out_metric == "mm":
        final_number = number * 10
elif enter_metric == "m":
    if out_metric == "cm":
        final_number = number * 100
    elif out_metric == "mm":
        final_number = number * 1000
print(f"{final_number:.3f}")
