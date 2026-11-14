lizard = "komodo dragon"
print("Is lizard == 'komodo dragon'? I predict True")
print(lizard == "komodo dragon")

print("Is lizard == 'crested gecko'? I predict False")
print(lizard == "crested gecko")

car = "toyota"
print("\nIs car == 'audi'? I expect False")
print(car == "audi")

print("Is car == 'toyota'? I expect True")
print(car == "toyota")

beverage = "soda"
print("\nIs beverage == 'Coca Cola'? I expect False")
print(beverage == "Coca Cola")

print("Is beverage == 'soda'? I expect True")
print(beverage == "soda")

game = "Monster Hunter"
print("\nIs game == 'Monster Hunter'? I expect True")
print(game == "Monster Hunter")

print("Is game == 'Super Metroid'? I expect False")
print(game == "Super Metroid")

power = "off"
print("\nIs power == 'off'? I expect True")
print(power == "off")

print("Is power == 'on'? I expect False")
print(power == "on")

sweet = "candy"
print("\nIs sweet == 'candy'? I expect True")
print(sweet == "candy")

print("Is sweet == 'fruit'? I expect False")
print(sweet == "fruit")

list_true = [
    car == "toyota",
    beverage == "soda",
    game == "Monster Hunter",
    power == "off",
    sweet == "candy",
]
print("\nHere's amount of True:")
print(list_true)
print(len(list_true))

list_false = [
    car == "audi",
    beverage == "Coca Cola",
    game == "Super Metroid",
    power == "on",
    sweet == "fruit",
]
print("\nHere's the amount of False:")
print(list_false)
print(len(list_false))
