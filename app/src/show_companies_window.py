# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_companies_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src.mongodb import *

class Ui_show_companies_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("show companies - EUR")
        MainWindow.resize(985, 400)
        self.window = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_companies = QtWidgets.QTableView(self.centralwidget)
        self.table_companies.setGeometry(QtCore.QRect(30, 60, 925, 201))
        self.table_companies.setObjectName("table_companies")
        self.label_show_companies = QtWidgets.QLabel(self.centralwidget)
        self.label_show_companies.setGeometry(QtCore.QRect(220, 20, 91, 17))
        self.label_show_companies.setObjectName("label_show_companies")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 270, 89, 25))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
                [   "name",
                    "fundation year",
                    "web address" ]
            )
        self.fill_data()
        self.table_companies.setModel( self.model )
        self.pushButton.clicked.connect( MainWindow.close )


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_show_companies.setText(_translate("MainWindow", "show companies"))
        self.pushButton.setText(_translate("MainWindow", "close"))

    def fill_data(self):
        lst = show_companies()
        row_count = 0
        for tuple_read in lst:
            data = tuple_read
            self.model.setItem(row_count, 0, QtGui.QStandardItem(str(data['name'])))
            self.model.setItem(row_count, 1, QtGui.QStandardItem(str(data['fundation_year'])))
            self.model.setItem(row_count, 2, QtGui.QStandardItem(str(data['web_address'])))
            row_count += 1

