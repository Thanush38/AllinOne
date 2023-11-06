from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys
from pathlib import Path
from PIL import Image


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.convertLabel = QLabel(parent=Form)
        self.convertLabel.setGeometry(QtCore.QRect(210, 70, 131, 16))
        self.convertLabel.setObjectName("convertLabel")
        self.horizontalLayoutWidget = QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 491, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.Location = QHBoxLayout(self.horizontalLayoutWidget)
        self.Location.setContentsMargins(0, 0, 0, 0)
        self.Location.setObjectName("Location")
        self.LocationLabel = QLabel(parent=self.horizontalLayoutWidget)
        self.LocationLabel.setObjectName("LocationLabel")
        self.Location.addWidget(self.LocationLabel)
        self.LocationInput = QLineEdit(parent=self.horizontalLayoutWidget)
        self.LocationInput.setObjectName("LocationInput")
        self.Location.addWidget(self.LocationInput)
        self.Locationbtn = QPushButton(parent=self.horizontalLayoutWidget)
        self.Locationbtn.setObjectName("Locationbtn")
        self.Locationbtn.clicked.connect(self.openDir)
        self.Location.addWidget(self.Locationbtn)
        self.comboBox = QComboBox(parent=Form)
        self.options = ["jpeg", "png", "pdf", "jpg", "ico"]
        self.comboBox.addItems(self.options)
        self.comboBox.setGeometry(QtCore.QRect(110, 175, 104, 26))
        self.comboBox.setObjectName("comboBox")
        self.label = QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(30, 150, 72, 68))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QWidget(parent=Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 190, 491, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.Location_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.Location_2.setContentsMargins(0, 0, 0, 0)
        self.Location_2.setObjectName("Location_2")
        self.SaveLocation = QLabel(parent=self.horizontalLayoutWidget_2)
        self.SaveLocation.setObjectName("SaveLocation")
        self.Location_2.addWidget(self.SaveLocation)
        self.SaveInput = QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.SaveInput.setObjectName("SaveInput")
        self.Location_2.addWidget(self.SaveInput)
        self.Savebtn = QPushButton(parent=self.horizontalLayoutWidget_2)
        self.Savebtn.setObjectName("Savebtn")
        self.Savebtn.clicked.connect(self.saveDir)
        self.Location_2.addWidget(self.Savebtn)
        self.Convertbtn = QPushButton(parent=Form)
        self.Convertbtn.setGeometry(QtCore.QRect(50, 275, 400, 32))
        self.Convertbtn.setObjectName("Convertbtn")
        self.Convertbtn.clicked.connect(self.convert)
        self.convertDone = QLabel(parent=Form)
        self.convertDone.setGeometry(QtCore.QRect(190, 320, 211, 16))
        self.convertDone.setObjectName("convertDone")
        self.convertDone.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.convertLabel.setText(_translate("Form", "File Convertor"))
        self.LocationLabel.setText(_translate("Form", "File Location:"))
        self.Locationbtn.setText(_translate("Form", "Browse"))
        self.label.setText(_translate("Form", "Convert To:"))
        self.SaveLocation.setText(_translate("Form", "Save To:"))
        self.Savebtn.setText(_translate("Form", "Browse"))
        self.Convertbtn.setText(_translate("Form", "Convert"))
        self.convertDone.setText(_translate("Form", "Conversion Done"))
    
    def openDir(self):
        print("open Dir clicked")
        folder = QFileDialog.getOpenFileName(None,"Open File", "","JPEG (*.jpg *.jpeg);;PNG (*.png);;ico (*.ico)")
        
        print(folder[0])   
        fileName = folder[0]
        if folder:
            path = Path(fileName)
            self.LocationInput.setText(str(path))
            print(path)

    def saveDir(self):
        print("save Dir clicked")
        folder = QFileDialog.getExistingDirectory()
        if folder:
            path = Path(folder)
            self.SaveInput.setText(str(path))
            print(path)

   

    def convert(self):
        try:
            imagepath = self.SaveInput.text()
            fileType = self.comboBox.currentText()
            image = Image.open(self.LocationInput.text())
            image = image.convert('RGB')
            image.save(f"{imagepath}/converted.{fileType}")
            self.convertDone.show()
        except:
            print("Error")
   

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
