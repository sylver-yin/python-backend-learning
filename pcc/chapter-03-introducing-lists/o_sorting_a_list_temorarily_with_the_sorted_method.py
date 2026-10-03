cats = ["calico", "tabi", "orange", "siamese"]
print("Here's the original list:")
print(cats)

print("\nHere's the sorted list:")
print(sorted(cats))

print("\nHere's the original list again:")
print(cats)

# Now I want to add how to do reverse for sort() function, since it's not in the book for me
cats_reversed = sorted(
    cats, reverse=True
)  # For reverse, we need to put it in the same parentheses as our list name
print("\nHere's the reversed list:")
print(cats_reversed)

print("\nHere's the original list, once again:")
print(cats)
