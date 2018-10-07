
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from src.menu_window import *

app = None
window = None


def start_app():
    print("...")
    create_menu()

def init_window_manager():
    global app
    global window
    app = QtWidgets.QApplication( sys.argv )
    window = QtWidgets.QMainWindow()

