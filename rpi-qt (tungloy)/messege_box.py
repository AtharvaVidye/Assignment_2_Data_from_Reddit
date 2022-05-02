
from PyQt5.QtWidgets import QMessageBox

def wrong_password_message():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Question)
    msg.setText("Please Validate Your Credentials")
    msg.setWindowTitle("Wrong Password")
    retval = msg.exec_()  

