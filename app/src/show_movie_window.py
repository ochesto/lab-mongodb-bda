# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show_movie_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src.mongodb import *

class Ui_show_movie_window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_movies = QtWidgets.QTableView(self.centralwidget)
        self.table_movies.setGeometry(QtCore.QRect(30, 60, 925, 201))
        self.table_movies.setObjectName("table_movies")
        self.label_show_movies = QtWidgets.QLabel(self.centralwidget)
        self.label_show_movies.setGeometry(QtCore.QRect(220, 20, 91, 17))
        self.label_show_movies.setObjectName("label_show_movies")
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
                    "genre",
                    "director's name",
                    "franchise",
                    "country",
                    "year",
                    "duration",
                    "company",
                    "actors" ]
            )
        self.fill_data()
        self.table_movies.setModel( self.model )
        self.pushButton.clicked.connect( MainWindow.close )


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_show_movies.setText(_translate("MainWindow", "show movies"))
        self.pushButton.setText(_translate("MainWindow", "close"))

    def fill_data(self):
        lst = show_movies()
        row_count = 0
        for tuple_read in lst:
            data = tuple_read
            self.model.setItem(row_count, 0, QtGui.QStandardItem(str(data['name'])))
            self.model.setItem(row_count, 1, QtGui.QStandardItem(str(data['genre'])))
            self.model.setItem(row_count, 2, QtGui.QStandardItem(str(data['directors_name'])))
            self.model.setItem(row_count, 3, QtGui.QStandardItem(str(data['franchise'])))
            self.model.setItem(row_count, 4, QtGui.QStandardItem(str(data['country'])))
            self.model.setItem(row_count, 5, QtGui.QStandardItem(str(data['year'])))
            self.model.setItem(row_count, 6, QtGui.QStandardItem(str(data['duration'])))
            self.model.setItem(row_count, 7, QtGui.QStandardItem(str(data['company'])))
            self.model.setItem(row_count, 8, QtGui.QStandardItem(str(data['actors'])))
            row_count += 1

