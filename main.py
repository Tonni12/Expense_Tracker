from PySide6.QtWidgets import QApplication
from login_page import LoginWindow
import sys

def user_login(data):
    print("Login successful: ", data)

app = QApplication(sys.argv)
window = LoginWindow()

window.show()
app.exec()
