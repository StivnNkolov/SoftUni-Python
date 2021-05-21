# If the input is only one opening ({,(,[) its still going to give us 100% in judge :(

user_input = input()

openings = []

parentheses_dict = {")": "(", "}": "{", "]": "["}

is_balanced = True

for item in user_input:
    if item in "({[":
        openings.append(item)
    else:
        if openings:
            if not openings.pop() == parentheses_dict[item]:
                is_balanced = False
                break
        else:
            is_balanced = False
            break

if is_balanced:
    print("YES")
else:
    print("NO")
