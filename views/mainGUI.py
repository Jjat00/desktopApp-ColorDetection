from PySide2 import QtWidgets, QtCore, QtUiTools
from views.styles import StylesMainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.load_form()
        self.initUI()
        StylesMainWindow(self)

    def initUI(self):
        self.setWindowTitle("Color Dection")
        self.setGeometry(300, 100, 788, 442)


    def load_form(self):
        file = QtCore.QFile("./views/form.ui")
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader(file)
        self.window = loader.load(file)
        self.setCentralWidget(self.window)

