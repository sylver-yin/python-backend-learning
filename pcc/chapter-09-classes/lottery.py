import random

given_elements = [1, "A", 6, 2, "S", 9, "E", 25, 8, "R", 0, 12, "M", 99, 56]
winner_elements = []
while True:
    if len(winner_elements) >= 4:
        break
    else:
        winner_combination = random.choice(given_elements)
        if winner_combination in winner_elements:
            continue
        else:
            winner_elements.append(winner_combination)

print(f"Anyone who has these numbers or letters will win: {winner_elements}")
