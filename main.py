import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from server import server
from views.main import lxy_mainwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = lxy_mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())