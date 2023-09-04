# coding=utf-8

import csv
project_name = 'Personal Expense Tracker'

CSV_PATH = 'expense_data.csv'

print("==============================================================")

"""
-> display the menu of options
:return: menu of options
"""
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
print("WELCOME TO PERSONAL EXPENSE TRACKER HOME!!")
print("""What would you like to do today?:
         1. Add Expenses
         2. Update Expenses
         3. Delete Expenses 
         4. View Expense Summary
         5. Quit""")

print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
def main():
    """

    :return:
    """

    option = input("Enter your option:\n")
    if option == '1':
        add_expense()
    elif option == '2':
        update_expense()
    elif option == '3':
        expense_summary()
    elif option == '4':
        delete_expense()
    if option == '5':
        quit_app()

expenses = []
def add_expense():
    """
    adds expense data to the program
    :return: float
    """
    date = input("Enter expense date(DD-MM-YYYY):\n")
    description = input("Enter expense description:\n")
    category = input("Enter expense category:\n")
    amount = input("Enter expense amount:\nGHS")

    # writing to the csv file
    with open(CSV_PATH, "a") as csv_file:
        write_to = csv.writer(csv_file)
        write_to.writerow([date, description, category, amount])

def update_expense(date, description, category, amount):
    """
    Updates an expense in the CSV file.
    :return:
    """
    with open('expense-data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)

        for row in data:
            if row[0] == date and row[1] == description and row[2] == category:
                row[3] = amount

    with open('expense-data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(csv_file)

    # Getting new expense information from user
    date = input("Enter new expense date(DD-MM-YYYY):\n")
    description = input("Enter new expense description:\n")
    category = input("Enter new expense category:\n")
    amount = input("Enter new expense amount:\nGHS")

    # Updating the expense information in the csv file
    with open(CSV_PATH, "r") as csv_file:
        read_file = csv.reader(csv_file)
        expenses_ = list(read_file)

    # find the expense to update
    for i, expense in enumerate(expenses_):
        if expense[0] == category:
            expenses_[i] = [date, description, category, amount]
            break

    # writing the updated expense to the csv file
    with open(CSV_PATH, "w+") as csv_file:
        write_to = csv.writer(csv_file)
        write_to.writerows(expenses_)

update_expense()


def expense_summary(date, description, category, amount):
    """

    :return:
    """
    with open('expense-data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)

        for row in data:
            if row[0] == date and row[1] == description and row[2] == category:
                row[3] = amount

    with open('expenses.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(data)


def delete_expense(date, description, category):
    """

    :return:
    """
    with open('expense_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        data = list(reader)

    new_data = []
    for row in data:
        if row[0] == date or row[1] == description or row[2] == category:
            new_data.remove(row)

    with open('expense_data.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(new_data)

def quit_app():
    """
    Quits the program
    :rtype: None
    """
    quit()


if __name__ == "__main__":
    main()

