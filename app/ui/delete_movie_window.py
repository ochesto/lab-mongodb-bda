# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete_movie_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_delete_movie_window(object):
    def setupUi(self, delete_movie_window):
        delete_movie_window.setObjectName("delete_movie_window")
        delete_movie_window.resize(456, 183)
        self.centralwidget = QtWidgets.QWidget(delete_movie_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_delete_movie = QtWidgets.QLabel(self.centralwidget)
        self.label_delete_movie.setGeometry(QtCore.QRect(180, 20, 101, 17))
        self.label_delete_movie.setObjectName("label_delete_movie")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(140, 70, 113, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(70, 70, 67, 17))
        self.label_name.setObjectName("label_name")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(280, 70, 89, 25))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(180, 120, 89, 25))
        self.pushButton_close.setObjectName("pushButton_close")
        delete_movie_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(delete_movie_window)
        self.statusbar.setObjectName("statusbar")
        delete_movie_window.setStatusBar(self.statusbar)

        self.retranslateUi(delete_movie_window)
        QtCore.QMetaObject.connectSlotsByName(delete_movie_window)

    def retranslateUi(self, delete_movie_window):
        _translate = QtCore.QCoreApplication.translate
        delete_movie_window.setWindowTitle(_translate("delete_movie_window", "delete movie - EUR"))
        self.label_delete_movie.setText(_translate("delete_movie_window", "delete movie"))
        self.label_name.setText(_translate("delete_movie_window", "name"))
        self.pushButton_delete.setText(_translate("delete_movie_window", "delete"))
        self.pushButton_close.setText(_translate("delete_movie_window", "close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    delete_movie_window = QtWidgets.QMainWindow()
    ui = Ui_delete_movie_window()
    ui.setupUi(delete_movie_window)
    delete_movie_window.show()
    sys.exit(app.exec_())

