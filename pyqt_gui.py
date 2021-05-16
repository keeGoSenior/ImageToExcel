# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageToExcel.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 260)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(61, 62, 61);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_link_Edit = QtWidgets.QLineEdit(self.centralwidget)
        self.image_link_Edit.setGeometry(QtCore.QRect(95, 9, 181, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.image_link_Edit.setFont(font)
        self.image_link_Edit.setStyleSheet("background-color: rgb(255, 255, 255);gridline-color: rgb(255, 255, 67);\n"
"selection-color: rgb(69, 255, 178);")
        self.image_link_Edit.setInputMask("")
        self.image_link_Edit.setText("")
        self.image_link_Edit.setObjectName("image_link_Edit")
        self.imagelink_label = QtWidgets.QLabel(self.centralwidget)
        self.imagelink_label.setGeometry(QtCore.QRect(0, 9, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.imagelink_label.setFont(font)
        self.imagelink_label.setStyleSheet("color: rgb(184, 184, 134);")
        self.imagelink_label.setAlignment(QtCore.Qt.AlignCenter)
        self.imagelink_label.setObjectName("imagelink_label")
        self.xlsx_file_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.xlsx_file_edit.setGeometry(QtCore.QRect(120, 209, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.xlsx_file_edit.setFont(font)
        self.xlsx_file_edit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.xlsx_file_edit.setInputMask("")
        self.xlsx_file_edit.setObjectName("xlsx_file_edit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(5, 209, 111, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(184, 184, 134);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.made_by_label = QtWidgets.QLabel(self.centralwidget)
        self.made_by_label.setGeometry(QtCore.QRect(0, 239, 341, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.made_by_label.setFont(font)
        self.made_by_label.setStyleSheet("color: rgb(110, 111, 86);")
        self.made_by_label.setAlignment(QtCore.Qt.AlignCenter)
        self.made_by_label.setObjectName("made_by_label")
        self.image_show_label = QtWidgets.QLabel(self.centralwidget)
        self.image_show_label.setGeometry(QtCore.QRect(0, 40, 341, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.image_show_label.setFont(font)
        self.image_show_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_show_label.setObjectName("image_show_label")
        self.transform_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.transform_buttom.setGeometry(QtCore.QRect(254, 210, 87, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.transform_buttom.setFont(font)
        self.transform_buttom.setStyleSheet("color: rgb(184, 184, 134);background-color: rgb(75, 76, 75);\n"
"alternate-background-color: rgb(69, 70, 69);")
        self.transform_buttom.setObjectName("transform_buttom")
        self.unpload_buttom = QtWidgets.QPushButton(self.centralwidget)
        self.unpload_buttom.setGeometry(QtCore.QRect(280, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.unpload_buttom.setFont(font)
        self.unpload_buttom.setStyleSheet("color: rgb(184, 184, 134);background-color: rgb(75, 76, 75);\n"
"alternate-background-color: rgb(69, 70, 69);")
        self.unpload_buttom.setObjectName("unpload_buttom")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ImageToExcel"))
        self.image_link_Edit.setPlaceholderText(_translate("MainWindow", "C:\\folder\\image.jpg"))
        self.imagelink_label.setText(_translate("MainWindow", "Image link:"))
        self.xlsx_file_edit.setPlaceholderText(_translate("MainWindow", "Example"))
        self.label_2.setText(_translate("MainWindow", ".xlsx file name:"))
        self.made_by_label.setText(_translate("MainWindow", "Made by github/KeeGoSenior"))
        self.image_show_label.setText(_translate("MainWindow", "🖼️"))
        self.transform_buttom.setText(_translate("MainWindow", "Transform"))
        self.unpload_buttom.setText(_translate("MainWindow", "Upload"))

    def add_functions(self):
        pass

    def image_show(self, ):
        pass

    def image_upload(self):
        pass

    def transform(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
