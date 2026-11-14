lizards = ["komodo dragon", "bearded dragon", "iguana", "chameleon", "crested gecko"]
print(lizards)

lizards.remove("iguana")
print(lizards)

mammalians = ["dog", "fox", "hyena", "duck", "bear", "badger"]
print(mammalians)

not_a_mammal = "duck"
mammalians.remove(not_a_mammal)
print(mammalians)
print(f"\nSorry, but {not_a_mammal.title()} is not a mammal. Try something else.")
