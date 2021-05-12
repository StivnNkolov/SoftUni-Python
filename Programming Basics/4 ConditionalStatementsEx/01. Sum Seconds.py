first = int(input())
second = int(input())
third = int(input()) #v sekundi

time_for_all_three = first + second + third
minutes = time_for_all_three // 60
seconds = time_for_all_three % 60
if seconds <= 9:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
