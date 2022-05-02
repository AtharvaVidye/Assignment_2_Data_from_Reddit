# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 0, 1024, 600))
        self.tabWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 40px;font: 75 8pt \"Arial\";}\n"
"\n"
"\n"
"\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 151, 41))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/favicon.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_18 = QtWidgets.QLabel(self.tab)
        self.label_18.setGeometry(QtCore.QRect(260, 237, 141, 31))
        self.label_18.setStyleSheet("font: 20pt \"Arial\";")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(470, 230, 221, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_13 = QtWidgets.QPushButton(self.tab)
        self.pushButton_13.setGeometry(QtCore.QRect(410, 322, 141, 31))
        self.pushButton_13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"padding:8px;\n"
"min-width:10px;\n"
"")
        self.pushButton_13.setObjectName("pushButton_13")
        self.label_28 = QtWidgets.QLabel(self.tab)
        self.label_28.setGeometry(QtCore.QRect(440, 330, 16, 16))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap(":/newPrefix/images/login_.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.label_56 = QtWidgets.QLabel(self.tab)
        self.label_56.setGeometry(QtCore.QRect(310, 110, 371, 81))
        self.label_56.setText("")
        self.label_56.setPixmap(QtGui.QPixmap(":/newPrefix/images/grmaton.jpg"))
        self.label_56.setScaledContents(True)
        self.label_56.setObjectName("label_56")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.label_21.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_24 = QtWidgets.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 151, 41))
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(":/newPrefix/favicon.jpeg"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_3)
        self.dateEdit.setGeometry(QtCore.QRect(330, 70, 321, 81))
        self.dateEdit.setStyleSheet("border : 2px solid black;\n"
"background-color : white;\n"
"padding : 5px;")
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab_3)
        self.dateEdit_2.setGeometry(QtCore.QRect(330, 200, 321, 91))
        self.dateEdit_2.setStyleSheet("border : 2px solid black;\n"
"background-color : white;\n"
"padding : 5px;")
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label_30 = QtWidgets.QLabel(self.tab_3)
        self.label_30.setGeometry(QtCore.QRect(410, 320, 121, 21))
        self.label_30.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 14pt \"Ubuntu Mono\";")
        self.label_30.setObjectName("label_30")
        self.pushButton_16 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_16.setGeometry(QtCore.QRect(1166, 15, 91, 31))
        self.pushButton_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"padding:8px;\n"
