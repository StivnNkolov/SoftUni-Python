# # От конзолата се четат 3 реда:
# # 1.	Брой страници в текущата книга – цяло число;
# # 2.	Страници, които може да прочита за 1 час – цяло число;
# # 3.	Броя на дните, за които трябва да прочете книгата – цяло число;
# # Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
#
# първо трябвя да разделиме броя страници в една книга на страниците които чете за един час и полуцхажаме за колко часа ще
# прочете една книга. след това делим часовете за една книга на дните които са му дадени за една книга и получаваме колко
# часа на ден трябва да отдели за една книга.

pages_in_one_book = int(input())
pages_for_one_hour = int(input())
days_for_one_book = int(input())

hours_for_one_book = pages_in_one_book / pages_for_one_hour
hour_in_one_day_for_reading = hours_for_one_book / days_for_one_book
print(hour_in_one_day_for_reading)