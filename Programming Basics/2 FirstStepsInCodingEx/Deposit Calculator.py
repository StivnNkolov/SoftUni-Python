# каква сума ще получите в края на депозитния период при определен лихвен процент

# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)
# От конзолата се четат 3 реда:
# 1.	Депозирана сума – реално число;
# 2.	Срок на депозита(в месеци) – цяло число;
# 3.	Годишен лихвен процент – реално число;
# Да се отпечата на конзолата сумата в края на срока.

deposit = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input())
# purvo namirame kolko sa 12% ot depoziranata suma. taka razbirame kolko pari pechelim za godina ot lihvata.
# sled tova delim pechalbata za godian na 12 za da razberem klolko e pechalbata za mesec.Nakraq umnojavamme pechalbata
# za mesec po sroka na depozata za da vidim kolko pechalba shte imame za perioda na depozita.Subirame depoziranata suma s
# pechalbata za celiqa period na depozita.Printirame
# interest = annual_interest_rate / 100
year_profit = deposit * (annual_interest_rate / 100)
month_profit = year_profit / 12
profit_for_the_term = term_of_deposit * month_profit
final_profit = deposit + profit_for_the_term
print(final_profit)
