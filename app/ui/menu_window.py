# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(549, 308)
        self.centralWidget = QtWidgets.QWidget(menu_window)
        self.centralWidget.setObjectName("centralWidget")
        self.label_lab = QtWidgets.QLabel(self.centralWidget)
        self.label_lab.setGeometry(QtCore.QRect(10, 20, 151, 17))
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
        self.button_exit.setGeometry(QtCore.QRect(230, 270, 89, 25))
        self.button_exit.setObjectName("button_exit")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(263, 20, 20, 231))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.button_search_movies = QtWidgets.QPushButton(self.centralWidget)
        self.button_search_movies.setGeometry(QtCore.QRect(320, 110, 171, 25))
        self.button_search_movies.setObjectName("button_search_movies")
        self.button_statistics = QtWidgets.QPushButton(self.centralWidget)
        self.button_statistics.setGeometry(QtCore.QRect(320, 190, 171, 25))
        self.button_statistics.setObjectName("button_statistics")
        menu_window.setCentralWidget(self.centralWidget)

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

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
        self.button_search_movies.setText(_translate("menu_window", "search about movies"))
        self.button_statistics.setText(_translate("menu_window", "companies statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_window = QtWidgets.QMainWindow()
    ui = Ui_menu_window()
    ui.setupUi(menu_window)
    menu_window.show()
    sys.exit(app.exec_())

