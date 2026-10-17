vacation_poll = {}
poll_active = True

while poll_active:
    name = input("\nPlease, state your name: ")
    place = input("\nIf you could visit one place in the world, where would you go? ")

    vacation_poll[name] = place

    repeat = input(
        "\nWould you like to continue the poll for another person? (yes/no) "
    )
    if repeat == "no":
        poll_active = False

print("\n_-_ Poll Results _-_")
for name, place in vacation_poll.items():
    print(f"{name.title()} want to visit {place.title()}")
