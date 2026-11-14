favorite_places = {
    "Colin": ["Amazon rainforest"],
    "Martha": ["Brno city", "Great Chinese Wall"],
    "Rory": ["Starbucks", "Paris", "Local gym"],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name} favorite place is \n\t{places[0]}")
    else:
        print(f"\n{name} favorite places are:")
        for place in places:
            print(f"\t{place}")
