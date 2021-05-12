# кучета е на цена 2.50лв., а всяка останала, която не е за тях струва 4лв.
# От конзолата се четат 2 реда:
# 1.	Броят на кучетата - цяло число;
# 2.	Броят на останалите животни  - цяло число.
# На конзолата се отпечатва:
# "{крайната сума} lv."

dogs = int(input())
animals = int(input())
dogsFood = 2.5
animalsFood = 4
priceDogs = dogs * dogsFood
priceAnimals = animals * animalsFood
finalPrice = priceDogs + priceAnimals
print(f"{finalPrice} lv.")


dogs = int(input())
animals = int(input())
print(f"{((dogs * 2.5) + (animals * animalsFood))}")


