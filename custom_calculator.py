# This custom calculator provides the amount of monthly payments for a Ferrari
# based on their budget and the number of monthly payments they'd like to make at
# 0% interest to pay it off.

# Formula to calculate monthly payments: Monthly Payments = {budget} / {installments}

print("Welcome to Arj's Custom Monthly Ferrari Payment Calculator!")

name = input("What's your name?")

budget = input("What's your Ferrari budget? Minimum is $100,000!")

installments = input("How many monthly installments would you like to make?")

monthly_cost = int(budget)/int(installments)

print(f"{name}'s monthly Ferrari payment is ${monthly_cost}.")
