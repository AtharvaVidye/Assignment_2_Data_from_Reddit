from PyQt5 import QtCore, QtGui, QtWidgets
import messege_box
from apscheduler.schedulers.qt import QtScheduler
import serial
import sqlite3,csv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from number_pad import numberPopup
import os
from glob import glob
from subprocess import check_output, CalledProcessError
from openpyxl import Workbook
import openpyxl
from time import sleep
import sys
from PyQt5.QtGui import *
import cv2
import subprocess
import datetime

class cQLineEdit(QLineEdit):
    clicked= pyqtSignal()
    def __init__(self,widget):
        super().__init__(widget)
    def mousePressEvent(self,QMouseEvent):
        self.clicked.emit()

class Ui_MainWindow(QWidget):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS date_and_time(id INTEGER primary key AUTOINCREMENT, Date Text)')
        c.execute("INSERT INTO date_and_time(Date) values ('YYYY-MM-DD  HH%MM%SS')")
        c.execute('CREATE TABLE IF NOT EXISTS Data_Capture(id INTEGER primary key AUTOINCREMENT, Length INTEGER ,Width INTEGER , Height INTEGER , Weight INTEGER , Cubical_Weight_Surface INTEGER , Cubical_Weight_Air INTEGER , Date TEXT , Barcode TEXT , Path Text)')
        c.execute("INSERT INTO Data_Capture(Length,Width,Height,Weight,Cubical_Weight_Surface,Cubical_Weight_Air,Date,Barcode,path) values (?,?,?,?,?,?,?,?,?)",(0,0,0,0,0,0,'None','None','None'))
        conn.commit()
        c.close()
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)

    def ImageUpdateSlot(self, Image):
        self.FeedLabel.setPixmap(QPixmap.fromImage(Image))

    def non_zero(self,a,b,c):
        if a!=0 and b!=0 and c!=0:
            return 1
        elif a!=0 and b!=0 and c==0:
            return 0
        elif a!=0 and b==0 and c!=0:
            return 0
        elif a==0 and b!=0 and c!=0:
            return 0   
        elif a==0 and b==0 and c!=0:
            return 0
        elif a!=0 and b==0 and c==0:
            return 0  
        elif a==0 and b!=0 and c==0:
            return 0
        else:
            return 1
        
    def round_nearest(self, x, a):
        return round(x / a) * a

    def Numpad_setspan_1(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_3, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def Numpad_setspan_2(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_8, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def Numpad_setspan_3(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_6, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def Numpad_setspan_4(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_10, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def onClick(self,e):
        MainWindow.setEnabled(True)
    
    def callBackOnSubmit(self, arg1, arg2): 
        print("Function is called with args: %s & %s" % (arg1, arg2))

    def Numpad_login(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def Numpad_Terminal_ID(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_15, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def Numpad_Volume_Factor(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_17, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def Numpad_Volume_Factor_Air(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_18, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show()

    def Numpad_Weight_Resolution(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_14, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def Numpad_Weight_Capacity(self):
        MainWindow.setEnabled(False)
        self.exPopup = numberPopup(MainWindow,self.lineEdit_16, "", self.callBackOnSubmit, "Argument 1", "Argument 2")
        self.exPopup.setGeometry(70,180,400, 300)
        self.exPopup.show() 

    def login(self):
        pwd = self.lineEdit.text()   
        password = str(1234)
        if pwd == password:
            self.tabWidget.removeTab(0)
            self.tabWidget.addTab(self.tab_3 , "         EXPORT DATA       ")
            self.tabWidget.addTab(self.tab_4, "     SENSOR CALIBRATION    ")  
            self.tabWidget.addTab(self.tab_5, "   DEVICE CONFIGURATION   ")
            self.tabWidget.addTab(self.tab_2, "       DATA CAPTURE     ")
            self.pushButton_18.setHidden(False)
            self.label_33.setHidden(False) 
            self.pushButton_16.setHidden(False) 
            self.label_46.setHidden(False) 
            self.tabWidget.setCurrentIndex(3)
            self.lineEdit.setText("") 
        else:
            messege_box.wrong_password_message()
            self.lineEdit.setText("") 
    
    def logout(self):
        self.tabWidget.removeTab(3)
        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1) 
        self.tabWidget.removeTab(0)
        self.tabWidget.addTab(self.tab , "               LOGIN             ")   
        self.tabWidget.addTab(self.tab_2, "       DATA CAPTURE     ")
        self.pushButton_18.setHidden(True)
        self.label_33.setHidden(True) 
        self.pushButton_16.setHidden(True)
        self.label_46.setHidden(True) 
        self.tabWidget.setCurrentIndex(2)
        self.label_37.setText("")
        self.label_38.setText("")
        self.label_39.setText("")
        self.label_40.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_14.setText("")
        self.lineEdit_15.setText("")

    def serial_data(self):
        try:
            ser = serial.Serial ("/dev/serial0", 9600)
            received_data = ser.read()
            sleep(0.08)
            data_left = ser.inWaiting()             
            received_data += ser.read(data_left)
            self.a = received_data.decode('utf-8').split(',')
            try:
                if len(self.a) == 6:
                    conn = sqlite3.connect('database.db')
                    conn.text_factory = str 
                    cur = conn.cursor()

                    query_1 = "SELECT * FROM Coefficient ORDER BY id DESC LIMIT 1"
                    cur.execute(query_1)
                    rows = cur.fetchall()
                    if not rows:
                        return None
                    for row in rows:
                        coefficient_1 = row[1]
                        coefficient_2 = row[2]
                        coefficient_3 = row[3]
                        coefficient_4 = row[4]
                        len_sz = row[5]
                        wdt_sz = row[6]
                        ht_sz = row[7]
                        wt_sz = row[8]

                    query_2 = "SELECT * FROM Device_Configure ORDER BY id DESC LIMIT 1"
                    cur.execute(query_2)
                    rows = cur.fetchall()
                    if not rows:
                        return None
                    for row in rows:
                        Terminal_ID = row[1]
                        Volume_Factor_Surface = row[2]
                        Volume_Factor_Air = row[3]
                        Distance_Unit = row[4]
                        Weight_Unit = row[5]
                        Distance_Resolution = row[6]
                        Weight_Resolution = row[7] + 10
                        Weight_Capacity = row[8]
                    conn.commit()
                    conn.close() 
                    
                    if Distance_Unit == 'cm':    
                        b1 = self.round_nearest(((float(self.a[1]) - float(len_sz))/coefficient_1)/10,Distance_Resolution)
                        b2 = self.round_nearest(((float(self.a[2]) - float(wdt_sz))/coefficient_2)/10,Distance_Resolution)
                        b3 = self.round_nearest(((float(self.a[3]) - float(ht_sz))/coefficient_3)/10,Distance_Resolution)
                        self.label_50.setText(Distance_Unit)
                        self.label_51.setText(Distance_Unit)
                        self.label_52.setText(Distance_Unit)
                    elif Distance_Unit == 'inch':
                        b1 = self.round_nearest(((float(self.a[1]) - float(len_sz))/coefficient_1)/25.4,Distance_Resolution)
                        b2 = self.round_nearest(((float(self.a[2]) - float(wdt_sz))/coefficient_2)/25.4,Distance_Resolution)
                        b3 = self.round_nearest(((float(self.a[3]) - float(ht_sz))/coefficient_3)/25.4,Distance_Resolution)
                        self.label_50.setText(Distance_Unit)
                        self.label_51.setText(Distance_Unit)
                        self.label_52.setText(Distance_Unit)
                    else:
                        b1 = self.round_nearest((float(self.a[1]) - float(len_sz))/coefficient_1,Distance_Resolution)
                        b2 = self.round_nearest((float(self.a[2]) - float(wdt_sz))/coefficient_2,Distance_Resolution)
                        b3 = self.round_nearest((float(self.a[3]) - float(ht_sz))/coefficient_3,Distance_Resolution)
                        self.label_50.setText(Distance_Unit)
                        self.label_51.setText(Distance_Unit)
                        self.label_52.setText(Distance_Unit)

                    cub_wt = ((b1*b2*b3)/Volume_Factor_Surface)/1000
                    cub_wt_air = ((b1*b2*b3)/Volume_Factor_Air)/1000
                    if Weight_Unit == 'gm':
                        Weight_Capacity *= 1000
                        b4 = self.round_nearest((((float(self.a[4]) - float(wt_sz))/coefficient_4)*1000),Weight_Resolution)
                        self.label_53.setText(Weight_Unit)
                    elif Weight_Unit == 'lb':
                        Weight_Capacity *= 1000
                        gram = self.round_nearest((((float(self.a[4]) - float(wt_sz))/coefficient_4)*1000),Weight_Resolution)
                        b4 = gram/454
                        self.label_53.setText(Weight_Unit)
                    else:
                        Weight_Capacity *= 1
                        gram = self.round_nearest((((float(self.a[4]) - float(wt_sz))/coefficient_4)*1000),Weight_Resolution)
                        b4 = gram/1000
                        self.label_53.setText(Weight_Unit)
                    
                    
                    if Distance_Unit == 'cm':
                        self.label_10.setText("{:.3f}".format(b1))
                        self.label_12.setText("{:.3f}".format(b2)) 
                        self.label_11.setText("{:.3f}".format(b3)) 
                    elif Distance_Unit == 'inch':
                        self.label_10.setText("{:.3f}".format(b1))
                        self.label_12.setText("{:.3f}".format(b2)) 
                        self.label_11.setText("{:.3f}".format(b3))
                    else:
                        self.label_10.setText(str(int(b1)))
                        self.label_12.setText(str(int(b2))) 
                        self.label_11.setText(str(int(b3))) 
                    if b4 < float(0.180):
                        self.label_13.setText("0.000")
                    elif b4 < Weight_Capacity:    
                        self.label_13.setText("{:.3f}".format(b4))
                    else:
                        self.label_13.setText("OL")  
                        self.label_15.setText("OL") 

                    self.label_14.setText("{:.3f}".format(cub_wt))
                    self.label_15.setText("{:.3f}".format(cub_wt_air))
                        
                    self.label_54.setText("kg\u00b3")
                    self.label_55.setText("kg\u00b3")

            except sqlite3.OperationalError:
                self.label_10.setText("0.000")
                self.label_12.setText("0.000") 
                self.label_11.setText("0.000")                             
                self.label_13.setText("0.000")
                self.label_14.setText("0.000")
                self.label_15.setText("0.000") 

        except serial.serialutil.SerialException:
            print("Failed to open serial port")

    def barcode(self):
        try:
            while True:
                if self.non_zero(float(self.label_10.text()),float(self.label_12.text()),float(self.label_11.text())):
                    barcode_serial = serial.Serial ('/dev/ttyACM0', 9600)
                    barcode_data = barcode_serial.read()
                    sleep(0.08)
                    barcode_data_left = barcode_serial.inWaiting()             
                    barcode_data += barcode_serial.read(barcode_data_left)
                    line = barcode_data.decode('utf-8')

                    self.lineEdit_4.setText(line)
                    conn = sqlite3.connect('database.db')
                    conn.text_factory = str 
                    cur = conn.cursor()
                    query_1 = "SELECT EXISTS(SELECT 1 FROM Data_Capture WHERE Barcode={})".format(self.lineEdit_4.text())
                    cur.execute(query_1)
                    rows = cur.fetchall()
                    for row in rows:
                        barcode_flag = row[0]
                    conn.commit()
                    cur.close()

                    if barcode_flag == 0:
                        self.save_date() 
                        conn = sqlite3.connect('database.db')
                        conn.text_factory = str 
                        cur = conn.cursor()
                        query_1 = "SELECT * FROM date_and_time where ID = 1"
                        cur.execute(query_1)
                        rows = cur.fetchall()
                        for row in rows:
                            path = row[1]
                            print(path)
                        conn.commit()
                        cur.close()
                        self.Worker1.capture_image(path)
                        barcode_path = path+'.jpg'
                        if line:
                            # self.label_58.setVisible(False)
                            self.lineEdit_4.setText(line)  
                            conn = sqlite3.connect('database.db')
                            c = conn.cursor()
                            c.execute('CREATE TABLE IF NOT EXISTS Data_Capture(id INTEGER primary key AUTOINCREMENT, Length INTEGER ,Width INTEGER , Height INTEGER , Weight INTEGER , Cubical_Weight_Surface INTEGER , Cubical_Weight_Air INTEGER , Date TEXT , Barcode TEXT , Path Text)')
                            c.execute("INSERT INTO Data_Capture(Length,Width,Height,Weight,Cubical_Weight_Surface,Cubical_Weight_Air,Date,Barcode,path) values (?,?,?,?,?,?,?,?,?)",(self.label_10.text(),self.label_12.text(),self.label_11.text(),self.label_13.text(),self.label_14.text(),self.label_15.text(),datetime.datetime.now().date(),self.lineEdit_4.text(),barcode_path))
                            query = f"UPDATE date_and_time SET Date = ? WHERE ID = ?"
                            c.execute(query, ("YYYY-MM-DD  HH%MM%SS", '1'))
                            conn.commit()
                            c.close()
                            
                            zpl ='^XA ^CF0,30 ^FO70,50^FD     Shipment ID : {}^FS ^FO70,100^FD     Date & Time : {}^FS ^CF0,30 ^FX Tabel. ^FO130,130^GB570,400,3^FS ^FO130,130^GB250,400,3^FS ^FO100,160^FD    Actual Weight^FS ^FO400,160^FD{} {}^FS ^FO100,260^FD    Dimension^FS ^FO400,260^FD{} x {} x {} ({})^FS ^FO100,360^FD    Vol.Weight(Surface)^FS ^FO400,360^FD{} kg3^FS ^FO100,460^FD    Vol.Weight(Air)^FS ^FO400,460^FD{} kg3^FS ^FO130,220^GB570,3,3^FS ^FO130,320^GB570,3,3^FS ^FO130,420^GB570,3,3^FS ^FO250,550^BQN,2,4^FD   Shipment ID : {} Date & Time : {} Actual Weight : {} {} Dimension : {}x{}x{} ({}) Vol.Weight (Surface) : {} Vol. Weight (Air) : {} ^FS ^XZ'.format(self.lineEdit_4.text(),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.label_13.text(),weight_unit,self.label_10.text(),self.label_12.text(),self.label_11.text(),distance_unit,self.label_14.text(),self.label_15.text(),self.lineEdit_4.text(),path,self.label_13.text(),weight_unit,self.label_10.text(),self.label_12.text(),self.label_11.text(),distance_unit,self.label_14.text(),self.label_15.text())
                            f = open("label.zpl", "w+")
                            f.write(zpl)
                            f.close()
                            subprocess.call(['lp', '-d', 'TSC_TE210', '-o', 'raw', 'label.zpl']) 

                            self.label_58.setVisible(False)
                            break
                    else:
                        self.label_58.setText("Already Scanned !!!")
                        self.label_58.setVisible(True)
                        self.save_date() 
                        conn = sqlite3.connect('database.db')
                        conn.text_factory = str 
                        cur = conn.cursor()
                        query_1 = "SELECT * FROM date_and_time where ID = 1"
                        cur.execute(query_1)
                        rows = cur.fetchall()
                        for row in rows:
                            path = row[1]
                            print(path)
                        conn.commit()
                        cur.close()
                        conn = sqlite3.connect('database.db')
                        conn.text_factory = str 
                        cur = conn.cursor()
                        query_2 = "SELECT * FROM Device_Configure ORDER BY id DESC LIMIT 1"
                        cur.execute(query_2)
                        rows = cur.fetchall()
                        for row in rows:
                            distance_unit = row[4]
                            weight_unit = row[5]
                        conn.commit()
                        conn.close()
                        self.Worker1.capture_image(path)
                        barcode_path = path+'.jpg'
                        if line:
                            # self.label_58.setVisible(False)
                            self.lineEdit_4.setText(line)  
                            conn = sqlite3.connect('database.db')
                            c = conn.cursor()
                            c.execute('CREATE TABLE IF NOT EXISTS Data_Capture(id INTEGER primary key AUTOINCREMENT, Length INTEGER ,Width INTEGER , Height INTEGER , Weight INTEGER , Cubical_Weight_Surface INTEGER , Cubical_Weight_Air INTEGER , Date TEXT , Barcode TEXT , Path Text)')
                            c.execute("INSERT INTO Data_Capture(Length,Width,Height,Weight,Cubical_Weight_Surface,Cubical_Weight_Air,Date,Barcode,path) values (?,?,?,?,?,?,?,?,?)",(self.label_10.text(),self.label_12.text(),self.label_11.text(),self.label_13.text(),self.label_14.text(),self.label_15.text(),datetime.datetime.now().date(),self.lineEdit_4.text(),barcode_path))
                            query = f"UPDATE date_and_time SET Date = ? WHERE ID = ?"
                            c.execute(query, ("YYYY-MM-DD  HH%MM%SS", '1'))
                            conn.commit()
                            c.close()

                            zpl ='^XA ^CF0,30 ^FO70,50^FD     Shipment ID : {}^FS ^FO70,100^FD     Date & Time : {}^FS ^CF0,30 ^FX Tabel. ^FO130,130^GB570,400,3^FS ^FO130,130^GB250,400,3^FS ^FO100,160^FD    Actual Weight^FS ^FO400,160^FD{} {}^FS ^FO100,260^FD    Dimension^FS ^FO400,260^FD{} x {} x {} ({})^FS ^FO100,360^FD    Vol.Weight(Surface)^FS ^FO400,360^FD{} kg3^FS ^FO100,460^FD    Vol.Weight(Air)^FS ^FO400,460^FD{} kg3^FS ^FO130,220^GB570,3,3^FS ^FO130,320^GB570,3,3^FS ^FO130,420^GB570,3,3^FS ^FO250,550^BQN,2,4^FD   Shipment ID : {} Date & Time : {} Actual Weight : {} {} Dimension : {}x{}x{} ({}) Vol.Weight (Surface) : {} Vol. Weight (Air) : {} ^FS ^XZ'.format(self.lineEdit_4.text(),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.label_13.text(),weight_unit,self.label_10.text(),self.label_12.text(),self.label_11.text(),distance_unit,self.label_14.text(),self.label_15.text(),self.lineEdit_4.text(),path,self.label_13.text(),weight_unit,self.label_10.text(),self.label_12.text(),self.label_11.text(),distance_unit,self.label_14.text(),self.label_15.text())
                            f = open("label.zpl", "w+")
                            f.write(zpl)
                            f.close()
                            subprocess.call(['lp', '-d', 'TSC_TE210', '-o', 'raw', 'label.zpl'])   

                            # self.label_58.setVisible(False)
                            break
                else:
                    self.label_58.setText("Keep Box Properly !!!")
                    self.label_58.setVisible(True)
                    break
        except serial.serialutil.SerialException:
            print("Failed to open serial port")


    def weight_setzero(self):
        try:
            self.wt_sz = self.a[4]
            self.lineEdit_9.setText(self.wt_sz)
        except AttributeError:
            print("Data not received")
        except IndexError:
            self.weight_setzero

    def height_setzero(self):
        try:
            self.ht_sz = self.a[3]
            self.lineEdit_5.setText(self.ht_sz)
        except AttributeError:
            print("Data not received")
        except IndexError:
            self.height_setzero

    def width_setzero(self):
        try:
            self.wdt_sz = self.a[2]
            self.lineEdit_7.setText(self.wdt_sz)
        except AttributeError:
            print("Data not received")
        except IndexError:
            self.width_setzero

    def length_setzero(self):
        try:
            self.len_sz = self.a[1]
            self.lineEdit_2.setText(self.len_sz)
        except AttributeError:
            print("Data not received")
        except IndexError:
            self.length_setzero

    def weight_setspan(self):
        if self.lineEdit_10.text() == '':
            print("Enter the known weight before setting up span")
        else:
            try:    
                self.known_weight_1 = float(self.lineEdit_10.text())  
                self.wt_sp = self.a[4]
                self.lineEdit_10.setText(self.wt_sp)
            except ValueError:
                print("Enter neumerical value in all fields")
            except serial.serialutil.SerialException:
                print("Failed to open serial port")
            except AttributeError:
                print("Data not received")
            except IndexError:
                self.weight_setspan


    def height_setspan(self):
        if self.lineEdit_6.text() == '':
            print("Enter the known weight before setting up span")
        else:
            try:    
                self.known_distance_3 = float(self.lineEdit_6.text()) 
                self.ht_sp = "600"
                self.lineEdit_6.setText(self.ht_sp)
            except ValueError:
                print("Enter neumerical value in all fields")
            except serial.serialutil.SerialException:
                print("Failed to open serial port")
            except AttributeError:
                print("Data not received")
            except IndexError:
                self.height_setspan

    def width_setspan(self):
        if self.lineEdit_8.text() == '':
            print("Enter the known weight before setting up span")
        else:
            try:    
                self.known_distance_2 = float(self.lineEdit_8.text())    
                self.wdt_sp = "600"
                self.lineEdit_8.setText(self.wdt_sp)
            except ValueError:
                print("Enter neumerical value in all fields")
            except serial.serialutil.SerialException:
                print("Failed to open serial port")
            except AttributeError:
                print("Data not received")
            except IndexError:
                self.width_setspan

    def length_setspan(self):
        if self.lineEdit_3.text() == '':
            print("Enter the known weight before setting up span")
        else:
            try:    
                self.known_distance_1 = float(self.lineEdit_3.text())        
                self.len_sp = "600"
                self.lineEdit_3.setText(self.len_sp)
            except ValueError:
                print("Enter neumerical value in all fields")
            except serial.serialutil.SerialException:
                print("Failed to open serial port")
            except AttributeError:
                print("Data not received")
            except IndexError:
                self.length_setspan

    def calibrate(self):
        try:
            self.coefficient_1 = (float(self.len_sp) - float(self.len_sz)) / float(self.known_distance_1)
            self.coefficient_2 = (float(self.wdt_sp) - float(self.wdt_sz)) / float(self.known_distance_2)
            self.coefficient_3 = (float(self.ht_sp) - float(self.ht_sz)) / float(self.known_distance_3)
            self.coefficient_4 = (float(self.wt_sp) -float(self.wt_sz)) / float(self.known_weight_1)
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS Coefficient(id INTEGER primary key AUTOINCREMENT,coefficient_1 INTEGER ,coefficient_2 INTEGER , coefficient_3 INTEGER , coefficient_4 INTEGER , length_setzero INTEGER ,width_setzero INTEGER, height_setzero INTEGER, weight_setzero INTEGER)')
            c.execute("INSERT INTO Coefficient (coefficient_1,coefficient_2,coefficient_3,coefficient_4,length_setzero,width_setzero,height_setzero,weight_setzero) values (?,?,?,?,?,?,?,?)",(self.coefficient_1,self.coefficient_2,self.coefficient_3,self.coefficient_4,float(self.len_sz),float(self.wdt_sz),float(self.ht_sz),float(self.wt_sz)))
            conn.commit()
            c.close() 
        except ValueError:
            print("Enter neumerical value in all fields")
        except NameError:
            print("Please enter known weight or known length before setting up span")
        except ZeroDivisionError:
            print("Setzero and Setspan values are same")
        except IndexError:
            self.calibrate
        except AttributeError:
            print("Data not received")
    
    def ok(self):
        try:
            calibrated_len = (float(self.a[1]) - float(self.len_sz))/self.coefficient_1
            self.label_37.setText("{:.3f}".format(calibrated_len))

            calibrated_wdt = (float(self.a[2]) - float(self.wdt_sz))/self.coefficient_2
            self.label_39.setText("{:.3f}".format(calibrated_wdt))

            calibrated_ht =  (float(self.a[3]) - float(self.ht_sz))/self.coefficient_3
            self.label_38.setText("{:.3f}".format(calibrated_ht))

            calibrated_wt =  (float(self.a[4]) - float(self.wt_sz))/self.coefficient_4
            self.label_40.setText("{:.2f}".format(calibrated_wt))
        except IndexError:
            self.ok
        except AttributeError:
            print("Data not received")
            
    def submit_configuration(self):
        try:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS Device_Configure(id INTEGER primary key AUTOINCREMENT,Terminal_ID INTEGER , Volume_Factor_Surface INTEGER , Volume_Factor_Air INTEGER ,Distance_Unit TEXT , Weight_Unit TEXT , Distance_Resolution INTEGER , Weight_Resolution INTEGER, Weight_Capacity INTEGER)')
            c.execute("INSERT INTO Device_Configure(Terminal_ID,Volume_Factor_Surface,Volume_Factor_Air,Distance_Unit,Weight_Unit,Distance_Resolution,Weight_Resolution,Weight_Capacity) values (?,?,?,?,?,?,?,?)",(int(self.lineEdit_15.text()),float(self.lineEdit_17.text()),float(self.lineEdit_18.text()),self.comboBox_2.currentText(),self.comboBox.currentText(),float(self.comboBox_3.currentText()),float(self.lineEdit_14.text()),float(self.lineEdit_16.text())))
            conn.commit()
            c.close() 
        except ValueError:
            print("Do not keep any field empty")
    
    def submit(self):
        try:
            if self.non_zero(float(self.label_10.text()),float(self.label_12.text()),float(self.label_11.text())):
                self.label_58.setVisible(False)
                conn = sqlite3.connect('database.db')
                conn.text_factory = str 
                cur = conn.cursor()
                query_1 = "SELECT EXISTS(SELECT 1 FROM Data_Capture WHERE Barcode={})".format(self.lineEdit_4.text())
                cur.execute(query_1)
                rows = cur.fetchall()
                for row in rows:
                    barcode_flag = row[0]
                conn.commit()
                cur.close()

                if barcode_flag == 0:
                    self.save_date() 
                    conn = sqlite3.connect('database.db')
                    conn.text_factory = str 
                    cur = conn.cursor()
                    query_1 = "SELECT * FROM date_and_time where ID = 1"
                    cur.execute(query_1)
                    rows = cur.fetchall()
                    for row in rows:
                        path = row[1]
                    conn.commit()
                    cur.close()
                    conn = sqlite3.connect('database.db')
                    conn.text_factory = str 
                    cur = conn.cursor()
                    query_2 = "SELECT * FROM Device_Configure ORDER BY id DESC LIMIT 1"
                    cur.execute(query_2)
                    rows = cur.fetchall()
                    for row in rows:
                        distance_unit = row[4]
                        weight_unit = row[5]
                    conn.commit()
                    conn.close()
                    self.Worker1.capture_image(path)
                    barcode_path = path+'.jpg'
                    if self.lineEdit_4.text != '':
                        self.label_58.setVisible(False) 
                        conn = sqlite3.connect('database.db')
                        c = conn.cursor()
                        c.execute('CREATE TABLE IF NOT EXISTS Data_Capture(id INTEGER primary key AUTOINCREMENT, Length INTEGER ,Width INTEGER , Height INTEGER , Weight INTEGER , Cubical_Weight_Surface INTEGER , Cubical_Weight_Air INTEGER , Date TEXT , Barcode TEXT , Path Text)')
                        c.execute("INSERT INTO Data_Capture(Length,Width,Height,Weight,Cubical_Weight_Surface,Cubical_Weight_Air,Date,Barcode,path) values (?,?,?,?,?,?,?,?,?)",(self.label_10.text(),self.label_12.text(),self.label_11.text(),self.label_13.text(),self.label_14.text(),self.label_15.text(),datetime.datetime.now().date(),self.lineEdit_4.text(),barcode_path))
                        query = f"UPDATE date_and_time SET Date = ? WHERE ID = ?"
                        c.execute(query, ("YYYY-MM-DD  HH%MM%SS", '1'))
                        conn.commit()
                        c.close()

                        zpl ='^XA ^CF0,30 ^FO70,50^FD     Shipment ID : {}^FS ^FO70,100^FD     Date & Time : {}^FS ^CF0,30 ^FX Tabel. ^FO130,130^GB570,400,3^FS ^FO130,130^GB250,400,3^FS ^FO100,160^FD    Actual Weight^FS ^FO400,160^FD{} {}^FS ^FO100,260^FD    Dimension^FS ^FO400,260^FD{} x {} x {} ({})^FS ^FO100,360^FD    Vol.Weight(Surface)^FS ^FO400,360^FD{} kg3^FS ^FO100,460^FD    Vol.Weight(Air)^FS ^FO400,460^FD{} kg3^FS ^FO130,220^GB570,3,3^FS ^FO130,320^GB570,3,3^FS ^FO130,420^GB570,3,3^FS ^FO250,550^BQN,2,4^FD   Shipment ID : {} Date & Time : {} Actual Weight : {} {} Dimension : {}x{}x{} ({}) Vol.Weight (Surface) : {} Vol. Weight (Air) : {} ^FS ^XZ'.format(self.lineEdit_4.text(),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.label_13.text(),weight_unit,self.label_10.text(),self.label_12.text(),self.label_11.text(),distance_unit,self.label_14.text(),self.label_15.text(),self.lineEdit_4.text(),path,self.label_13.text(),weight_unit,self.label_10.text(),self.label_12.text(),self.label_11.text(),distance_unit,self.label_14.text(),self.label_15.text())
                        f = open("label.zpl", "w+")
                        f.write(zpl)
                        f.close()
                        subprocess.call(['lp', '-d', 'TSC_TE210', '-o', 'raw', 'label.zpl']) 
                else:
                    self.label_58.setText("Already Scanned !!!")
                    self.label_58.setVisible(True)
                    self.save_date() 
                    conn = sqlite3.connect('database.db')
                    conn.text_factory = str 
                    cur = conn.cursor()
                    query_1 = "SELECT * FROM date_and_time where ID = 1"
                    cur.execute(query_1)
                    rows = cur.fetchall()
                    for row in rows:
                        path = row[1]
                    conn.commit()
                    cur.close()
                    conn = sqlite3.connect('database.db')
                    conn.text_factory = str 
                    cur = conn.cursor()
                    query_2 = "SELECT * FROM Device_Configure ORDER BY id DESC LIMIT 1"
                    cur.execute(query_2)
                    rows = cur.fetchall()
                    for row in rows:
                        distance_unit = row[4]
                        weight_unit = row[5]
                    conn.commit()
                    conn.close()
                    self.Worker1.capture_image(path)
                    barcode_path = path+'.jpg'
                    if self.lineEdit_4.text != '': 
                        conn = sqlite3.connect('database.db')
                        c = conn.cursor()
                        c.execute('CREATE TABLE IF NOT EXISTS Data_Capture(id INTEGER primary key AUTOINCREMENT, Length INTEGER ,Width INTEGER , Height INTEGER , Weight INTEGER , Cubical_Weight_Surface INTEGER , Cubical_Weight_Air INTEGER , Date TEXT , Barcode TEXT , Path Text)')
                        c.execute("INSERT INTO Data_Capture(Length,Width,Height,Weight,Cubical_Weight_Surface,Cubical_Weight_Air,Date,Barcode,path) values (?,?,?,?,?,?,?,?,?)",(self.label_10.text(),self.label_12.text(),self.label_11.text(),self.label_13.text(),self.label_14.text(),self.label_15.text(),datetime.datetime.now().date(),self.lineEdit_4.text(),barcode_path))
                        query = f"UPDATE date_and_time SET Date = ? WHERE ID = ?"
                        c.execute(query, ("YYYY-MM-DD  HH%MM%SS", '1'))
                        conn.commit()
                        c.close()
                        
                        zpl ='^XA ^CF0,30 ^FO70,50^FD     Shipment ID : {}^FS ^FO70,100^FD     Date & Time : {}^FS ^CF0,30 ^FX Tabel. ^FO130,130^GB570,400,3^FS ^FO130,130^GB250,400,3^FS ^FO100,160^FD    Actual Weight^FS ^FO400,160^FD{} {}^FS ^FO100,260^FD    Dimension^FS ^FO400,260^FD{} x {} x {} ({})^FS ^FO100,360^FD    Vol.Weight(Surface)^FS ^FO400,360^FD{} kg3^FS ^FO100,460^FD    Vol.Weight(Air)^FS ^FO400,460^FD{} kg3^FS ^FO130,220^GB570,3,3^FS ^FO130,320^GB570,3,3^FS ^FO130,420^GB570,3,3^FS ^FO250,550^BQN,2,4^FD   Shipment ID : {} Date & Time : {} Actual Weight : {} {} Dimension : {}x{}x{} ({}) Vol.Weight (Surface) : {} Vol. Weight (Air) : {} ^FS ^XZ'.format(self.lineEdit_4.text(),datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),self.label_13.text(),weight_unit,self.label_10.text(),self.label_12.text(),self.label_11.text(),distance_unit,self.label_14.text(),self.label_15.text(),self.lineEdit_4.text(),path,self.label_13.text(),weight_unit,self.label_10.text(),self.label_12.text(),self.label_11.text(),distance_unit,self.label_14.text(),self.label_15.text())
                        f = open("label.zpl", "w+")
                        f.write(zpl)
                        f.close()
                        subprocess.call(['lp', '-d', 'TSC_TE210', '-o', 'raw', 'label.zpl']) 
            else:
                self.label_58.setText("Keep Box Properly !!!")
                self.label_58.setVisible(True)
        except ValueError:
            print("Do not keep any field empty")
        except sqlite3.OperationalError:
            self.label_58.setText("Don't keep barcode field empty")
            self.label_58.setVisible(True)
    
    
    def fetch(self):
        try:
            usb_name = "/mnt/usb0"
            from_date = self.dateEdit.date().toPyDate()
            to_date = self.dateEdit_2.date().toPyDate()
            conn = sqlite3.connect('database.db')
            query = "SELECT Barcode,Weight,Cubical_Weight_Surface,Cubical_Weight_Air,Length,Width,Height,Path from Data_Capture where Date BETWEEN '{}' AND '{}'".format(from_date,to_date)
            cur = conn.cursor()
            data = cur.execute(query)
            a = datetime.datetime.now()
            if self.radioButton.isChecked() :
                # LOCAL STORAGE
                with open(r'./Reports/loadcell {}.csv'.format(a), 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Barcode', 'Actual_Weight', 'Cubical_Weight_Surface' , 'Cubical_Weight_Air', 'Length', 'Width' , 'Height' , 'Image_Path'])
                    writer.writerows(data)
                csv_data = []
                with open(r'./Reports/loadcell {}.csv'.format(a)) as file_obj:
                    reader = csv.reader(file_obj)
                    for row in reader:
                        csv_data.append(row)
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                for row in csv_data:
                    sheet.append(row)
                workbook.save(r'./Reports/loadcell {}.xlsx'.format(a))
                os.remove(r'./Reports/loadcell {}.csv'.format(a))
                # USB
                with open(r'{}/loadcell.csv'.format(usb_name), 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Barcode', 'Actual_Weight', 'Cubical_Weight_Surface' , 'Cubical_Weight_Air', 'Length', 'Width' , 'Height' , 'Image_Path'])
                    writer.writerows(data)
                csv_data = []
                with open(r'{}/loadcell.csv'.format(usb_name)) as file_obj:
                    reader = csv.reader(file_obj)
                    for row in reader:
                        csv_data.append(row)
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                for row in csv_data:
                    sheet.append(row)
                workbook.save(r'{}/loadcell.xlsx'.format(usb_name))
                os.remove(r'{}/loadcell.csv'.format(usb_name))
                print("File saved successfully!")
                
            elif self.radioButton_2.isChecked() :
                # LOCAL STORAGE
                with open(r'./Reports/loadcell {}.csv'.format(a), 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Barcode', 'Actual_Weight', 'Cubical_Weight_Surface' , 'Cubical_Weight_Air', 'Length', 'Width' , 'Height' , 'Image_Path'])
                    writer.writerows(data)

                # USB
                with open(r'{}/loadcell.csv'.format(usb_name), 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow(['Barcode', 'Actual_Weight', 'Cubical_Weight_Surface' , 'Cubical_Weight_Air', 'Length', 'Width' , 'Height' , 'Image_Path'])
                    writer.writerows(data)          
        except:
            pass

    def save_date(self):
        try:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute('CREATE TABLE IF NOT EXISTS date_and_time(id INTEGER primary key AUTOINCREMENT, Date Text)')
            query = f"UPDATE date_and_time SET Date = ? WHERE ID = ?"
            c.execute(query, (datetime.datetime.now(), '1'))
            conn.commit()
            c.close()
        except AttributeError:
            print("Data not received")

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
        self.lineEdit = cQLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(470, 230, 221, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.clicked.connect(self.Numpad_login)
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
        self.pushButton_13.clicked.connect(self.login)
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
        self.pushButton_16.clicked.connect(self.logout)
        self.pushButton_16.setHidden(True)
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
        self.pushButton_14.clicked.connect(self.fetch)
        self.label_23 = QtWidgets.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(40, 10, 271, 61))
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
        self.label_46.setHidden(True)
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
        self.label_19.setGeometry(QtCore.QRect(40, 110, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
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
        self.lineEdit_3 = cQLineEdit(self.tab_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 160, 441, 41))
        self.lineEdit_3.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.clicked.connect(self.Numpad_setspan_1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 240, 441, 41))
        self.lineEdit_5.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = cQLineEdit(self.tab_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 290, 441, 41))
        self.lineEdit_6.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.clicked.connect(self.Numpad_setspan_3)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(540, 110, 441, 41))
        self.lineEdit_7.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = cQLineEdit(self.tab_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(540, 160, 441, 41))
        self.lineEdit_8.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_8.clicked.connect(self.Numpad_setspan_2)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(540, 240, 441, 41))
        self.lineEdit_9.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = cQLineEdit(self.tab_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(540, 290, 441, 41))
        self.lineEdit_10.setStyleSheet("border-color: rgb(163, 163, 163);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.clicked.connect(self.Numpad_setspan_4)
        self.pushButton = QtWidgets.QPushButton(self.tab_4)
        self.pushButton.setGeometry(QtCore.QRect(370, 122, 76, 27))
        self.pushButton.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.length_setzero)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 167, 76, 27))
        self.pushButton_2.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.length_setspan)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(370, 247, 76, 27))
        self.pushButton_3.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.height_setzero)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_6.setGeometry(QtCore.QRect(370, 296, 76, 27))
        self.pushButton_6.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.height_setspan)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(885, 116, 76, 27))
        self.pushButton_7.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.width_setzero)
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_8.setGeometry(QtCore.QRect(885, 167, 76, 27))
        self.pushButton_8.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.width_setspan)
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(885, 246, 76, 27))
        self.pushButton_9.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.weight_setzero)
        self.pushButton_10 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_10.setGeometry(QtCore.QRect(885, 297, 76, 27))
        self.pushButton_10.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 10pt \"Ubuntu Mono\";\n"
