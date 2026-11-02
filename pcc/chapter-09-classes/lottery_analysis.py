import random

given_elements = [1, "A", 6, 2, "C", 9, "E", 25, 8, "F", 0, 12, "G", 99, 56]
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

my_ticket = []
possible_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
loops_needed = 0
while True:
    if len(my_ticket) == 4 and my_ticket in winner_elements:
        print(f"I won! My ticket: {my_ticket}. Tries needed: {loops_needed}")
        break
    elif len(my_ticket) == 4 and my_ticket not in winner_elements:
        my_ticket = []
    else:
        coin_flip = random.randint(1, 2)
        if coin_flip == 1:
            random_element = random.randint(0, 99)
        else:
            random_element = random.choice(possible_letters)
        if random_element in my_ticket:
            continue
        else:
            my_ticket.append(random_element)
            loops_needed += 1
