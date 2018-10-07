# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from src.mongodb import *

from src.create_movie_window import *
from src.show_movie_window import *
from src.update_movie_window import *
from src.delete_movie_window import *

from src.create_company_window import *
from src.show_companies_window import *
from src.update_company_window import *
from src.delete_company_window import *

class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(289, 322)
        self.centralWidget = QtWidgets.QWidget(menu_window)
        self.centralWidget.setObjectName("centralWidget")
        self.label_lab = QtWidgets.QLabel(self.centralWidget)
        self.label_lab.setGeometry(QtCore.QRect(100, 30, 151, 17))
        self.label_lab.setObjectName("label_lab")
        self.button_movie_create = QtWidgets.QPushButton(self.centralWidget)
        self.button_movie_create.setGeometry(QtCore.QRect(30, 120, 89, 25))
        self.button_movie_create.setObjectName("button_movie_create")
        self.button_movie_show = QtWidgets.QPushButton(self.centralWidget)
        self.button_movie_show.setGeometry(QtCore.QRect(30, 150, 89, 25))
        self.button_movie_show.setObjectName("button_movie_show")
        self.button_movie_edit = QtWidgets.QPushButton(self.centralWidget)
        self.button_movie_edit.setGeometry(QtCore.QRect(30, 180, 89, 25))
        self.button_movie_edit.setObjectName("button_movie_edit")
        self.button_movie_delete = QtWidgets.QPushButton(self.centralWidget)
        self.button_movie_delete.setGeometry(QtCore.QRect(30, 210, 89, 25))
        self.button_movie_delete.setObjectName("button_movie_delete")
        self.label_movie = QtWidgets.QLabel(self.centralWidget)
        self.label_movie.setGeometry(QtCore.QRect(40, 90, 67, 17))
        self.label_movie.setObjectName("label_movie")
        self.button_company_show = QtWidgets.QPushButton(self.centralWidget)
        self.button_company_show.setGeometry(QtCore.QRect(150, 150, 89, 25))
        self.button_company_show.setObjectName("button_company_show")
        self.button_company_create = QtWidgets.QPushButton(self.centralWidget)
        self.button_company_create.setGeometry(QtCore.QRect(150, 120, 89, 25))
        self.button_company_create.setObjectName("button_company_create")
        self.label_company = QtWidgets.QLabel(self.centralWidget)
        self.label_company.setGeometry(QtCore.QRect(160, 90, 67, 17))
        self.label_company.setObjectName("label_company")
        self.button_company_edit = QtWidgets.QPushButton(self.centralWidget)
        self.button_company_edit.setGeometry(QtCore.QRect(150, 180, 89, 25))
        self.button_company_edit.setObjectName("button_company_edit")
        self.button_company_delete = QtWidgets.QPushButton(self.centralWidget)
        self.button_company_delete.setGeometry(QtCore.QRect(150, 210, 89, 25))
        self.button_company_delete.setObjectName("button_company_delete")
        self.button_exit = QtWidgets.QPushButton(self.centralWidget)
        self.button_exit.setGeometry(QtCore.QRect(80, 260, 89, 25))
        self.button_exit.setObjectName("button_exit")
        menu_window.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(menu_window)
        self.statusBar.setObjectName("statusBar")
        menu_window.setStatusBar(self.statusBar)

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

        self.dialog_create_movie = Ui_create_movie_window()
        # BUTTON HANDLERS #
        self.button_movie_create.clicked.connect( self.movie_create )
        self.button_movie_show.clicked.connect( self.movie_show )
        self.button_movie_edit.clicked.connect( self.movie_edit )
        self.button_movie_delete.clicked.connect( self.movie_delete )

        self.button_company_create.clicked.connect( self.company_create )
        self.button_company_show.clicked.connect( self.company_show )
        self.button_company_edit.clicked.connect( self.company_edit )
        self.button_company_delete.clicked.connect( self.company_delete )
        self.button_exit.clicked.connect( menu_window.close )


    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "lab - mongodb - EUR"))
        self.label_lab.setText(_translate("menu_window", "lab - mongodb"))
        self.button_movie_create.setText(_translate("menu_window", "create"))
        self.button_movie_show.setText(_translate("menu_window", "show"))
        self.button_movie_edit.setText(_translate("menu_window", "edit"))
        self.button_movie_delete.setText(_translate("menu_window", "delete"))
        self.label_movie.setText(_translate("menu_window", "movie"))
        self.button_company_show.setText(_translate("menu_window", "show"))
        self.button_company_create.setText(_translate("menu_window", "create"))
        self.label_company.setText(_translate("menu_window", "company"))
        self.button_company_edit.setText(_translate("menu_window", "edit"))
        self.button_company_delete.setText(_translate("menu_window", "delete"))
        self.button_exit.setText(_translate("menu_window", "exit"))

    def movie_create(self):
        print ("movie_create")
        self.child_menu_window = QtWidgets.QMainWindow()
        self.child_win = Ui_create_movie_window()
        self.child_win.setupUi(self.child_menu_window)
        self.child_menu_window.show()

    def movie_show(self):
        print ("movie_show")
        self.child_show_movie = QtWidgets.QMainWindow()
        self.ui_child = Ui_show_movie_window()
        self.ui_child.setupUi(self.child_show_movie)
        self.child_show_movie.show()

    def movie_edit(self):
        print ("movie_edit")
        self.child_update_movie = QtWidgets.QMainWindow()
        self.ui_child_u = Ui_update_movie_window()
        self.ui_child_u.setupUi(self.child_update_movie)
        self.child_update_movie.show()

    def movie_delete(self):
        print ("movie_delete")
        self.child_delete_movie = QtWidgets.QMainWindow()
        self.ui_child_d = Ui_delete_movie_window()
        self.ui_child_d.setupUi(self.child_delete_movie)
        self.child_delete_movie.show()

    def company_create(self):
        print ("company_create")
        self.child_create_company_window = QtWidgets.QMainWindow()
        self.child_win_cc = Ui_create_company_window()
        self.child_win_cc.setupUi(self.child_create_company_window)
        self.child_create_company_window.show()

    def company_show(self):
        print ("company_show")
        self.child_show_company = QtWidgets.QMainWindow()
        self.ui_child_sc = Ui_show_companies_window()
        self.ui_child_sc.setupUi(self.child_show_company)
        self.child_show_company.show()

    def company_edit(self):
        print ("company_edit")
        self.child_update_company = QtWidgets.QMainWindow()
        self.ui_child_uc = Ui_update_company_window()
        self.ui_child_uc.setupUi(self.child_update_company)
        self.child_update_company.show()

    def company_delete(self):
        print ("company_delete")
        self.child_delete_company = QtWidgets.QMainWindow()
        self.ui_child_dc = Ui_delete_company_window()
        self.ui_child_dc.setupUi(self.child_delete_company)
        self.child_delete_company.show()

def create_menu():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_window = QtWidgets.QMainWindow()
    ui = Ui_menu_window()
    ui.setupUi(menu_window)
    menu_window.show()
    sys.exit(app.exec_())