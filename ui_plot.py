# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_plot_ui(object):
    def setupUi(self, plot_ui):
        if not plot_ui.objectName():
            plot_ui.setObjectName(u"plot_ui")
        plot_ui.resize(583, 541)
        self.verticalLayoutWidget = QWidget(plot_ui)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 0, 541, 531))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_out = QLabel(self.verticalLayoutWidget)
        self.label_out.setObjectName(u"label_out")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.label_out.sizePolicy().hasHeightForWidth())
        self.label_out.setSizePolicy(sizePolicy)
        self.label_out.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.label_out)

        self.label_err = QLabel(self.verticalLayoutWidget)
        self.label_err.setObjectName(u"label_err")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_err.sizePolicy().hasHeightForWidth())
        self.label_err.setSizePolicy(sizePolicy1)
        self.label_err.setMinimumSize(QSize(0, 30))
        self.label_err.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout.addWidget(self.label_err)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.curve_plot = PlotWidget(self.verticalLayoutWidget)
        self.curve_plot.setObjectName(u"curve_plot")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.curve_plot.sizePolicy().hasHeightForWidth())
        self.curve_plot.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.curve_plot)


        self.retranslateUi(plot_ui)

        QMetaObject.connectSlotsByName(plot_ui)
    # setupUi

    def retranslateUi(self, plot_ui):
        plot_ui.setWindowTitle(QCoreApplication.translate("plot_ui", u"Form", None))
        self.label_out.setText(QCoreApplication.translate("plot_ui", u"TextLabel", None))
        self.label_err.setText(QCoreApplication.translate("plot_ui", u"TextLabel", None))
    # retranslateUi

