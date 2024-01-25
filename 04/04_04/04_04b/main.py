primary_colors = frozenset(["red", "blue", "yellow"])

if "blue" in primary_colors:
  print("Blue in the set!")

#cannot add to the set as it is immutable
#prevent unwanted changes to the initial set
primary_colors.add("green")