from controllers.events import Events

class MainController():
    def __init__(self, mainWindow):
        self.window = mainWindow.window
        self.events = Events(self.window)

        self.connect_buttons()
        mainWindow.show()

    def connect_buttons(self):
        self.window.button_load_image.clicked.connect(self.events.load_image)
        self.window.button_start.clicked.connect(self.events.init_dection)
        self.window.button_stop.clicked.connect(self.events.stop_dection)
        self.window.button_new.clicked.connect(self.events.new_process)
