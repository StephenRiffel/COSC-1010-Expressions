years = int(input("Enter the number of years: "))

total_rainfall = 0.0
total_months = years * 12

for year in range(1, years + 1):
    print ("Year", year)

    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall for month {month}: "))
        total_rainfall = total_rainfall + rainfall

average_rainfall = total_rainfall / total_months

print("Total number of months:", total_months)
print("Total rainfall:", total_rainfall)
print("Average rainfall per month:", average_rainfall)
