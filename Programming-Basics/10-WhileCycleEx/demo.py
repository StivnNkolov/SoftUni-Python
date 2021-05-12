width = int(input())
lengt = int(input())
high = int(input())

volume = width * lengt * high
boxes_space = 0
while volume > 0:
    boxes = input()
    if boxes != "Done":
        boxes_space = int(boxes)
        volume -= boxes_space
    else:
        print(f"{abs(volume)} Cubic meters left.")
        break
if volume <= 0:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")