income = float(input("Enter your monthly income: "))

# Prompt the user for their total monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Calculate projected annual savings with 5% simple interest
annual_savings = monthly_savings * 12
projected_savings = annual_savings + (annual_savings * 0.05)

# Display results
print(f"\nYour monthly savings are: {monthly_savings}")
print(f"Your projected savings after one year (with 5% interest): {projected_savings}")