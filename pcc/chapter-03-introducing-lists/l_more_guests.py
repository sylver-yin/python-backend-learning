guest_list = ["Mom", "Dad", "Oleg", "John"]
print(
    f"Hello, {guest_list[0]}, I invite you for the Dinner tonight, at 7 PM. See you around!"
)
print(
    f"Hello, {guest_list[1]}, I would like to see you at my dinner tonight, at 7 PM to be precise. See ya!"
)
print(
    f"Hi, {guest_list[2]}! Bro, Come to the dinner tonight, wait you at 7 PM! Alright, catch ya later!"
)
print(
    f"Hello, my dear colleague {guest_list[3]}, I think it would be good idea to invite you to my dinner at 7 PM. Have a nice day."
)
print("Change of plans! New guests are going to be there since I found a bigger table!")

guest_list.insert(0, "Rory")
guest_list.insert(2, "Chris")
guest_list.insert(5, "Sarah")
print(f"Hello, {guest_list[0]}, I'm glad to invite you to my dinner at 7 PM!")
print(f"Hi, {guest_list[2]}, I'm glad to invite you to my dinner at 7 PM!")
print(f"Howdy, {guest_list[5]}, I'm glad to invite you to my dinner at 7 PM!")
