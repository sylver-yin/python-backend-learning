million = []
for number in range(0, 1_000_000):  # noqa: PIE808
    from_to = number + 1
    million.append(from_to)

print(min(million))
print(max(million))
print(sum(million))
