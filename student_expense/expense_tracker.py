name = input("Enter your name: ")
monthly_budget = int(input("Enter budget: "))

number_of_expenses = int(input("How many expenses? "))

expense_name = input("Enter expense name: ")
expense_amount = int(input("Enter expense amount: "))

expenses = []

expenses.append({
    "expense": expense_name,
    "amount": expense_amount
})

total = 0

for expense in expenses:
    total = total + expense["amount"]

remaining = monthly_budget - total

print("Total expense:", total)
print("Remaining budget:", remaining)

print(expenses)