# coding=utf-8
"""

"""
import csv

project_name = 'Py Expense Tracker'


CSV_PATH = 'expense_data.csv'

def display_menu():
    """

    :return:
    """
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    print("""Select your option:
        1. Add Expenses
        2. Update Expenses
        3. Delete Expenses 
        4. View Expense Summary
        5. Quit""")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    input("Enter your choice (1, 2, 3, 4, 5 ): \n")
display_menu()

def main():
    """

    :return:
    """
    print("==============================================================")
    print(project_name)
    display_menu()
    add_expense()
    update_expense()
    expense_summary()
    delete_expense()
    quit()

expenses = []
def add_expense():
    """

    :return: float
    """
    date = input("Enter expense date(DD-MM-YYYY):\n")
    description = input("Enter expense description:\n")
    category = input("Enter expense category:\n")
    amount = input("Enter expense amount in GHS:\n")

    # writing to the csv file
    with open(CSV_PATH, "a") as csv_file:
        write_to = csv.writer(csv_file)
        write_to.writerow([date,
                           description,
                           category,
                           amount])

add_expense()

def update_expense():
    """

    :return:
    """
    expense_id = input("Enter expense ID:\n")

    # Getting new expense information from user
    date = input("Enter new expense date(DD-MM-YYYY):\n")
    description = input("Enter new expense description:\n")
    category = input("Enter new expense category:\n")
    amount = input("Enter new expense amount in GHS:\n")

    # Updating the expense information in the csv file
    with open(CSV_PATH, "r") as csv_file:
        read_file = csv.reader(csv_file)
        expenses = list(read_file)

    # find the expense to update
    for i, expense in enumerate(expenses):
        if expense[0] == expense_id:
            expense[i] = [date, description, category, amount]
            break

    # writing the updated expense to the csv file
    with open(CSV_PATH, "w") as csv_file:
        write_to = csv.writer(csv_file)
        write_to.writerows(expenses)


update_expense()


def expense_summary():
    """

    :return:
    """

def delete_expense():
    """

    :return:
    """

delete_expense()

def quit():
    """

    :rtype: object
    """
quit()


if __name__ == "__main__":
    main()

