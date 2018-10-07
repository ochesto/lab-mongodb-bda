# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/create_movie_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

#import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from src.mongodb import *


class Ui_create_movie_window(object):
    def setupUi(self, create_movie_window):
        self.window = create_movie_window
        create_movie_window.setObjectName("create_movie_window")
        create_movie_window.resize(309, 390)
        self.centralwidget = QtWidgets.QWidget(create_movie_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(50, 50, 67, 17))
        self.label_name.setObjectName("label_name")
        self.label_genre = QtWidgets.QLabel(self.centralwidget)
        self.label_genre.setGeometry(QtCore.QRect(50, 80, 67, 17))
        self.label_genre.setObjectName("label_genre")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(50, 200, 67, 17))
        self.label_year.setObjectName("label_year")
        self.label_actors = QtWidgets.QLabel(self.centralwidget)
        self.label_actors.setGeometry(QtCore.QRect(50, 290, 67, 17))
        self.label_actors.setObjectName("label_actors")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(100, 50, 113, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_genre = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_genre.setGeometry(QtCore.QRect(100, 80, 113, 25))
        self.lineEdit_genre.setObjectName("lineEdit_genre")
        self.lineEdit_directors_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_directors_name.setGeometry(QtCore.QRect(170, 110, 113, 25))
        self.lineEdit_directors_name.setObjectName("lineEdit_directors_name")
        self.lineEdit_franchise = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_franchise.setGeometry(QtCore.QRect(130, 140, 113, 25))
        self.lineEdit_franchise.setObjectName("lineEdit_franchise")
        self.lineEdit_country = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_country.setGeometry(QtCore.QRect(110, 170, 113, 25))
        self.lineEdit_country.setObjectName("lineEdit_country")
        self.lineEdit_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_year.setGeometry(QtCore.QRect(90, 200, 113, 25))
        self.lineEdit_year.setObjectName("lineEdit_year")
        self.lineEdit_duration = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_duration.setGeometry(QtCore.QRect(120, 230, 113, 25))
        self.lineEdit_duration.setObjectName("lineEdit_duration")
        self.lineEdit_company = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_company.setGeometry(QtCore.QRect(120, 260, 113, 25))
        self.lineEdit_company.setObjectName("lineEdit_company")
        self.lineEdit_actors = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_actors.setGeometry(QtCore.QRect(100, 290, 113, 25))
        self.lineEdit_actors.setObjectName("lineEdit_actors")
        self.label_directors_name = QtWidgets.QLabel(self.centralwidget)
        self.label_directors_name.setGeometry(QtCore.QRect(50, 110, 111, 17))
        self.label_directors_name.setObjectName("label_directors_name")
        self.label_franchise = QtWidgets.QLabel(self.centralwidget)
        self.label_franchise.setGeometry(QtCore.QRect(50, 140, 67, 17))
        self.label_franchise.setObjectName("label_franchise")
        self.label_company = QtWidgets.QLabel(self.centralwidget)
        self.label_company.setGeometry(QtCore.QRect(50, 260, 67, 17))
        self.label_company.setObjectName("label_company")
        self.label_country = QtWidgets.QLabel(self.centralwidget)
        self.label_country.setGeometry(QtCore.QRect(50, 170, 67, 17))
        self.label_country.setObjectName("label_country")
        self.label_new_movie = QtWidgets.QLabel(self.centralwidget)
        self.label_new_movie.setGeometry(QtCore.QRect(110, 10, 91, 17))
        self.label_new_movie.setObjectName("label_new_movie")
        self.label_duration = QtWidgets.QLabel(self.centralwidget)
        self.label_duration.setGeometry(QtCore.QRect(50, 230, 67, 17))
        self.label_duration.setObjectName("label_duration")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(40, 330, 89, 25))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(170, 330, 89, 25))
        self.pushButton_submit.setObjectName("pushButton_submit")
        create_movie_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(create_movie_window)
        self.statusbar.setObjectName("statusbar")
        create_movie_window.setStatusBar(self.statusbar)

        self.retranslateUi(create_movie_window)
        QtCore.QMetaObject.connectSlotsByName(create_movie_window)

        # BUTTON HANDLERS #
        self.pushButton_cancel.clicked.connect( create_movie_window.close )
        self.pushButton_submit.clicked.connect( self.submit )

    def retranslateUi(self, create_movie_window):
        _translate = QtCore.QCoreApplication.translate
        create_movie_window.setWindowTitle(_translate("create_movie_window", "new movie - EUR"))
        self.label_name.setText(_translate("create_movie_window", "name"))
        self.label_genre.setText(_translate("create_movie_window", "genre"))
        self.label_year.setText(_translate("create_movie_window", "year"))
        self.label_actors.setText(_translate("create_movie_window", "actors"))
        self.label_directors_name.setText(_translate("create_movie_window", "director\'s name"))
        self.label_franchise.setText(_translate("create_movie_window", "franchise"))
        self.label_company.setText(_translate("create_movie_window", "company"))
        self.label_country.setText(_translate("create_movie_window", "country"))
        self.label_new_movie.setText(_translate("create_movie_window", "new movie"))
        self.pushButton_cancel.setText(_translate("create_movie_window", "cancel"))
        self.pushButton_submit.setText(_translate("create_movie_window", "submit"))
        self.label_duration.setText(_translate("create_movie_window", "duration"))

    def submit(self):
        res = create_movie(   self.lineEdit_name.text(),
                        self.lineEdit_genre.text(),
                        self.lineEdit_directors_name.text(),
                        self.lineEdit_franchise.text(),
                        self.lineEdit_country.text(),
                        self.lineEdit_year.text(),
                        self.lineEdit_duration.text(),
                        self.lineEdit_company.text(),
                        self.lineEdit_actors.text() )
        self.showdialog( res )
    
    def showdialog(self, p_response):
        msg = QtWidgets.QMessageBox()
        if( p_response == 0 ):
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("data inserted correctly")
            msg.buttonClicked.connect(self.window.close)
        else:
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("error inserting data")
        msg.setWindowTitle("insert info")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
