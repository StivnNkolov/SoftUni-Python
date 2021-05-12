width = int(input())
lenght = int(input())

cake_volume = width * lenght

comand = input()
while comand != "STOP":
    cake_volume -= int(comand)
    if cake_volume < 1:
        break
    comand = input()

if cake_volume >= 1:
    print(f"{cake_volume} pieces are left." )
else:
    print(f"No more cake left! You need {abs(cake_volume)} pieces more.")


# width = int(input())
# lenght = int(input())
#
# cake_volume = width * lenght
#
# while cake_volume > 0:
#     comand = input()
#     if comand != "STOP":
#         cake_volume -= int(comand)
#     else:
#
#         break
#
# if cake_volume <= 0:
#     print(f"No more cake left! You need {abs(cake_volume)} pieces more.")
# if comand == "STOP":
#     print(f"{abs(cake_volume)} pieces are left.")


