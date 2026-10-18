import math

# Get user input
square_feet = float(input("Enter square feet of wall space: "))
paint_price = float(input("Enter price of paint per gallon: $"))

# Calculations
gallons_needed = math.ceil(square_feet / 112)
labor_hours = (square_feet / 112) * 8

paint_cost = gallons_needed * paint_price
labor_cost = labor_hours * 35
total_cost = paint_cost + labor_cost

# Display results
print("\nPaint Job Estimate")
print("-------------------")
print(f"Gallons of paint required: {gallons_needed}")
print(f"Hours of labor required: {labor_hours:.2f}")
print(f"Cost of paint: ${paint_cost:.2f}")
print(f"Labor charges: ${labor_cost:.2f}")
print(f"Total cost: ${total_cost:.2f}")
