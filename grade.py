points_possible = float(input("Total Points Possible: "))
earned_points = float(input("Points Achieved: "))

if points_possible > 0:
    percentage = (earned_points / points_possible) * 100
else:
    print("Total points possible cannot be zero")

if 0 <= percentage <= 50:
    grade = "F"
elif 51 <= percentage <= 60:
    grade = "D"
elif 61 <= percentage <= 75:
    grade = "C"
elif 76 <= percentage <= 88:
    grade = "B"
elif 89 <= percentage <= 100:
    grade = "A"
else:
    grade = "invalid percentage"

print(f"Letter Grade: {grade}")