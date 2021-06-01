from PySide2 import QtWidgets, QtCore, QtUiTools

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.load_form()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Color Dection")
        self.setGeometry(300, 100, 654, 441)


    def load_form(self):
        file = QtCore.QFile("./views/form.ui")
        file.open(QtCore.QFile.ReadOnly)
        loader = QtUiTools.QUiLoader(file)
        self.window = loader.load(file)
        self.setCentralWidget(self.window)

