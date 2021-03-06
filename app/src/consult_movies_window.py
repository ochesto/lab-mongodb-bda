# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consult_movies.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from src.mongodb import *

class Ui_consult_movies_window(object):
    def setupUi(self, consult_movies_window):
        consult_movies_window.setObjectName("consult_movies_window")
        consult_movies_window.resize(985, 446)
        self.centralwidget = QtWidgets.QWidget(consult_movies_window)
        self.centralwidget.setObjectName("centralwidget")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(860, 20, 89, 25))
        self.button_close.setObjectName("button_close")
        self.table_movies = QtWidgets.QTableView(self.centralwidget)
        self.table_movies.setGeometry(QtCore.QRect(20, 70, 925, 201))
        self.table_movies.setObjectName("table_movies")
        self.pushButton_by_movie_name = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_by_movie_name.setGeometry(QtCore.QRect(330, 320, 131, 25))
        self.pushButton_by_movie_name.setObjectName("pushButton_by_movie_name")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(130, 320, 181, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_movie_name = QtWidgets.QLabel(self.centralwidget)
        self.label_movie_name.setGeometry(QtCore.QRect(40, 320, 91, 17))
        self.label_movie_name.setObjectName("label_movie_name")
        self.label_franchise = QtWidgets.QLabel(self.centralwidget)
        self.label_franchise.setGeometry(QtCore.QRect(40, 380, 91, 17))
        self.label_franchise.setObjectName("label_franchise")
        self.lineEdit_franchise = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_franchise.setGeometry(QtCore.QRect(130, 380, 181, 25))
        self.lineEdit_franchise.setText("")
        self.lineEdit_franchise.setObjectName("lineEdit_franchise")
        self.pushButton_by_franchise = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_by_franchise.setGeometry(QtCore.QRect(330, 380, 141, 25))
        self.pushButton_by_franchise.setObjectName("pushButton_by_franchise")
        self.label_results = QtWidgets.QLabel(self.centralwidget)
        self.label_results.setGeometry(QtCore.QRect(20, 50, 111, 17))
        self.label_results.setObjectName("label_results")
        self.lineEdit_initial_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_initial_year.setGeometry(QtCore.QRect(630, 290, 113, 25))
        self.lineEdit_initial_year.setObjectName("lineEdit_initial_year")
        self.lineEdit_final_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_final_year.setGeometry(QtCore.QRect(630, 320, 113, 25))
        self.lineEdit_final_year.setObjectName("lineEdit_final_year")
        self.label_initial_year = QtWidgets.QLabel(self.centralwidget)
        self.label_initial_year.setGeometry(QtCore.QRect(550, 290, 81, 17))
        self.label_initial_year.setObjectName("label_initial_year")
        self.label_final_year = QtWidgets.QLabel(self.centralwidget)
        self.label_final_year.setGeometry(QtCore.QRect(550, 320, 81, 17))
        self.label_final_year.setObjectName("label_final_year")
        self.pushButton_by_range = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_by_range.setGeometry(QtCore.QRect(760, 300, 171, 25))
        self.pushButton_by_range.setObjectName("pushButton_by_range")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 300, 16, 131))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(50, 350, 431, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(540, 350, 431, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lineEdit_companys_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_companys_name.setGeometry(QtCore.QRect(730, 380, 151, 25))
        self.lineEdit_companys_name.setObjectName("lineEdit_companys_name")
        self.label_companys_name = QtWidgets.QLabel(self.centralwidget)
        self.label_companys_name.setGeometry(QtCore.QRect(610, 380, 121, 17))
        self.label_companys_name.setObjectName("label_companys_name")
        self.pushButton_by_company = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_by_company.setGeometry(QtCore.QRect(660, 410, 191, 25))
        self.pushButton_by_company.setObjectName("pushButton_by_company")
        consult_movies_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(consult_movies_window)
        QtCore.QMetaObject.connectSlotsByName(consult_movies_window)

        self.button_close.clicked.connect( consult_movies_window.close )

    def retranslateUi(self, consult_movies_window):
        _translate = QtCore.QCoreApplication.translate
        consult_movies_window.setWindowTitle(_translate("consult_movies_window", "consult movies info - EUR"))
        self.button_close.setText(_translate("consult_movies_window", "close"))
        self.pushButton_by_movie_name.setText(_translate("consult_movies_window", "search by name"))
        self.label_movie_name.setText(_translate("consult_movies_window", "movie name"))
        self.label_franchise.setText(_translate("consult_movies_window", "franchise"))
        self.pushButton_by_franchise.setText(_translate("consult_movies_window", "search by franchise"))
        self.label_results.setText(_translate("consult_movies_window", "search results"))
        self.label_initial_year.setText(_translate("consult_movies_window", "initial year"))
        self.label_final_year.setText(_translate("consult_movies_window", "final year"))
        self.pushButton_by_range.setText(_translate("consult_movies_window", "search by year range"))
        self.label_companys_name.setText(_translate("consult_movies_window", "company\'s name"))
        self.pushButton_by_company.setText(_translate("consult_movies_window", "search by company\'s name"))


