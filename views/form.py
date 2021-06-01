# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(788, 442)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(-290, 120, 160, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_image = QFrame(Form)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setGeometry(QRect(10, 30, 531, 321))
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.frame_image)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 531, 321))
        self.layout_image = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.layout_image.setObjectName(u"layout_image")
        self.layout_image.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 370, 320, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.button_load_image = QPushButton(self.horizontalLayoutWidget)
        self.button_load_image.setObjectName(u"button_load_image")

        self.horizontalLayout.addWidget(self.button_load_image)

        self.button_start = QPushButton(self.horizontalLayoutWidget)
        self.button_start.setObjectName(u"button_start")

        self.horizontalLayout.addWidget(self.button_start)

        self.button_stop = QPushButton(self.horizontalLayoutWidget)
        self.button_stop.setObjectName(u"button_stop")

        self.horizontalLayout.addWidget(self.button_stop)

        self.button_new = QPushButton(self.horizontalLayoutWidget)
        self.button_new.setObjectName(u"button_new")

        self.horizontalLayout.addWidget(self.button_new)

        self.verticalLayoutWidget_2 = QWidget(Form)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(560, 40, 160, 278))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.slider_hue_min = QSlider(self.verticalLayoutWidget_2)
        self.slider_hue_min.setObjectName(u"slider_hue_min")
        self.slider_hue_min.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_hue_min)

        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.slider_hue_max = QSlider(self.verticalLayoutWidget_2)
        self.slider_hue_max.setObjectName(u"slider_hue_max")
        self.slider_hue_max.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_hue_max)

        self.label_3 = QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.slider_sat_min = QSlider(self.verticalLayoutWidget_2)
        self.slider_sat_min.setObjectName(u"slider_sat_min")
        self.slider_sat_min.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_sat_min)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.slider_sat_max = QSlider(self.verticalLayoutWidget_2)
        self.slider_sat_max.setObjectName(u"slider_sat_max")
        self.slider_sat_max.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_sat_max)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.slider_value_min = QSlider(self.verticalLayoutWidget_2)
        self.slider_value_min.setObjectName(u"slider_value_min")
        self.slider_value_min.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_value_min)

        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)

        self.slider_value_max = QSlider(self.verticalLayoutWidget_2)
        self.slider_value_max.setObjectName(u"slider_value_max")
        self.slider_value_max.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.slider_value_max)

        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(560, 330, 160, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_g_max = QLabel(self.gridLayoutWidget)
        self.label_g_max.setObjectName(u"label_g_max")

        self.gridLayout.addWidget(self.label_g_max, 2, 3, 1, 1)

        self.label_r_min = QLabel(self.gridLayoutWidget)
        self.label_r_min.setObjectName(u"label_r_min")

        self.gridLayout.addWidget(self.label_r_min, 1, 2, 1, 1)

        self.label_b_max = QLabel(self.gridLayoutWidget)
        self.label_b_max.setObjectName(u"label_b_max")

        self.gridLayout.addWidget(self.label_b_max, 3, 3, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 1, 1, 1, 1)

        self.label_g_min = QLabel(self.gridLayoutWidget)
        self.label_g_min.setObjectName(u"label_g_min")

        self.gridLayout.addWidget(self.label_g_min, 2, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 3, 1, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_r_max = QLabel(self.gridLayoutWidget)
        self.label_r_max.setObjectName(u"label_r_max")

        self.gridLayout.addWidget(self.label_r_max, 1, 3, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout.addWidget(self.label_15, 0, 2, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout.addWidget(self.label_16, 0, 3, 1, 1)

        self.label_b_min = QLabel(self.gridLayoutWidget)
        self.label_b_min.setObjectName(u"label_b_min")

        self.gridLayout.addWidget(self.label_b_min, 3, 2, 1, 1)

        self.state_process = QPushButton(Form)
        self.state_process.setObjectName(u"state_process")
        self.state_process.setGeometry(QRect(380, 370, 75, 23))
        self.label_hue_min = QLabel(Form)
        self.label_hue_min.setObjectName(u"label_hue_min")
        self.label_hue_min.setGeometry(QRect(730, 60, 47, 13))
        self.label_hue_max = QLabel(Form)
        self.label_hue_max.setObjectName(u"label_hue_max")
        self.label_hue_max.setGeometry(QRect(730, 100, 47, 13))
        self.label_sat_min = QLabel(Form)
        self.label_sat_min.setObjectName(u"label_sat_min")
        self.label_sat_min.setGeometry(QRect(730, 150, 47, 13))
        self.label_sat_max = QLabel(Form)
        self.label_sat_max.setObjectName(u"label_sat_max")
        self.label_sat_max.setGeometry(QRect(730, 200, 47, 13))
        self.label_val_min = QLabel(Form)
        self.label_val_min.setObjectName(u"label_val_min")
        self.label_val_min.setGeometry(QRect(730, 250, 47, 13))
        self.label_val_max = QLabel(Form)
        self.label_val_max.setObjectName(u"label_val_max")
        self.label_val_max.setGeometry(QRect(730, 300, 47, 13))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.button_load_image.setText("")
        self.button_start.setText("")
        self.button_stop.setText("")
        self.button_new.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"hue min:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"hue max:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"saturation min:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"saturation max:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"value min:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"value max:", None))
        self.label_g_max.setText("")
        self.label_r_min.setText("")
        self.label_b_max.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"R:", None))
        self.label_g_min.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"B:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"G:", None))
        self.label_r_max.setText("")
        self.label_15.setText(QCoreApplication.translate("Form", u"Min", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Max", None))
        self.label_b_min.setText("")
        self.state_process.setText("")
        self.label_hue_min.setText("")
        self.label_hue_max.setText("")
        self.label_sat_min.setText("")
        self.label_sat_max.setText("")
        self.label_val_min.setText("")
        self.label_val_max.setText("")
    # retranslateUi

