from PySide2 import QtGui, QtCore

class StylesMainWindow():
    def __init__(self, mainWindow):
        self.widget = mainWindow
        self.window = self.widget.window
        self.set_colors()
        self.set_theme()
        self.set_icons()

    def set_colors(self):
        self.hover_button = '#8DDBE0'
        self.background = '#202020'
        self.buttons = '#708D81'
        self.frame_image = '#4B5043'
        self.primaryText = '#9BC4BC'
        self.secondaryText = '#D3FFE9'

    def set_icons(self):
        self.window.button_load_image.setIcon(
            QtGui.QPixmap('./views/icons/upload-button.png'))
        self.window.button_load_image.setIconSize(QtCore.QSize(25, 25))
        self.window.button_load_image.setToolTip('load image')

        self.window.button_start.setIcon(
            QtGui.QPixmap('./views/icons/play.png'))
        self.window.button_start.setIconSize(QtCore.QSize(25, 25))
        self.window.button_start.setToolTip('start color detection')

        self.window.button_stop.setIcon(
            QtGui.QPixmap('./views/icons/stop.png'))
        self.window.button_stop.setIconSize(QtCore.QSize(25, 25))
        self.window.button_stop.setToolTip('stop color dection')

        self.window.button_new.setIcon(
            QtGui.QPixmap('./views/icons/reload.png'))
        self.window.button_new.setIconSize(QtCore.QSize(25, 25))
        self.window.button_new.setToolTip('new color detection')        

    def set_theme(self):
        styleWindow = """
            QWidget{
                background: """ + self.background + """;
                color:  """ + self.primaryText + """;
                border: none;
                font: Ubuntu;
                font-size: 12pt;
            }
            QPushButton{
                Background: """ + self.buttons + """;
                min-height: 40px;
                border-radius: 2px;
            }       
            QPushButton:pressed {
                background-color: rgb(30, 30, 30);
                border-style: inset;
            } 
            QPushButton:hover {
                background-color: """+self.hover_button+""";
                border-style: inset;
            } 
            QLabel {
                color: """+self.secondaryText + """;
                font-size: 11pt;
            }              
        """
        self.widget.setStyleSheet(styleWindow)


        style_frame_image = """
            background: """ + self.frame_image + """;
        """

        self.window.frame_image.setStyleSheet(style_frame_image)

        style_state_process = """
            background: #E64C4C;
            max-height: 40px;
            max-width: 40px;
            border-radius: 20px;
        """

        self.widget.window.state_process.setStyleSheet(style_state_process)

