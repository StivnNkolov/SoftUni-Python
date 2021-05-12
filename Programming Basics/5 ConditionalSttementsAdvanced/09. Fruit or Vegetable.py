# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук
product = input()
# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".
if product == "banana" or product == "apple" or product == "kiwi" or product == "cherry" or product == "lemon" or product == "grapes":
    print("fruit")
elif product == "tomato" or product == "cucumber" or product == "pepper" or product == "carrot":
    print("vegetable")
else:
    print("unknown")