# Number Analysis Program

numbers = []

# Get 20 numbers from the user
for i in range(20):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Calculate results
lowest = min(numbers)
highest = max(numbers)
total = sum(numbers)
average = total / len(numbers)

# Display results
print("\nNumber Analysis Results")
print("-----------------------")
print("Lowest number:", lowest)
print("Highest number:", highest)
print("Total:", total)
print("Average:", average)
