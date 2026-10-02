transport = ["car", "bicycle", "ship", "plane"]

i_would_never = f"I would never use a {transport[-2].title()} for traveling!"
i_could = f"I think I could tolerate {transport[-1].title()} as long as I'm with you."
dont_care = f"I already get used to use {transport[1].title()} since I use it everyday."
big_yes = (
    f"I love to travel with {transport[0].title()}, it's the most relaxing and calm."
)
print(i_would_never, i_could, dont_care, big_yes)
