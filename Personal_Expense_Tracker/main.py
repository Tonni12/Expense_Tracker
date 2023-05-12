# coding=utf-8
"""
This project seeks to bukl
"""
project_name = 'Py Expense Tracker'
def display_menu():
    """

    :return:
    """
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    print("""Select your option:
        1. Add Expenses
        2. View Expenses
        3. Update Expenses
        4. Delete Expenses 
        5. View Expense Summary""")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    int(input("Enter your choice: \n"))



display_menu()
def main():
    """

    :return:
    """
    print("==============================================================")
    print(project_name)
    display_menu()
    add_expenses()
    # view_expenses()
    # update_expenses()
    # expense_summary()
    # delete_expenses()


def add_expenses():
    """

    :return: float
    """
    expense_description = {}
    user_input = input("Enter expense description")
    amount_spent = input("Enter amount: ")
    expense_description[user_input] = expense_description.update(amount_spent)
    return expense_description

add_expenses()

def delete_expenses():
    """

    :return:
    """

delete_expenses()

def view_expenses():
    """


    :return:
    """

view_expenses()

def expense_summary():
    """

    :return:
    """

def update_expenses():
    """

    :return:
    """

update_expenses()

if __name__ == "__main__":
    main()

