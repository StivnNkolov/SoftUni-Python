# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# •	Първият ред съдържа час на изпита – цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита – цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане – цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане – цяло число от 0 до 59.

hour_for_exam = int(input())
minute_of_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

if hour_for_exam == arrival_hour:
    if minute_of_exam == arrival_minute:
        print("On time.")