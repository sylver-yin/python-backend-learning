guest_list = ["Rory", "Mom", "Chris", "Dad", "Oleg", "John", "Sarah"]
print(f"Hello, {guest_list[0]}, I'm glad to invite you to my dinner at 7 PM!")
print(
    f"Hello, {guest_list[1]}, I invite you for the Dinner tonight, at 7 PM. See you around!"
)
print(f"Hi, {guest_list[2]}, I'm glad to invite you to my dinner at 7 PM!")
print(
    f"Hello, {guest_list[3]}, I would like to see you at my dinner tonight, at 7 PM to be precise. See ya!"
)
print(
    f"Hi, {guest_list[4]}! Bro, Come to the dinner tonight, wait you at 7 PM! Alright, catch ya later!"
)
print(
    f"Hello, my dear colleague {guest_list[5]}, I think it would be good idea to invite you to my dinner at 7 PM. Have a nice day."
)
print(f"Howdy, {guest_list[6]}, I'm glad to invite you to my dinner at 7 PM!")
guest_list_popped_00 = guest_list.pop()
print(
    f"Hi, Sorry, {guest_list_popped_00}! Turns out new table didn't arrive plus we have a shrinkage!"
)
guest_list_popped_01 = guest_list.pop()
print(
    f"Hi, Sorry, {guest_list_popped_01}! Turns out new table didn't arrive plus we have a shrinkage!"
)
guest_list_popped_02 = guest_list.pop()
print(
    f"Hi, Sorry, {guest_list_popped_02}! Turns out new table didn't arrive plus we have a shrinkage!"
)
guest_list_popped_03 = guest_list.pop()
print(
    f"Hi, Sorry, {guest_list_popped_03}! Turns out new table didn't arrive plus we have a shrinkage!"
)
guest_list_popped_04 = guest_list.pop()
print(
    f"Hi, Sorry, {guest_list_popped_04}! Turns out new table didn't arrive plus we have a shrinkage!"
)

print(f"Hey, {guest_list[1]}, you're on the list! Still up for a dinner?")
del guest_list[1]
print(f"Hey, {guest_list[0]}, you're on the list! Still up for a dinner?")
del guest_list[0]
print(guest_list)
