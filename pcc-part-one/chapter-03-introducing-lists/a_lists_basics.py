owl_kinds = ["snowy_owl", "barn_owl", "athene noctua", "eagle owl"]
print(owl_kinds)

drinks = ["soda", "water", "tea", "coffee"]  # Lists start with an index of 0, not 1.
print(drinks[0])
print(drinks[3])
print(
    drinks[-1]
)  # Negative index returns elements from the end. For instance, '-1' will give the last, '-2' give the second from the end etc.

cereal = ["corn", "chocolate"]
print(cereal[0].title())

health_recommendation = f"Dr. Sam says, that {drinks[-2].upper()} and {drinks[1].title()} is better than {drinks[0].lower()}"
print(health_recommendation)