"border-radius:6px\n"
"")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.weight_setspan)
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_11.setGeometry(QtCore.QRect(220, 340, 561, 31))
        self.pushButton_11.setStyleSheet("background-color: rgb(117, 37, 255);\n"
"font: 75 11pt \"Ubuntu Mono\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.calibrate)
        self.pushButton_12 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_12.setEnabled(True)
        self.pushButton_12.setGeometry(QtCore.QRect(909, 343, 71, 31))
        self.pushButton_12.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 11pt \"Ubuntu Mono\";\n"
"border-radius:6px;\n"
"color: rgb(255, 255, 255);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.ok)
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
        self.pushButton_17.clicked.connect(self.logout)
        self.label_37 = QtWidgets.QLabel(self.tab_4)
        self.label_37.setGeometry(QtCore.QRect(30, 377, 441, 41))
        self.label_37.setStyleSheet("border: 1px solid rgb(157, 157, 157);")
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.tab_4)
        self.label_38.setGeometry(QtCore.QRect(30, 430, 441, 41))
        self.label_38.setStyleSheet("border: 1px solid rgb(157, 157, 157);")
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.tab_4)
        self.label_39.setGeometry(QtCore.QRect(540, 377, 441, 41))
        self.label_39.setStyleSheet("border: 1px solid rgb(157, 157, 157);")
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.tab_4)
        self.label_40.setGeometry(QtCore.QRect(540, 430, 441, 41))
        self.label_40.setStyleSheet("border: 1px solid rgb(157, 157, 157);")
        self.label_40.setObjectName("label_40")
        self.label_44 = QtWidgets.QLabel(self.tab_4)
        self.label_44.setGeometry(QtCore.QRect(40, 10, 271, 61))
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
        self.label_48.setGeometry(QtCore.QRect(920, 350, 21, 20))
        self.label_48.setText("")
        self.label_48.setPixmap(QtGui.QPixmap(":/newPrefix/images/ok_.png"))
        self.label_48.setScaledContents(True)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.tab_4)
        self.label_49.setGeometry(QtCore.QRect(440, 345, 21, 20))
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
        self.pushButton_19.clicked.connect(self.logout)
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
        self.lineEdit_14 = cQLineEdit(self.tab_5)
        self.lineEdit_14.setGeometry(QtCore.QRect(540, 350, 441, 41))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setText("")
        self.lineEdit_14.clicked.connect(self.Numpad_Weight_Resolution)
        self.lineEdit_15 = cQLineEdit(self.tab_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(50, 82, 441, 41))
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_15.clicked.connect(self.Numpad_Terminal_ID) 
        self.label_36 = QtWidgets.QLabel(self.tab_5)
        self.label_36.setGeometry(QtCore.QRect(850, 364, 16, 16))
        self.label_36.setText("")
        self.label_36.setPixmap(QtGui.QPixmap(":/newPrefix/submit.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setObjectName("label_36")
        self.lineEdit_16 = cQLineEdit(self.tab_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(50, 350, 441, 41))
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_16.clicked.connect(self.Numpad_Weight_Capacity)
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
        self.lineEdit_17 = cQLineEdit(self.tab_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(540, 82, 441, 41))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_17.clicked.connect(self.Numpad_Volume_Factor)
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
        self.label_31.setGeometry(QtCore.QRect(1070, 545, 31, 31))
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
        self.pushButton_15.clicked.connect(self.submit_configuration)
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
        self.comboBox_3.addItem("")
        self.lineEdit_18 = cQLineEdit(self.tab_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(540, 170, 441, 41))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_18.clicked.connect(self.Numpad_Volume_Factor_Air)
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
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Ubuntu Mono\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(270, 210, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("font: 75 16pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(520, 210, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 75 16pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(60, 430, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 75 16pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(270, 430, 231, 91))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("font: 75 16pt \"Ubuntu Mono\";\n"
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
        self.pushButton_5.clicked.connect(self.submit)
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
        self.pushButton_18.clicked.connect(self.logout)
        self.pushButton_18.setHidden(True)
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(870, 20, 21, 21))
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap(":/newPrefix/images/logout.jpeg"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.label_33.setHidden(True)
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(510, 300, 201, 131))
        self.label_15.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 75 35pt \"Waree\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(510, 430, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("font: 75 16pt \"Ubuntu Mono\";\n"
"color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
#         self.save_data_button = QtWidgets.QPushButton(self.tab_2)
#         self.save_data_button.setGeometry(QtCore.QRect(1015, 108, 241, 41))
#         font = QtGui.QFont()
#         font.setFamily("Ubuntu Mono")
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(9)
#         self.save_data_button.setFont(font)
#         self.save_data_button.setStyleSheet("background-color: rgb(15, 16, 227);\n"
# "font: 75 12pt \"Ubuntu Mono\";\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius:6px\n"
# "")
#         self.save_data_button.setObjectName("save_data_button")
#         self.save_data_button.clicked.connect(self.save_data)
#         self.capture_button = QtWidgets.QPushButton(self.tab_2)
#         self.capture_button.setGeometry(QtCore.QRect(1018, 384, 241, 41))
#         font = QtGui.QFont()
#         font.setFamily("Ubuntu Mono")
#         font.setPointSize(12)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(9)
#         self.capture_button.setFont(font)
#         self.capture_button.setStyleSheet("background-color: rgb(237, 212, 0);\n"
# "color: rgb(255, 255, 255);\n"
# "font: 75 12pt \"Ubuntu Mono\";\n"
# "border-radius : 6px")
#         self.capture_button.setObjectName("capture_button")
#         self.capture_button.clicked.connect(self.save_date)
#         self.capture_button.clicked.connect(self.Worker1.capture_image)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(730, 350, 241, 41))
        self.lineEdit_4.setStyleSheet("font: 75 20pt \"Ubuntu Condensed\";")
        self.lineEdit_4.setObjectName("lineEdit_4")
        # self.label_32 = QtWidgets.QLabel(self.tab_2)
        # self.label_32.setGeometry(QtCore.QRect(1070, 390, 31, 31))
        # self.label_32.setText("")
        # self.label_32.setPixmap(QtGui.QPixmap(":/newPrefix/images/cam.png"))
        # self.label_32.setScaledContents(True)
        # self.label_32.setObjectName("label_32")
        # self.label_47 = QtWidgets.QLabel(self.tab_2)
        # self.label_47.setGeometry(QtCore.QRect(1050, 108, 51, 41))
        # self.label_47.setText("")
        # self.label_47.setPixmap(QtGui.QPixmap(":/newPrefix/images/save__.png"))
        # self.label_47.setScaledContents(True)
        # self.label_47.setObjectName("label_47")
        self.label_50 = QtWidgets.QLabel(self.tab_2)
        self.label_50.setGeometry(QtCore.QRect(120, 170, 67, 31))
        self.label_50.setStyleSheet("background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 85 22pt \"Ubuntu Condensed\";")
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.label_51 = QtWidgets.QLabel(self.tab_2)
        self.label_51.setGeometry(QtCore.QRect(347, 170, 67, 31))
        self.label_51.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px;\n"
"font: 75 22pt \"Ubuntu Condensed\";")
        self.label_51.setAlignment(QtCore.Qt.AlignCenter)
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(self.tab_2)
        self.label_52.setGeometry(QtCore.QRect(580, 170, 67, 31))
        self.label_52.setStyleSheet("font: 75 22pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_52.setAlignment(QtCore.Qt.AlignCenter)
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(self.tab_2)
        self.label_53.setGeometry(QtCore.QRect(120, 390, 67, 31))
        self.label_53.setStyleSheet("font: 75 22pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_53.setAlignment(QtCore.Qt.AlignCenter)
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(self.tab_2)
        self.label_54.setGeometry(QtCore.QRect(350, 390, 67, 31))
        self.label_54.setStyleSheet("font: 75 22pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_54.setAlignment(QtCore.Qt.AlignCenter)
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(self.tab_2)
        self.label_55.setGeometry(QtCore.QRect(580, 390, 67, 31))
        self.label_55.setStyleSheet("font: 75 22pt \"Ubuntu Condensed\";\n"
"background-color: rgb(0, 0, 127);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:6px")
        self.label_55.setAlignment(QtCore.Qt.AlignCenter)
        self.label_55.setObjectName("label_55")
        self.label_58 = QtWidgets.QLabel(self.tab_2)
        self.label_58.setGeometry(QtCore.QRect(310, 0, 831, 71))
        self.label_58.setStyleSheet("color: rgb(164, 0, 0);\n"
"font: 75 43pt \"Ubuntu Condensed\";")
        self.label_58.setObjectName("label_58")
        self.label_58.setVisible(False)
#         self.label_59 = QtWidgets.QLabel(self.tab_2)
#         self.label_59.setGeometry(QtCore.QRect(670, 300, 201, 131))
#         self.label_59.setStyleSheet("font: 87 20pt \"Arial Black\";\n"
# "background-color: rgb(0, 0, 127);\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius:6px")
#         self.label_59.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_59.setObjectName("label_59")
#         self.label_60 = QtWidgets.QLabel(self.tab_2)
#         self.label_60.setGeometry(QtCore.QRect(740, 390, 67, 17))
#         self.label_60.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
# "background-color: rgb(0, 0, 127);\n"
# "color: rgb(255, 255, 255);\n"
# "border-radius:6px")
#         self.label_60.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_60.setObjectName("label_60")
#         self.label_61 = QtWidgets.QLabel(self.tab_2)
#         self.label_61.setGeometry(QtCore.QRect(670, 430, 201, 51))
#         font = QtGui.QFont()
#         font.setFamily("Ubuntu Mono")
#         font.setPointSize(14)
#         font.setBold(False)
#         font.setItalic(False)
#         font.setWeight(9)
#         self.label_61.setFont(font)
#         self.label_61.setStyleSheet("font: 75 14pt \"Ubuntu Mono\";\n"
# "color: rgb(0, 0, 0);")
#         self.label_61.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_61.setObjectName("label_61")
        self.FeedLabel = QtWidgets.QLabel(self.tab_2)
        self.FeedLabel.setGeometry(QtCore.QRect(730, 80, 231, 211))
        self.FeedLabel.setText("")
        self.FeedLabel.setObjectName("FeedLabel")
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
        # self.tabWidget.removeTab(4)
        self.tabWidget.removeTab(3)
        self.tabWidget.removeTab(2)
        self.tabWidget.removeTab(1) 
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
        self.comboBox_2.setItemText(0, _translate("MainWindow", "mm"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "cm"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "inch"))
        self.label_41.setText(_translate("MainWindow", "Distance unit"))
        self.label_42.setText(_translate("MainWindow", "Distance resolution"))
        self.lineEdit_17.setPlaceholderText(_translate("MainWindow", "  Volume Factor"))
        self.pushButton_15.setText(_translate("MainWindow", "SUBMIT"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2"))
        # self.label_61.setText(_translate("MainWindow", "Cubical Weight (Air)"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "5"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "10"))
        # self.label_59.setText(_translate("MainWindow", "0"))
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
        self.label_58.setText(_translate("MainWindow", "Already Scanned !!"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Cubical Weight </p><p align=\"center\">(Air)</p></body></html>"))
        # self.save_data_button.setText(_translate("MainWindow", "SAVE DATA"))
        # self.capture_button.setText(_translate("MainWindow", "CAPTURE"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "  Barcode"))
        self.lineEdit_18.setPlaceholderText(_translate("MainWindow", "  Volume Factor (Air)"))
        self.label_50.setText(_translate("MainWindow", "Unit"))
        self.label_51.setText(_translate("MainWindow", "Unit"))
        # self.label_60.setText(_translate("MainWindow", "Unit"))
        self.label_52.setText(_translate("MainWindow", "Unit"))
        self.label_53.setText(_translate("MainWindow", "Unit"))
        self.label_54.setText(_translate("MainWindow", "Unit"))
        self.label_55.setText(_translate("MainWindow", "Unit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "           DATA CAPTURE         "))
import img_rc

class Worker1(QThread):
    try:
        ImageUpdate = pyqtSignal(QImage)
        def run(self):
            self.flag = 0
            self.ThreadActive = True
            Capture = cv2.VideoCapture(0)
            while self.ThreadActive:
                ret, frame = Capture.read()
                if ret:
                    Image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    FlippedImage = cv2.flip(Image, 1)
                    ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                    Pic = ConvertToQtFormat.scaled(231,211, Qt.KeepAspectRatio)
                    self.ImageUpdate.emit(Pic)
                if self.flag:
                    try:
                        route = r'./Reports/barcode_images/'
                        QtWidgets.QApplication.beep()
                        name = "{}.jpg".format(self.path) 
                        cv2.imwrite(os.path.join(route, name), frame)
                        self.flag = 0
                    except:
                        "Connect Camera"
        def capture_image(self,path):
            self.flag = 1
            self.path = path
    except:
        pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    scheduler = QtScheduler()
    scheduler.add_job(ui.serial_data, 'interval', seconds=1)
    scheduler.add_job(ui.barcode, 'interval', seconds=1)
    scheduler.start()

    sys.exit(app.exec_())