"min-width:10px;\n"
"")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_14.setGeometry(QtCore.QRect(670, 440, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Ubuntu Mono\";\n"
"border-radius : 6px")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 271, 61))
        self.label_23.setAutoFillBackground(False)
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap(":/newPrefix/images/grmaton.jpg"))
        self.label_23.setScaledContents(True)
        self.label_23.setObjectName("label_23")
        self.label_46 = QtWidgets.QLabel(self.tab_3)
        self.label_46.setGeometry(QtCore.QRect(1170, 20, 21, 21))
        self.label_46.setText("")
        self.label_46.setPixmap(QtGui.QPixmap(":/newPrefix/images/logout.jpeg"))
        self.label_46.setScaledContents(True)
        self.label_46.setObjectName("label_46")
        self.radioButton = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton.setGeometry(QtCore.QRect(450, 360, 112, 23))
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab_3)
        self.radioButton_2.setGeometry(QtCore.QRect(450, 400, 112, 23))
        self.radioButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_2.setObjectName("radioButton_2")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setStyleSheet("")
        self.tab_4.setObjectName("tab_4")
        self.label_20 = QtWidgets.QLabel(self.tab_4)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_19 = QtWidgets.QLabel(self.tab_4)
        self.label_19.setGeometry(QtCore.QRect(30, 85, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";")
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.tab_4)
        self.label_22.setGeometry(QtCore.QRect(550, 80, 91, 21))
        self.label_22.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";")
        self.label_22.setObjectName("label_22")
        self.label_25 = QtWidgets.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(30, 210, 91, 21))
        self.label_25.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(560, 210, 91, 21))
        self.label_26.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";")
        self.label_26.setObjectName("label_26")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 115, 441, 41))
        self.lineEdit_2.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 160, 441, 41))
        self.lineEdit_3.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 240, 441, 41))
        self.lineEdit_5.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 290, 441, 41))
        self.lineEdit_6.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(540, 110, 441, 41))
        self.lineEdit_7.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(540, 160, 441, 41))
        self.lineEdit_8.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(540, 240, 441, 41))
        self.lineEdit_9.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(540, 290, 441, 41))
        self.lineEdit_10.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(370, 122, 76, 27))
        self.pushButton.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 167, 76, 27))
        self.pushButton_2.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 247, 76, 27))
        self.pushButton_3.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 296, 76, 27))
        self.pushButton_6.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(885, 116, 76, 27))
        self.pushButton_7.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QtCore.QRect(885, 167, 76, 27))
        self.pushButton_8.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(885, 246, 76, 27))
        self.pushButton_9.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(885, 297, 76, 27))
        self.pushButton_10.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_11.setGeometry(QtCore.QRect(230, 360, 561, 31))
        self.pushButton_11.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"font: 75 11pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QtCore.QRect(909, 363, 71, 31))
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 11pt \"Ubuntu Mono\";\n"
"border-radius:6px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_27 = QtWidgets.QLabel(self.tab_4)
        self.label_27.setGeometry(QtCore.QRect(450, 368, 16, 16))
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap(":/newPrefix/tick.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.pushButton_17 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_17.setGeometry(QtCore.QRect(1166, 15, 91, 31))
        self.pushButton_17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"padding:8px;\n"
"min-width:10px;\n"
"")
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_37 = QtWidgets.QLabel(self.tab_4)
        self.label_37.setGeometry(QtCore.QRect(20, 414, 441, 41))
        self.label_37.setStyleSheet("border: 1px solid rgb(157, 157, 157);")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.tab_4)
        self.label_38.setGeometry(QtCore.QRect(20, 467, 441, 41))
        self.label_38.setStyleSheet("border: 1px solid rgb(157, 157, 157);")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.tab_4)
        self.label_39.setGeometry(QtCore.QRect(540, 414, 441, 41))
        self.label_39.setStyleSheet("border: 1px solid rgb(157, 157, 157);")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.tab_4)
        self.label_40.setGeometry(QtCore.QRect(540, 467, 441, 41))
        self.label_40.setStyleSheet("border: 1px solid rgb(157, 157, 157);")
        self.label_40.setObjectName("label_40")
        self.label_44 = QtWidgets.QLabel(self.tab_4)
        self.label_44.setGeometry(QtCore.QRect(0, 0, 271, 61))
        self.label_44.setAutoFillBackground(False)
        self.label_44.setText("")
        self.label_44.setPixmap(QtGui.QPixmap(":/newPrefix/images/grmaton.jpg"))
        self.label_44.setScaledContents(True)
        self.label_44.setObjectName("label_44")
        self.label_45 = QtWidgets.QLabel(self.tab_4)
        self.label_45.setGeometry(QtCore.QRect(1170, 20, 21, 21))
        self.label_45.setText("")
        self.label_45.setPixmap(QtGui.QPixmap(":/newPrefix/images/logout.jpeg"))
        self.label_45.setScaledContents(True)
        self.label_45.setObjectName("label_45")
        self.label_48 = QtWidgets.QLabel(self.tab_4)
        self.label_48.setGeometry(QtCore.QRect(920, 370, 21, 20))
        self.label_48.setText("")
        self.label_48.setPixmap(QtGui.QPixmap(":/newPrefix/images/ok_.png"))
        self.label_48.setScaledContents(True)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.tab_4)
        self.label_49.setGeometry(QtCore.QRect(450, 365, 21, 20))
        self.label_49.setText("")
        self.label_49.setPixmap(QtGui.QPixmap(":/newPrefix/images/calibrate.png"))
        self.label_49.setScaledContents(True)
        self.label_49.setObjectName("label_49")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_29 = QtWidgets.QLabel(self.tab_5)
        self.label_29.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.label_29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_19.setGeometry(QtCore.QRect(1166, 15, 91, 31))
        self.pushButton_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"padding:8px;\n"
