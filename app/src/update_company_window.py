# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_company.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src.mongodb import *

class Ui_update_company_window(object):
    def setupUi(self, update_company_window):
        update_company_window.setObjectName("update_company_window")
        update_company_window.resize(294, 264)
        self.window = update_company_window
        self.centralwidget = QtWidgets.QWidget(update_company_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(30, 50, 67, 17))
        self.label_name.setObjectName("label_name")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(100, 50, 161, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_update_company = QtWidgets.QLabel(self.centralwidget)
        self.label_update_company.setGeometry(QtCore.QRect(90, 10, 111, 17))
        self.label_update_company.setObjectName("label_update_company")
        self.lineEdit_field = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_field.setGeometry(QtCore.QRect(20, 150, 113, 25))
        self.lineEdit_field.setObjectName("lineEdit_field")
        self.label_field = QtWidgets.QLabel(self.centralwidget)
        self.label_field.setGeometry(QtCore.QRect(50, 120, 67, 17))
        self.label_field.setObjectName("label_field")
        self.lineEdit_new_data = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_new_data.setGeometry(QtCore.QRect(160, 150, 113, 25))
        self.lineEdit_new_data.setObjectName("lineEdit_new_data")
        self.label_new_data = QtWidgets.QLabel(self.centralwidget)
        self.label_new_data.setGeometry(QtCore.QRect(180, 120, 81, 20))
        self.label_new_data.setObjectName("label_new_data")
        self.button_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.button_cancel.setGeometry(QtCore.QRect(30, 200, 89, 25))
        self.button_cancel.setObjectName("button_cancel")
        self.button_update = QtWidgets.QPushButton(self.centralwidget)
        self.button_update.setGeometry(QtCore.QRect(170, 200, 89, 25))
        self.button_update.setObjectName("button_update")
        update_company_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(update_company_window)
        self.statusbar.setObjectName("statusbar")
        update_company_window.setStatusBar(self.statusbar)

        self.retranslateUi(update_company_window)
        QtCore.QMetaObject.connectSlotsByName(update_company_window)

        self.button_cancel.clicked.connect(update_company_window.close)
        self.button_update.clicked.connect(self.submit)

    def retranslateUi(self, update_company_window):
        _translate = QtCore.QCoreApplication.translate
        update_company_window.setWindowTitle(_translate("update_company_window", "update company - EUR"))
        self.label_name.setText(_translate("update_company_window", "name"))
        self.label_update_company.setText(_translate("update_company_window", "update company"))
        self.label_field.setText(_translate("update_company_window", "field"))
        self.label_new_data.setText(_translate("update_company_window", "new data"))
        self.button_cancel.setText(_translate("update_company_window", "cancel"))
        self.button_update.setText(_translate("update_company_window", "update"))
    
    def submit(self):
        res = update_company(   self.lineEdit_name.text(),
                        self.lineEdit_field.text(),
                        self.lineEdit_new_data.text() )
        self.showdialog( res )

    def showdialog(self, p_response):
        msg = QtWidgets.QMessageBox()
        if( p_response == 0 ):
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("data updated correctly")
            msg.buttonClicked.connect(self.window.close)
        else:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("error inserting data")
        msg.setWindowTitle("update info")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()


