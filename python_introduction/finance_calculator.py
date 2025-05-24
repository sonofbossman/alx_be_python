monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
annual_interest = 0.05
number_of_month = 12
total_savings = monthly_savings * number_of_month
annual_sav_projection = total_savings + (total_savings * annual_interest)

print(f"Your monthly savings are ${int(monthly_savings)}.")
print(f"Projected savings after one year, with interest, is: ${int(annual_sav_projection)}.")