import sys
import re
import bcrypt
import psycopg2
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
                               QLabel, QLineEdit, QStackedWidget, QFormLayout, QComboBox, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from datetime import datetime

# Database connection
conn = psycopg2.connect(
    dbname="expenses_db",
    user="postgres",
    password="admin123",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

cursor = conn.cursor()

class LoginWindow(QWidget):
    def __init__(self, app, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.app = app
        self.setWindowTitle("Login")

        layout = QVBoxLayout()

        self.user_name = QLineEdit()
        self.user_name.setPlaceholderText("Username")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.login_btn = QPushButton("Login")
        self.signup_btn = QPushButton("Sign Up")

        self.login_btn.clicked.connect(self.login)
        self.signup_btn.clicked.connect(self.signup)

        layout.addWidget(QLabel("Login"))
        layout.addWidget(self.user_name)
        layout.addWidget(self.password)
        layout.addWidget(self.login_btn)
        layout.addWidget(self.signup_btn)

        self.setLayout(layout)

    def login(self):
        username = self.user_name.text()
        password = self.password.text()
        # Authentication logic
        cursor.execute("SELECT password FROM users WHERE user_name=%s", (user_name,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
            cursor.execute("SELECT id FROM users WHERE user_name=%s", (user_name,))
            user_id = cursor.fetchone()[0]
            self.app.show_main_window(user_id)
        else:
            QMessageBox.warning(self, "Error", "Invalid credentials")

    def signup(self):
        user_name = self.user_name.text()
        password = self.password.text()
        # Registration logic
        if not self.validate_password(password):
            QMessageBox.warning(self, "Error",
                                "Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            return

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        try:
            cursor.execute("INSERT INTO users (user_name, password) VALUES (%s, %s)", (user_name, hashed_password))
            conn.commit()
            QMessageBox.information(self, "Success", "User registered successfully")
        except psycopg2.errors.UniqueViolation:
            conn.rollback()
            QMessageBox.warning(self, "Error", "Username already exists")

    def validate_password(self, password):
        # Password must be at least 8 characters long
        if len(password) < 8:
            return False
        # Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

class MainWindow(QMainWindow):
    def __init__(self, user_id, parent=None):
        super(MainWindow, self).__init__(parent)
        self.user_id = user_id
        self.setWindowTitle("Expense Tracker")

        # Main layout
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)

        # Navigation pane
        nav_pane = QVBoxLayout()
        nav_pane.setAlignment(Qt.AlignTop)

        logo_label = QLabel("Expense Tracker")
        search_bar = QLineEdit()
        search_bar.setPlaceholderText("Search...")

        nav_pane.addWidget(logo_label)
        nav_pane.addWidget(search_bar)

        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Add Expense", self.show_add_expense),
            ("View Expense", self.show_view_expense),
            ("Delete Expense", self.show_delete_expense),
            ("View Expense Summary", self.show_view_summary),
            ("Settings", self.show_settings),
            ("Profile", self.show_profile),
            ("Help", self.show_help)
        ]

        for (text, slot) in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(slot)
            nav_pane.addWidget(btn)

        # Content area
        self.content_area = QStackedWidget()

        # Initial views
        self.dashboard_view = QWidget()
        self.add_expense_view = QWidget()
        self.view_expense_view = QWidget()
        self.delete_expense_view = QWidget()
        self.summary_view = QWidget()
        self.settings_view = QWidget()
        self.profile_view = QWidget()
        self.help_view = QWidget()

        self.content_area.addWidget(self.dashboard_view)
        self.content_area.addWidget(self.add_expense_view)
        self.content_area.addWidget(self.view_expense_view)
        self.content_area.addWidget(self.delete_expense_view)
        self.content_area.addWidget(self.summary_view)
        self.content_area.addWidget(self.settings_view)
        self.content_area.addWidget(self.profile_view)
        self.content_area.addWidget(self.help_view)

        main_layout.addLayout(nav_pane)
        main_layout.addWidget(self.content_area)

        self.setCentralWidget(main_widget)

        # Initialize dashboard view
        self.init_dashboard()

    def init_dashboard(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Dashboard"))
        self.dashboard_view.setLayout(layout)

    def show_dashboard(self):
        self.content_area.setCurrentWidget(self.dashboard_view)

    def show_add_expense(self):
        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.amount_input = QLineEdit()
        self.category_input = QLineEdit()
        self.description_input = QLineEdit()

        form_layout.addRow("Amount:", self.amount_input)
        form_layout.addRow("Category:", self.category_input)
        form_layout.addRow("Description:", self.description_input)

        submit_btn = QPushButton("Add Expense")
        submit_btn.clicked.connect(self.add_expense)

        layout.addLayout(form_layout)
        layout.addWidget(submit_btn)
        self.add_expense_view.setLayout(layout)

        self.content_area.setCurrentWidget(self.add_expense_view)

    def add_expense(self):
        amount = self.amount_input.text()
        category = self.category_input.text()
        description = self.description_input.text()

        cursor.execute("INSERT INTO expenses (user_id, amount, category, description) VALUES (%s, %s, %s, %s)",
                       (self.user_id, amount, category, description))
        conn.commit()
        QMessageBox.information(self, "Success", "Expense added successfully")

    def show_view_expense(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("View Expense"))
        self.view_expense_view.setLayout(layout)
        self.content_area.setCurrentWidget(self.view_expense_view)

    def show_delete_expense(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Delete Expense"))
        self.delete_expense_view.setLayout(layout)
        self.content_area.setCurrentWidget(self.delete_expense_view)

    def show_view_summary(self):
        layout = QVBoxLayout()

        view_type = QComboBox()
        view_type.addItems(["Table", "Pie Chart", "Line Chart"])

        view_type.currentIndexChanged.connect(self.update_summary_view)
        layout.addWidget(view_type)

        self.summary_view.setLayout(layout)
        self.content_area.setCurrentWidget(self.summary_view)

    def update_summary_view(self, index):
        if index == 0:
            # Table view
            pass
        elif index == 1:
            # Pie chart view
            fig, ax = plt.subplots()
            categories = ['Food', 'Travel', 'Shopping', 'Other']
            expenses = [300, 150, 100, 50]

            ax.pie(expenses, labels=categories, autopct='%1.1f%%')
            ax.axis('equal')

            chart = FigureCanvas(fig)
            self.summary_view.layout().addWidget(chart)
        elif index == 2:
            # Line chart view
            pass

    def show_settings(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Settings"))
        self.settings_view.setLayout(layout)
        self.content_area.setCurrentWidget(self.settings_view)

    def show_profile(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Profile"))
        self.profile_view.setLayout(layout)
        self.content_area.setCurrentWidget(self.profile_view)

    def show_help(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Help"))
        self.help_view.setLayout(layout)
        self.content_area.setCurrentWidget(self.help_view)

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_view = QMainWindow()

        self.login_view = LoginWindow(self)
        self.login_view.show()

    def show_main_window(self, user_id):
        self.main_view = MainWindow(user_id)
        self.login_view.close()
        self.main_view.show()

if __name__ == "__main__":
    app = App(sys.argv)
    app.exec()
    sys.exit
