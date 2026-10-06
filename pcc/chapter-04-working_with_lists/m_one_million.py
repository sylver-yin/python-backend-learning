zero_to_million = [value + 1 for value in range(0, 1_000_000)]  # noqa: PIE808
print(zero_to_million)

million = [value for value in range(1, 1_000_001)]
print(million)

exponent_to_million = [value for value in range(1, 10**6 + 1)]
print(exponent_to_million)

# Note: Tried to do some math instead of just counting and discovered that you can actually add by one to start from zero.
# It completely erase off-by-one but might be worse than second method.
# Third one was a hypotesis but it did work! I checked all of them in CMD and they work propperly.
