football_players = ["rory", "lilly", "sarah"]
for player_01 in football_players:
    print(f"\nHey, {player_01.title()}, you performed well!")
    print(f"Will be glad to see you again next week, {player_01.title()}")
# In that case, they go bilinear.
# So instead of doing FIRST command completely, like A-A...-A and and THEN start the second like B-B...-B,
# It will do A-B-A-B...-A-B till it finishes the entire loop.

for player_02 in football_players:
    print(f"Hey, that was a good one, {player_02.title()}")
print(f"I'm not disappointed in you, {player_02.title()}\n")
# Here is an another principe. It goes AFTER the loop so it's not indented and will not be repeated with each variable.
# That means it will associate only with the final variable in "player_02", which is "sarah" in this case.
# It might be either a good instrument or either a logical error - depends on the situation.