"min-width:10px;\n"
"")
        self.pushButton_19.setObjectName("pushButton_19")
        self.comboBox = QtWidgets.QComboBox(self.tab_5)
        self.comboBox.setGeometry(QtCore.QRect(540, 260, 441, 41))
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setStyleSheet("color: rgb(149, 149, 149);\n"
"font: 75 11pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_35 = QtWidgets.QLabel(self.tab_5)
        self.label_35.setGeometry(QtCore.QRect(540, 240, 91, 21))
        self.label_35.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_35.setObjectName("label_35")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_14.setGeometry(QtCore.QRect(540, 350, 441, 41))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(50, 82, 441, 41))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_36 = QtWidgets.QLabel(self.tab_5)
        self.label_36.setGeometry(QtCore.QRect(850, 364, 16, 16))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap(":/newPrefix/submit.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(50, 350, 441, 41))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 170, 441, 41))
        self.comboBox_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_2.setStyleSheet("color: rgb(149, 149, 149);\n"
"font: 75 11pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_41 = QtWidgets.QLabel(self.tab_5)
        self.label_41.setGeometry(QtCore.QRect(50, 150, 91, 21))
        self.label_41.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.tab_5)
        self.label_42.setGeometry(QtCore.QRect(50, 240, 131, 21))
        self.label_42.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_42.setObjectName("label_42")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(540, 82, 441, 41))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.label_43 = QtWidgets.QLabel(self.tab_5)
        self.label_43.setGeometry(QtCore.QRect(40, 10, 271, 61))
        self.label_43.setAutoFillBackground(False)
        self.label_43.setText("")
        self.label_43.setPixmap(QtGui.QPixmap(":/newPrefix/images/grmaton.jpg"))
        self.label_43.setScaledContents(True)
        self.label_43.setObjectName("label_43")
        self.label_34 = QtWidgets.QLabel(self.tab_5)
        self.label_34.setGeometry(QtCore.QRect(1170, 20, 21, 21))
        self.label_34.setText("")
        self.label_34.setPixmap(QtGui.QPixmap(":/newPrefix/images/logout.jpeg"))
        self.label_34.setScaledContents(True)
        self.label_34.setObjectName("label_34")
        self.label_31 = QtWidgets.QLabel(self.tab_5)
        self.label_31.setGeometry(QtCore.QRect(1089, 457, 31, 31))
        self.label_31.setText("")
        self.label_31.setPixmap(QtGui.QPixmap(":/newPrefix/images/submit_.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setObjectName("label_31")
        self.pushButton_15 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_15.setGeometry(QtCore.QRect(810, 440, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Ubuntu Mono\";\n"
"border-radius : 6px")
        self.pushButton_15.setObjectName("pushButton_15")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_3.setGeometry(QtCore.QRect(50, 260, 441, 41))
        self.comboBox_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_3.setStyleSheet("color: rgb(149, 149, 149);\n"
"font: 75 11pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(540, 170, 441, 41))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_29.raise_()
        self.pushButton_19.raise_()
        self.comboBox.raise_()
        self.label_35.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_15.raise_()
        self.label_36.raise_()
        self.lineEdit_16.raise_()
        self.comboBox_2.raise_()
        self.label_41.raise_()
        self.label_42.raise_()
        self.lineEdit_17.raise_()
        self.label_43.raise_()
        self.label_34.raise_()
        self.pushButton_15.raise_()
        self.label_31.raise_()
        self.comboBox_3.raise_()
        self.lineEdit_18.raise_()
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 271, 61))
        self.label_4.setAutoFillBackground(False)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/newPrefix/images/grmaton.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(50, 80, 201, 131))
        self.label_10.setStyleSheet("font: 75 35pt \"Waree\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(510, 80, 201, 131))
        self.label_11.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 75 35pt \"Waree\";\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setGeometry(QtCore.QRect(280, 80, 201, 131))
        self.label_12.setStyleSheet("font: 75 35pt \"Waree\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(50, 300, 201, 131))
        self.label_13.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 75 35pt \"Waree\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setGeometry(QtCore.QRect(280, 300, 201, 131))
        self.label_14.setStyleSheet("\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 75 35pt \"Waree\";")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 18pt \"Ubuntu Mono\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(270, 210, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 75 18pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(510, 210, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 75 18pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(60, 430, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 75 18pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(270, 430, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 75 18pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(730, 430, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(0, 213, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Ubuntu Mono\";\n"
"border-radius : 6px")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(780, 436, 31, 31))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap(":/newPrefix/images/submit_.png"))
        self.label_16.setScaledContents(True)
        self.label_16.setObjectName("label_16")
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_18.setGeometry(QtCore.QRect(866, 15, 91, 31))
        self.pushButton_18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 87 8pt \"Arial Black\";\n"
