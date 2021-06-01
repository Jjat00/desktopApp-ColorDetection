from views.mainGUI import MainWindow
from controllers.mainController import MainController

from PySide2 import QtWidgets
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainWindow = MainWindow()

    controller = MainController(mainWindow)

    sys.exit(app.exec_())
