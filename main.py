import json

all_expenses = []

with open("expenses.json","r") as file:
    all_expenses = json.load(file)

def menu():
    print("========================")
    print("     Expense Tracker")
    print("========================")

    options = ["1. Add Expense", "2. View Expenses", "3. Show Total", "4. Category Summary","5. Exit"]

    for i in options:
        print(i)

def add_expense():
    
    user_amount = int(input("Enter the amount: "))
    user_category = input("Enter the catogery: ")
    user_description = input("Enter the Description: ")
    added_expenses = {
        "amount": user_amount,
        "category": user_category,
        "description": user_description,
    }
    all_expenses.append(added_expenses)
    save_expense()

    print(added_expenses)
    print("Expense Added")

def view_expense():
    for index,item in enumerate(all_expenses,start=1):
        amount = item["amount"]
        category = item["category"]
        description = item["description"]
        print(f"Expense {index}")
        print(f"Amount: {amount}")
        print(f"Catogery: {category}")
        print(f"Description: {description}")


def total_expense():
    total = 0
    for item in all_expenses:
        value = item["amount"]
        total = total + value

    print(f"Total is {total} ")


def category_summary():
    category_totals = {}
    for item in all_expenses:
        category = item["category"]
        amount = item["amount"]
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    print(category_totals)

def save_expense():
    with open("expenses.json","w")as file:
        json.dump(all_expenses,file,indent=4)

def choices(a):
    if a == 1:
        print("You selected Add Expense")
        add_expense()
    elif a == 2:
        print("You Selected View Expenses")
        view_expense()
    elif a == 3:
        print("You Selected Show Total")
        total_expense()
    elif a == 4:
        print("You Selected Category Summary")
        category_summary()


menu()
users_choice = int(input("Choose the option! "))

exit_option_choosed = 5

choices(users_choice)

while users_choice != exit_option_choosed:
    menu()

    users_choice = int(input("Choose the option! "))
    choices(users_choice)

print("Good Bye")