"color: rgb(0, 0, 0);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-radius:10px;\n"
"border-color:black;\n"
"padding:8px;\n"
"min-width:10px;\n"
"")
        self.pushButton_18.setObjectName("pushButton_18")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(870, 20, 21, 21))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(":/newPrefix/images/logout.jpeg"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(510, 300, 201, 131))
        self.label_15.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 75 35pt \"Waree\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(510, 430, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 18pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(730, 350, 241, 41))
        self.lineEdit_4.setStyleSheet("font: 75 20pt \"Ubuntu Condensed\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_32 = QtWidgets.QLabel(self.tab_2)
        self.label_32.setGeometry(QtCore.QRect(1070, 390, 31, 31))
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap(":/newPrefix/images/cam.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.label_50 = QtWidgets.QLabel(self.tab_2)
        self.label_50.setGeometry(QtCore.QRect(120, 170, 67, 31))
        self.label_50.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 85 26pt \"Ubuntu Condensed\";")
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.tab_2)
        self.label_51.setGeometry(QtCore.QRect(347, 170, 67, 31))
        self.label_51.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 75 26pt \"Ubuntu Condensed\";")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.tab_2)
        self.label_52.setGeometry(QtCore.QRect(580, 170, 67, 31))
        self.label_52.setStyleSheet("font: 75 26pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.tab_2)
        self.label_53.setGeometry(QtCore.QRect(120, 390, 67, 31))
        self.label_53.setStyleSheet("font: 75 26pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.tab_2)
        self.label_54.setGeometry(QtCore.QRect(350, 390, 67, 31))
        self.label_54.setStyleSheet("font: 75 26pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.tab_2)
        self.label_55.setGeometry(QtCore.QRect(580, 390, 67, 31))
        self.label_55.setStyleSheet("font: 75 26pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.label_57 = QtWidgets.QLabel(self.tab_2)
        self.label_57.setGeometry(QtCore.QRect(730, 80, 231, 211))
        self.label_57.setText("")
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(self.tab_2)
        self.label_58.setGeometry(QtCore.QRect(270, 0, 571, 71))
        self.label_58.setStyleSheet("color: rgb(164, 0, 0);\n"
"font: 75 43pt \"Ubuntu Condensed\";")
        self.label_58.setObjectName("label_58")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_18.setText(_translate("MainWindow", "Password"))
        self.pushButton_13.setText(_translate("MainWindow", "   LOGIN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "                  LOGIN                "))
        self.label_30.setText(_translate("MainWindow", "Export Type"))
        self.pushButton_16.setText(_translate("MainWindow", "    LOGOUT"))
        self.pushButton_14.setText(_translate("MainWindow", "EXPORT DATA"))
        self.radioButton.setText(_translate("MainWindow", "XLSX"))
        self.radioButton_2.setText(_translate("MainWindow", "CSV"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "           EXPORT DATA         "))
        self.label_19.setText(_translate("MainWindow", "Length"))
        self.label_22.setText(_translate("MainWindow", "Width"))
        self.label_25.setText(_translate("MainWindow", "Height"))
        self.label_26.setText(_translate("MainWindow", "Weight"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "    Length"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "    Length"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "    Height"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "    Height"))
        self.lineEdit_7.setPlaceholderText(_translate("MainWindow", "    Width"))
        self.lineEdit_8.setPlaceholderText(_translate("MainWindow", "    Width"))
        self.lineEdit_9.setPlaceholderText(_translate("MainWindow", "    Weight"))
        self.lineEdit_10.setPlaceholderText(_translate("MainWindow", "    Weight"))
        self.pushButton.setText(_translate("MainWindow", "SET ZERO"))
        self.pushButton_2.setText(_translate("MainWindow", "SET SPAN"))
        self.pushButton_3.setText(_translate("MainWindow", "SET ZERO"))
        self.pushButton_6.setText(_translate("MainWindow", "SET SPAN"))
        self.pushButton_7.setText(_translate("MainWindow", "SET ZERO"))
        self.pushButton_8.setText(_translate("MainWindow", "SET SPAN"))
        self.pushButton_9.setText(_translate("MainWindow", "SET ZERO"))
        self.pushButton_10.setText(_translate("MainWindow", "SET SPAN"))
        self.pushButton_11.setText(_translate("MainWindow", "CALIBRATE"))
        self.pushButton_12.setText(_translate("MainWindow", "   OK"))
        self.pushButton_17.setText(_translate("MainWindow", "    LOGOUT"))
        self.label_37.setText(_translate("MainWindow", "  Length"))
        self.label_38.setText(_translate("MainWindow", "  Height"))
        self.label_39.setText(_translate("MainWindow", "  Width"))
        self.label_40.setText(_translate("MainWindow", "  Weight"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "     SENSOR CALIBRATION    "))
        self.pushButton_19.setText(_translate("MainWindow", "    LOGOUT"))
        self.comboBox.setItemText(0, _translate("MainWindow", "kg"))
        self.comboBox.setItemText(1, _translate("MainWindow", "gm"))
        self.comboBox.setItemText(2, _translate("MainWindow", "lb"))
        self.label_35.setText(_translate("MainWindow", "Weight Unit"))
        self.lineEdit_14.setPlaceholderText(_translate("MainWindow", "  Weight Resolution (in grams)"))
        self.lineEdit_15.setPlaceholderText(_translate("MainWindow", "  Terminal ID"))
        self.lineEdit_16.setPlaceholderText(_translate("MainWindow", "  Weight Capacity (in kg)"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "m"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "cm"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "inch"))
        self.label_41.setText(_translate("MainWindow", "Distance unit"))
        self.label_42.setText(_translate("MainWindow", "Distance resolution"))
        self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "  Volume Factor (Surface)"))
        self.pushButton_15.setText(_translate("MainWindow", "SUBMIT"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "0.1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "0.5"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "1"))
        self.lineEdit_18.setPlaceholderText(_translate("MainWindow", "  Volume Factor (Air)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "   DEVICE CONFIGURATION   "))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "Length"))
        self.label_17.setText(_translate("MainWindow", "Width"))
        self.label_6.setText(_translate("MainWindow", "Height"))
        self.label_7.setText(_translate("MainWindow", "Weight"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Cubical Weight </p><p align=\"center\">(Surface)</p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "SUBMIT"))
        self.pushButton_18.setText(_translate("MainWindow", "    LOGOUT"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Chargeable Weight"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "   Barcode"))
        self.label_50.setText(_translate("MainWindow", "Unit"))
        self.label_51.setText(_translate("MainWindow", "Unit"))
        self.label_52.setText(_translate("MainWindow", "Unit"))
        self.label_53.setText(_translate("MainWindow", "Unit"))
        self.label_54.setText(_translate("MainWindow", "Unit"))
        self.label_55.setText(_translate("MainWindow", "Unit"))
        self.label_58.setText(_translate("MainWindow", "Already Scanned !!"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "           DATA CAPTURE         "))
import img_rc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
