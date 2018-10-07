# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_statistics_window(object):
    def setupUi(self, statistics_window):
        statistics_window.setObjectName("statistics_window")
        statistics_window.resize(396, 348)
        self.centralwidget = QtWidgets.QWidget(statistics_window)
        self.centralwidget.setObjectName("centralwidget")
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(60, 290, 89, 25))
        self.button_close.setObjectName("button_close")
        self.label_movies_amount = QtWidgets.QLabel(self.centralwidget)
        self.label_movies_amount.setGeometry(QtCore.QRect(40, 40, 121, 17))
        self.label_movies_amount.setObjectName("label_movies_amount")
        self.label_amount_response = QtWidgets.QLabel(self.centralwidget)
        self.label_amount_response.setGeometry(QtCore.QRect(160, 40, 221, 17))
        self.label_amount_response.setObjectName("label_amount_response")
        self.label_shortest = QtWidgets.QLabel(self.centralwidget)
        self.label_shortest.setGeometry(QtCore.QRect(40, 90, 181, 17))
        self.label_shortest.setObjectName("label_shortest")
        self.label_longest = QtWidgets.QLabel(self.centralwidget)
        self.label_longest.setGeometry(QtCore.QRect(40, 140, 181, 17))
        self.label_longest.setObjectName("label_longest")
        self.label_average = QtWidgets.QLabel(self.centralwidget)
        self.label_average.setGeometry(QtCore.QRect(40, 190, 181, 17))
        self.label_average.setObjectName("label_average")
        self.label_shortest_response = QtWidgets.QLabel(self.centralwidget)
        self.label_shortest_response.setGeometry(QtCore.QRect(220, 90, 181, 17))
        self.label_shortest_response.setObjectName("label_shortest_response")
        self.label_longest_response = QtWidgets.QLabel(self.centralwidget)
        self.label_longest_response.setGeometry(QtCore.QRect(210, 140, 191, 17))
        self.label_longest_response.setObjectName("label_longest_response")
        self.label_average_response = QtWidgets.QLabel(self.centralwidget)
        self.label_average_response.setGeometry(QtCore.QRect(220, 190, 211, 17))
        self.label_average_response.setObjectName("label_average_response")
        self.label_company_name = QtWidgets.QLabel(self.centralwidget)
        self.label_company_name.setGeometry(QtCore.QRect(30, 250, 121, 17))
        self.label_company_name.setObjectName("label_company_name")
        self.lineEdit_companys_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_companys_name.setGeometry(QtCore.QRect(150, 250, 201, 25))
        self.lineEdit_companys_name.setObjectName("lineEdit_companys_name")
        self.button_statistics = QtWidgets.QPushButton(self.centralwidget)
        self.button_statistics.setGeometry(QtCore.QRect(210, 290, 111, 25))
        self.button_statistics.setObjectName("button_statistics")
        self.label_companys_statistics = QtWidgets.QLabel(self.centralwidget)
        self.label_companys_statistics.setGeometry(QtCore.QRect(130, 10, 141, 17))
        self.label_companys_statistics.setObjectName("label_companys_statistics")
        statistics_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(statistics_window)
        QtCore.QMetaObject.connectSlotsByName(statistics_window)

    def retranslateUi(self, statistics_window):
        _translate = QtCore.QCoreApplication.translate
        statistics_window.setWindowTitle(_translate("statistics_window", "MainWindow"))
        self.button_close.setText(_translate("statistics_window", "close"))
        self.label_movies_amount.setText(_translate("statistics_window", "movies amount:"))
        self.label_amount_response.setText(_translate("statistics_window", "0"))
        self.label_shortest.setText(_translate("statistics_window", "shortest duration movie:"))
        self.label_longest.setText(_translate("statistics_window", "longest duration movie:"))
        self.label_average.setText(_translate("statistics_window", "average movies duration:"))
        self.label_shortest_response.setText(_translate("statistics_window", "0"))
        self.label_longest_response.setText(_translate("statistics_window", "0"))
        self.label_average_response.setText(_translate("statistics_window", "0"))
        self.label_company_name.setText(_translate("statistics_window", "company\'s name"))
        self.button_statistics.setText(_translate("statistics_window", "get statistics"))
        self.label_companys_statistics.setText(_translate("statistics_window", "company\'s statistics"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    statistics_window = QtWidgets.QMainWindow()
    ui = Ui_statistics_window()
    ui.setupUi(statistics_window)
    statistics_window.show()
    sys.exit(app.exec_())

