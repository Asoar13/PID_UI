# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(503, 261)
        self.verticalLayoutWidget_3 = QWidget(Form)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 10, 231, 221))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_port = QLabel(self.verticalLayoutWidget_3)
        self.label_port.setObjectName(u"label_port")
        font = QFont()
        font.setPointSize(11)
        self.label_port.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_port)

        self.le_port = QLineEdit(self.verticalLayoutWidget_3)
        self.le_port.setObjectName(u"le_port")

        self.horizontalLayout_2.addWidget(self.le_port)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_baud = QLabel(self.verticalLayoutWidget_3)
        self.label_baud.setObjectName(u"label_baud")
        self.label_baud.setFont(font)

        self.horizontalLayout.addWidget(self.label_baud)

        self.le_baud = QLineEdit(self.verticalLayoutWidget_3)
        self.le_baud.setObjectName(u"le_baud")

        self.horizontalLayout.addWidget(self.le_baud)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_connect = QPushButton(self.verticalLayoutWidget_3)
        self.btn_connect.setObjectName(u"btn_connect")

        self.verticalLayout_2.addWidget(self.btn_connect)

        self.btn_disconnect = QPushButton(self.verticalLayoutWidget_3)
        self.btn_disconnect.setObjectName(u"btn_disconnect")

        self.verticalLayout_2.addWidget(self.btn_disconnect)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_show_curve = QPushButton(self.verticalLayoutWidget_3)
        self.btn_show_curve.setObjectName(u"btn_show_curve")
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_show_curve.setFont(font1)

        self.verticalLayout_16.addWidget(self.btn_show_curve)

        self.label_cur_status = QLabel(self.verticalLayoutWidget_3)
        self.label_cur_status.setObjectName(u"label_cur_status")

        self.verticalLayout_16.addWidget(self.label_cur_status)


        self.horizontalLayout_9.addLayout(self.verticalLayout_16)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lable_target = QLabel(self.verticalLayoutWidget_3)
        self.lable_target.setObjectName(u"lable_target")
        self.lable_target.setFont(font1)

        self.horizontalLayout_5.addWidget(self.lable_target)

        self.le_target = QLineEdit(self.verticalLayoutWidget_3)
        self.le_target.setObjectName(u"le_target")
        self.le_target.setFont(font1)

        self.horizontalLayout_5.addWidget(self.le_target)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.slider_target = QSlider(self.verticalLayoutWidget_3)
        self.slider_target.setObjectName(u"slider_target")
        self.slider_target.setMaximum(1000)
        self.slider_target.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout_6.addWidget(self.slider_target)


        self.horizontalLayout_6.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_click_update = QPushButton(self.verticalLayoutWidget_3)
        self.btn_click_update.setObjectName(u"btn_click_update")

        self.verticalLayout_7.addWidget(self.btn_click_update)

        self.btn_auto_update = QPushButton(self.verticalLayoutWidget_3)
        self.btn_auto_update.setObjectName(u"btn_auto_update")

        self.verticalLayout_7.addWidget(self.btn_auto_update)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalLayoutWidget_4 = QWidget(Form)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(270, 10, 211, 224))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_kp = QLabel(self.verticalLayoutWidget_4)
        self.label_kp.setObjectName(u"label_kp")
        self.label_kp.setFont(font1)

        self.verticalLayout_13.addWidget(self.label_kp)

        self.le_kp = QLineEdit(self.verticalLayoutWidget_4)
        self.le_kp.setObjectName(u"le_kp")
        self.le_kp.setFont(font1)

        self.verticalLayout_13.addWidget(self.le_kp)


        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.btn_kp_add = QPushButton(self.verticalLayoutWidget_4)
        self.btn_kp_add.setObjectName(u"btn_kp_add")
        self.btn_kp_add.setFont(font)

        self.verticalLayout_14.addWidget(self.btn_kp_add)

        self.btn_kp_sub = QPushButton(self.verticalLayoutWidget_4)
        self.btn_kp_sub.setObjectName(u"btn_kp_sub")
        self.btn_kp_sub.setFont(font)

        self.verticalLayout_14.addWidget(self.btn_kp_sub)


        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_kp_jump = QLabel(self.verticalLayoutWidget_4)
        self.label_kp_jump.setObjectName(u"label_kp_jump")
        self.label_kp_jump.setMaximumSize(QSize(100, 100))
        self.label_kp_jump.setFont(font)

        self.verticalLayout_15.addWidget(self.label_kp_jump)

        self.le_kp_jump = QLineEdit(self.verticalLayoutWidget_4)
        self.le_kp_jump.setObjectName(u"le_kp_jump")
        self.le_kp_jump.setFont(font)

        self.verticalLayout_15.addWidget(self.le_kp_jump)


        self.horizontalLayout_8.addLayout(self.verticalLayout_15)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_ki = QLabel(self.verticalLayoutWidget_4)
        self.label_ki.setObjectName(u"label_ki")
        self.label_ki.setFont(font1)

        self.verticalLayout_10.addWidget(self.label_ki)

        self.le_ki = QLineEdit(self.verticalLayoutWidget_4)
        self.le_ki.setObjectName(u"le_ki")
        self.le_ki.setFont(font1)

        self.verticalLayout_10.addWidget(self.le_ki)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.btn_ki_add = QPushButton(self.verticalLayoutWidget_4)
        self.btn_ki_add.setObjectName(u"btn_ki_add")
        self.btn_ki_add.setFont(font)

        self.verticalLayout_11.addWidget(self.btn_ki_add)

        self.btn_ki_sub = QPushButton(self.verticalLayoutWidget_4)
        self.btn_ki_sub.setObjectName(u"btn_ki_sub")
        self.btn_ki_sub.setFont(font)

        self.verticalLayout_11.addWidget(self.btn_ki_sub)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_ki_jump = QLabel(self.verticalLayoutWidget_4)
        self.label_ki_jump.setObjectName(u"label_ki_jump")
        self.label_ki_jump.setMaximumSize(QSize(100, 100))
        self.label_ki_jump.setFont(font)

        self.verticalLayout_12.addWidget(self.label_ki_jump)

        self.le_ki_jump = QLineEdit(self.verticalLayoutWidget_4)
        self.le_ki_jump.setObjectName(u"le_ki_jump")
        self.le_ki_jump.setFont(font)

        self.verticalLayout_12.addWidget(self.le_ki_jump)


        self.horizontalLayout_7.addLayout(self.verticalLayout_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_kd = QLabel(self.verticalLayoutWidget_4)
        self.label_kd.setObjectName(u"label_kd")
        self.label_kd.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_kd)

        self.le_kd = QLineEdit(self.verticalLayoutWidget_4)
        self.le_kd.setObjectName(u"le_kd")
        self.le_kd.setFont(font1)

        self.verticalLayout_5.addWidget(self.le_kd)


        self.horizontalLayout_4.addLayout(self.verticalLayout_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_kd_add = QPushButton(self.verticalLayoutWidget_4)
        self.btn_kd_add.setObjectName(u"btn_kd_add")
        self.btn_kd_add.setFont(font)

        self.verticalLayout_9.addWidget(self.btn_kd_add)

        self.btn_kd_sub = QPushButton(self.verticalLayoutWidget_4)
        self.btn_kd_sub.setObjectName(u"btn_kd_sub")
        self.btn_kd_sub.setFont(font)

        self.verticalLayout_9.addWidget(self.btn_kd_sub)


        self.horizontalLayout_4.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_kd_jump = QLabel(self.verticalLayoutWidget_4)
        self.label_kd_jump.setObjectName(u"label_kd_jump")
        self.label_kd_jump.setMaximumSize(QSize(100, 100))
        self.label_kd_jump.setFont(font)

        self.verticalLayout_8.addWidget(self.label_kd_jump)

        self.le_kd_jump = QLineEdit(self.verticalLayoutWidget_4)
        self.le_kd_jump.setObjectName(u"le_kd_jump")
        self.le_kd_jump.setFont(font)

        self.verticalLayout_8.addWidget(self.le_kd_jump)


        self.horizontalLayout_4.addLayout(self.verticalLayout_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(250, 0, 20, 251))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_port.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3", None))
        self.le_port.setText(QCoreApplication.translate("Form", u"COM9", None))
        self.label_baud.setText(QCoreApplication.translate("Form", u"\u6ce2\u7279\u7387", None))
        self.le_baud.setText(QCoreApplication.translate("Form", u"115200", None))
        self.btn_connect.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5\u4e32\u53e3", None))
        self.btn_disconnect.setText(QCoreApplication.translate("Form", u"\u65ad\u5f00\u8fde\u63a5", None))
        self.btn_show_curve.setText(QCoreApplication.translate("Form", u"\u663e\u793a\u66f2\u7ebf\u7a97\u53e3", None))
        self.label_cur_status.setText(QCoreApplication.translate("Form", u"--\u672a\u8fde\u63a5--", None))
        self.lable_target.setText(QCoreApplication.translate("Form", u"Target", None))
        self.le_target.setText(QCoreApplication.translate("Form", u"150", None))
        self.btn_click_update.setText(QCoreApplication.translate("Form", u"\u624b\u52a8\u66f4\u65b0", None))
        self.btn_auto_update.setText(QCoreApplication.translate("Form", u"\u5b9e\u65f6\u66f4\u65b0", None))
        self.label_kp.setText(QCoreApplication.translate("Form", u"Kp", None))
        self.le_kp.setText(QCoreApplication.translate("Form", u"1.5", None))
        self.btn_kp_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.btn_kp_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_kp_jump.setText(QCoreApplication.translate("Form", u"\u8df3\u53d8\u503c", None))
        self.le_kp_jump.setText(QCoreApplication.translate("Form", u"0.1", None))
        self.label_ki.setText(QCoreApplication.translate("Form", u"Ki", None))
        self.le_ki.setText(QCoreApplication.translate("Form", u"0.5", None))
        self.btn_ki_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.btn_ki_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_ki_jump.setText(QCoreApplication.translate("Form", u"\u8df3\u53d8\u503c", None))
        self.le_ki_jump.setText(QCoreApplication.translate("Form", u"0.1", None))
        self.label_kd.setText(QCoreApplication.translate("Form", u"Kd", None))
        self.le_kd.setText(QCoreApplication.translate("Form", u"0.1", None))
        self.btn_kd_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.btn_kd_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.label_kd_jump.setText(QCoreApplication.translate("Form", u"\u8df3\u53d8\u503c", None))
        self.le_kd_jump.setText(QCoreApplication.translate("Form", u"0.1", None))
    # retranslateUi

