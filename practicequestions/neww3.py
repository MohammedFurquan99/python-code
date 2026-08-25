name = input("Enter your name: ")
monthly_budget = int(input("Enter budget: "))

number_of_expenses = int(input("How many expenses? "))

budjet_name = input("Enter expense name: ")
budjet_amount = int(input("Enter expense amount: "))

expenses = []

expenses.append({
    "expense": budjet_name,
    "amount": budjet_amount
})

total = 0

for expense in expenses:
    total = total + expense["amount"]

remaining = monthly_budget - total

print("Total expense:", total)
print("Remaining budget:", remaining)

print(expenses)