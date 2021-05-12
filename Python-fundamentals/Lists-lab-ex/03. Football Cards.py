cards = input().split()
set_cards = set(cards)

is_stopped = False

team_a = 11
team_b = 11

for card in set_cards:
    if "A" in card:
        team_a -= 1
    elif "B" in card:
        team_b -= 1
    if team_b < 7 or team_a < 7:
        is_stopped = True
        break


print(f"Team A - {team_a}; Team B - {team_b}")
if is_stopped:
    print("Game was terminated")
