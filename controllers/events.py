from PySide2 import QtWidgets, QtGui, QtCore
import numpy as np
import colorsys
import cv2 

COLOR_START_PROCESS = """
            background: #2BF23F;
            max-height: 40px;
            max-width: 40px;
            border-radius: 20px;
        """

COLOR_STOP_PROCESS = """
            background: #E64C4C;
            max-height: 40px;
            max-width: 40px;
            border-radius: 20px;
        """

class Events():
    def __init__(self, window):
        self.window = window
        self.scala_image = 50
        self.init_values_slider()
        self.init_values_labels()

        self.clicked_load_button = False
        self.clicked_init_process = False

    def get_path_image(self):
        path_image = QtWidgets.QFileDialog.getOpenFileName(
            self.window.frame_image, "Select Image", dir="./", filter="Images (*.png *.jpg)"
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

            self.clicked_load_button = True
            
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
        if self.clicked_load_button:
            self.timer = QtCore.QTimer()
            self.timer.setInterval(50)
            self.timer.timeout.connect(self.get_frame)
            self.timer.start()

            self.scene_image_thresh = QtWidgets.QGraphicsView()
            scene = QtWidgets.QGraphicsScene()
            self.image_pixmap = QtGui.QPixmap(*self.dimensions_image)
            self.image_pixmap_item = scene.addPixmap(self.image_pixmap)
            self.scene_image_thresh.setScene(scene)

            self.clear_layout_image()
            self.window.layout_image.addWidget(self.scene_image_thresh)

            self.clicked_init_process = True
            self.window.state_process.setStyleSheet(COLOR_START_PROCESS)


    def get_frame(self):
        self.get_values_sliders()

        frame = self.image_resize(self.image_thresh)
        image = QtGui.QImage(frame, *self.dimensions_image,QtGui.QImage.Format_RGB888).rgbSwapped()
        self.image_pixmap = QtGui.QPixmap.fromImage(image)
        self.image_pixmap_item.setPixmap(self.image_pixmap)


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
        self.hue_min = self.window.slider_hue_min.value()
        self.hue_max = self.window.slider_hue_max.value()
        self.sat_min = self.window.slider_sat_min.value()
        self.sat_max = self.window.slider_sat_max.value()
        self.value_min = self.window.slider_value_min.value()
        self.value_max = self.window.slider_value_max.value()

        #print("hue min: %i, self.hue_max: %i" % (self.hue_min, self.hue_max))
        lower = np.array([self.hue_min, self.sat_min, self.value_min])
        upper = np.array([self.hue_max, self.sat_max, self.value_max])

        mask = cv2.inRange(self.img_hsv, lower, upper)

        self.image_thresh = cv2.bitwise_and(self.image, self.image, mask=mask)

        self.set_text_labels()

    def init_values_labels(self):
        self.window.label_hue_min.setText(str(0))
        self.window.label_hue_max.setText(str(179))
        self.window.label_sat_min.setText(str(0))
        self.window.label_sat_max.setText(str(255))
        self.window.label_val_min.setText(str(0))
        self.window.label_val_max.setText(str(255))

        self.window.label_r_min.setText(str(0))
        self.window.label_g_min.setText(str(0))
        self.window.label_b_min.setText(str(0))

        self.window.label_r_max.setText(str(0))
        self.window.label_g_max.setText(str(0))
        self.window.label_b_max.setText(str(0))


    def set_text_labels(self):
        self.window.label_hue_min.setText(str(self.hue_min))
        self.window.label_hue_max.setText(str(self.hue_max))
        self.window.label_sat_min.setText(str(self.sat_min))
        self.window.label_sat_max.setText(str(self.sat_max))
        self.window.label_val_min.setText(str(self.value_min))
        self.window.label_val_max.setText(str(self.value_max))

        r, g, b = colorsys.hsv_to_rgb(self.hue_min / 179, self.sat_min / 255, self.value_min /255 )
        self.window.label_r_min.setText(str(int(r*255)))
        self.window.label_g_min.setText(str(int(g*255)))
        self.window.label_b_min.setText(str(int(b*255)))

        r, g, b = colorsys.hsv_to_rgb(self.hue_max / 179, self.sat_max / 255, self.value_max /255 )
        self.window.label_r_max.setText(str(int(r*255)))
        self.window.label_g_max.setText(str(int(g*255)))
        self.window.label_b_max.setText(str(int(b*255)))


    def stop_dection(self):
        if self.clicked_init_process:
            self.timer.stop()
            self.window.state_process.setStyleSheet(COLOR_STOP_PROCESS)


    def new_process(self):
        self.clicked_load_button = False
        self.clicked_init_process = False
        self.clear_layout_image()

    def clear_layout_image(self):
        for index in reversed(range(self.window.layout_image.count())):
            layoutItem = self.window.layout_image.itemAt(index)
            widgetToRemove = layoutItem.widget()
            print("found widget: " + str(widgetToRemove))
            widgetToRemove.setParent(None)
            self.window.layout_image.removeWidget(widgetToRemove)    
        