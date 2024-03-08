# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(400, 157)
        Error.setStyleSheet(u"background-color:#16191d;")
        self.label = QLabel(Error)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 40, 321, 41))
        font = QFont()
        font.setFamilies([u"MS Sans Serif"])
        font.setPointSize(18)
        self.label.setFont(font)
        Error.setModal(True)
        self.label.setStyleSheet(u"color:white;")
        self.label.setAlignment(Qt.AlignCenter)
        self.ok_button = QPushButton(Error)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setGeometry(QRect(130, 100, 131, 41))
        font1 = QFont()
        font1.setFamilies([u"MS Sans Serif"])
        font1.setBold(False)
        self.ok_button.setFont(font1)
        self.ok_button.setStyleSheet(u"QPushButton{\n"
"border-radius: 10px;\n"
"font-size: 28px;\n"
"border: 2px solid rgba(255,255,255,40);\n"
"\n"
"color: white;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255,255,255,60);\n"
"color:white;\n"
"}")
        self.frame = QFrame(Error)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-1, -1, 401, 161))
        self.frame.setStyleSheet(u"border-radius:5px;\n"
"border: 5px solid rgba(255,255,255,40);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.raise_()
        self.label.raise_()
        self.ok_button.raise_()

        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"Error", None))
        self.label.setText(QCoreApplication.translate("Error", u"Connection failed", None))
        self.ok_button.setText(QCoreApplication.translate("Error", u"Ok", None))
    # retranslateUi

