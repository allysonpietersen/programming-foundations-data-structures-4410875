seating_chart = [
    ["Sarah", "CLaire", "Ben", "Taylor", "Eva"],
    ["Frankie", "George", "Lindsey", "Izzy", "Jack"],
    ["Katherine", "Lauren", "Mary", "Nathan", "Olive"],
    ["Chad", "April", "Matt", "Thomas", "Penny"]
]

#accessing the 2nd student in the 3rd row
print(seating_chart[2][1])

#display each student with row and seat number
# for i, row in enumerate(seating_chart):
#   print(f"row {i+1}, student {row}")

#display the seat number as well
for i, row in enumerate(seating_chart):
    for j, student_name in enumerate(row):
        print(f"{student_name} is in row {i+1} and seat {j+1}")