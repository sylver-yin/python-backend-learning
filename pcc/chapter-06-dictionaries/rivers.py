about_rivers = {
    "eGYPT": "NiLE",
    "South AmeRICa": "Amazon",
    "north America": "mississippi",
}

print("Here is some info about three famous rivers:")
for region, river in about_rivers.items():
    print(f"{river.title()} runs through {region.title()}")

print("\nRegions:")
for region in about_rivers:
    print(f"{region.title()}")

print("\nRivers:")
for river in about_rivers.values():
    print(f"{river.title()}")

# NOTE: If possible it's better to make less loops and combine when it's not ruining the logic, but here it would be a mistake.
