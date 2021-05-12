# един кв. м. е 7.61лв със ДДС.
#
# 18% отстъпка от крайната цена.
#
# От конзолата се прочита само един ред:
# 1.	Кв. метри, които ще бъдат озеленени – реално число.
# #
# •	"The final price is: {крайна цена на услугата} lv."
# •	"The discount is: {отстъпка} lv."

s = float(input())
firstPrice = s * 7.61
discount = firstPrice * 0.18
finalPrice = firstPrice - discount
print(f"The final price is: {finalPrice} lv.")
print(f"The discount is: {discount} lv.")

s1 = float(input())
print(f"The final price is: {(s1 * 7.61) - ((s1 * 7.61) * 0.18)} lv.")
print(f"The discount is: {((s1 * 7.61) * 0.18)} lv.")

