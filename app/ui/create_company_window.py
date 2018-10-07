# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_company_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_create_company_window(object):
    def setupUi(self, create_company_window):
        create_company_window.setObjectName("create_company_window")
        create_company_window.resize(277, 233)
        self.centralwidget = QtWidgets.QWidget(create_company_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_new_company = QtWidgets.QLabel(self.centralwidget)
        self.label_new_company.setGeometry(QtCore.QRect(70, 20, 131, 17))
        self.label_new_company.setObjectName("label_new_company")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(60, 70, 67, 17))
        self.label_name.setObjectName("label_name")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(110, 70, 113, 25))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.label_fundation = QtWidgets.QLabel(self.centralwidget)
        self.label_fundation.setGeometry(QtCore.QRect(10, 100, 121, 17))
        self.label_fundation.setObjectName("label_fundation")
        self.lineEdit__fundation_year = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit__fundation_year.setGeometry(QtCore.QRect(120, 100, 113, 25))
        self.lineEdit__fundation_year.setObjectName("lineEdit__fundation_year")
        self.label_web_address = QtWidgets.QLabel(self.centralwidget)
        self.label_web_address.setGeometry(QtCore.QRect(30, 130, 101, 17))
        self.label_web_address.setObjectName("label_web_address")
        self.lineEdit__web_address = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit__web_address.setGeometry(QtCore.QRect(130, 130, 113, 25))
        self.lineEdit__web_address.setObjectName("lineEdit__web_address")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(30, 170, 89, 25))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.pushButton_submit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submit.setGeometry(QtCore.QRect(150, 170, 89, 25))
        self.pushButton_submit.setObjectName("pushButton_submit")
        create_company_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(create_company_window)
        QtCore.QMetaObject.connectSlotsByName(create_company_window)

    def retranslateUi(self, create_company_window):
        _translate = QtCore.QCoreApplication.translate
        create_company_window.setWindowTitle(_translate("create_company_window", "new company - EUR"))
        self.label_new_company.setText(_translate("create_company_window", "new company"))
        self.label_name.setText(_translate("create_company_window", "name"))
        self.label_fundation.setText(_translate("create_company_window", "fundation year"))
        self.label_web_address.setText(_translate("create_company_window", "web address"))
        self.pushButton_cancel.setText(_translate("create_company_window", "cancel"))
        self.pushButton_submit.setText(_translate("create_company_window", "submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_company_window = QtWidgets.QMainWindow()
    ui = Ui_create_company_window()
    ui.setupUi(create_company_window)
    create_company_window.show()
    sys.exit(app.exec_())

