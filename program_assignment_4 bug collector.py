total_bugs = 0

for day in range(1, 6):
    bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs = total_bugs + bugs
print("Total number of bugs collected:", total_bugs)
