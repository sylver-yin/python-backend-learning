import random

given_elements = [1, 6, 2, 9, 25, 8, 0, 12, 99, 56]
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

print(f"Anyone who has these numbers will win: {winner_elements}")

my_ticket = []
loops_needed = 0
while True:
    if len(my_ticket) == 4 and set(my_ticket) == set(winner_elements):
        print(f"I won! My ticket: {my_ticket}. Tries needed: {loops_needed + 1}")
        break
    elif len(my_ticket) == 4:
        my_ticket = []
        loops_needed += 1
    else:
        random_element = random.randint(0, 99)
        if random_element in my_ticket:
            continue
        else:
            my_ticket.append(random_element)
