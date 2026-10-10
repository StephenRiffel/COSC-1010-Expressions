# Program Assignment 5 - Functions
# Automobile Costs
# Stephen Riffel

def monthly_cost(loan, insurance, gas, oil, tires, maintenance):
    return loan + insurance + gas + oil + tires + maintenance


def annual_cost(monthly):
    return monthly * 12


def main():
    print("Automobile Expense Calculator\n")

    loan = float(input("Enter monthly loan payment: $"))
    insurance = float(input("Enter monthly insurance cost: $"))
    gas = float(input("Enter monthly gas cost: $"))
    oil = float(input("Enter monthly oil cost: $"))
    tires = float(input("Enter monthly tire cost: $"))
    maintenance = float(input("Enter monthly maintenance cost: $"))

    monthly = monthly_cost(
        loan,
        insurance,
        gas,
        oil,
        tires,
        maintenance
    )

    yearly = annual_cost(monthly)

    print("\nExpense Summary")
    print(f"Total Monthly Cost: ${monthly:.2f}")
    print(f"Total Annual Cost:  ${yearly:.2f}")


main()
