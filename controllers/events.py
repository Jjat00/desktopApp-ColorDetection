from PySide2 import QtWidgets, QtGui, QtCore
import numpy as np
import cv2 

class Events():
    def __init__(self, window):
        self.window = window
        self.scala_image = 50
        self.init_values_slider()

    def get_path_image(self):
        path_image = QtWidgets.QFileDialog.getOpenFileName(
            self.window, "Select Image", dir="./", filter="Images (*.png *.jpg)"
        )
        path_image, _ = path_image
        return path_image

    def load_image(self):
        print("load image....")
        path_image = self.get_path_image()
        try:
            if len(path_image) == 0:
                raise ValueError("no se puede ingresar un path vacio")

            self.image = cv2.imread(path_image)
            self.img_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

            scene_image = self.image_to_scene(self.image)
            self.window.layout_image.addWidget(scene_image)
            
        except ValueError as ve:
            print(ve)

    def image_to_scene(self, frame):
        frame = self.image_resize(frame)
        image = QtGui.QImage(frame, *self.dimensions_image,
                             QtGui.QImage.Format_RGB888).rgbSwapped()
        image_pixmap = QtGui.QPixmap.fromImage(image)
        framePixmap = QtGui.QPixmap(*self.dimensions_image)
        imageScene = QtWidgets.QGraphicsScene()
        imageScene.addPixmap(image_pixmap)
        scene_image = QtWidgets.QGraphicsView()
        scene_image.setScene(imageScene)
        return scene_image    


    def image_resize(self, pathImage):
        if (isinstance(pathImage, str)):
            image = cv2.imread(pathImage, cv2.IMREAD_UNCHANGED)
        else:
            image = pathImage
        height,  width = image.shape[:2]
        scala = self.scala_image / 100
        self.dimensions_image =  [int(i) for i in np.array([width, height])*scala]
        self.dimensions_image = self.to_odd(self.dimensions_image)
        resized = cv2.resize(image, (self.dimensions_image[0], self.dimensions_image[1]),
          interpolation=cv2.INTER_AREA)
        return resized

    def to_odd(self, list):
        new_list = []
        for i in list:
            if i % 2 == 0:
                new_list.append(i)
            else:
                i += 1
                new_list.append(i)
        return new_list


    def init_dection(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.get_frame)
        self.timer.start()


    def get_frame(self):
        self.get_values_sliders()


    def init_values_slider(self):
        self.window.slider_hue_min.setMaximum(179)
        self.window.slider_hue_min.setValue(0)
        self.window.slider_hue_max.setMaximum(179)
        self.window.slider_hue_max.setValue(179)

        self.window.slider_sat_min.setMaximum(255)
        self.window.slider_sat_min.setValue(0)
        self.window.slider_sat_max.setMaximum(255)
        self.window.slider_sat_max.setValue(255)

        self.window.slider_value_min.setMaximum(255)
        self.window.slider_value_min.setValue(0)
        self.window.slider_value_max.setMaximum(255)
        self.window.slider_value_max.setValue(255)        

    def get_values_sliders(self):
        hue_min = self.window.slider_hue_min.value()
        hue_max = self.window.slider_hue_max.value()
        sat_min = self.window.slider_sat_min.value()
        sat_max = self.window.slider_sat_max.value()
        value_min = self.window.slider_value_min.value()
        value_max = self.window.slider_value_max.value()

        print("hue min: %i, hue_max: %i" % (hue_min, hue_max))

        lower = np.array([hue_min, sat_min, value_min])
        upper = np.array([hue_max, sat_max, value_max])

        mask = cv2.inRange(self.img_hsv, lower, upper)

        image_thresh = cv2.bitwise_and(self.image, self.image, mask=mask)

        cv2.imshow('image_thresh', image_thresh)

    def stop_dection(self):
        self.timer.stop()