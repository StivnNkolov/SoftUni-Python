cards_input = input().split()
count_of_shuffles = int(input())

half = int(len(cards_input) / 2)

for shuffle in range(count_of_shuffles):
    left_half = cards_input[:half]
    right_half = cards_input[half:]
    current_deck = []
    for card_index in range(len(left_half)):
        current_deck.append(left_half[card_index])
        current_deck.append(right_half[card_index])
    cards_input = current_deck

print(cards_input)
