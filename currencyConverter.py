# This is the widget for the currency converter that uses the currencyapicom client

from PyQt6 import QtCore, QtGui, QtWidgets
import currencyapicom 
from datetime import date

class Ui_Form(object):
    def setupUi(self, Form):
        # setting up base form and getting data from api
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.response = self.getData()
        self.data = self.response.currencies()
        self.cur = self.getAllCurrencies(self.data["data"])
        self.cur.sort()
        # label for the window
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(170, 120, 191, 16))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 150, 220, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        #  layout for the convert from box
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #  convert from label
        self.convertFromLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.convertFromLabel.setObjectName("convertFromLabel")
        self.horizontalLayout.addWidget(self.convertFromLabel)
        #  convert from box
        self.convertFromBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget)
        self.convertFromBox.setObjectName("convertFromBox")
        self.convertFromBox.addItems(self.cur)
        self.horizontalLayout.addWidget(self.convertFromBox)
        #  convert from amount layout
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 180, 201, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        #  convert from amount input
        self.ConvertFromAmount = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.ConvertFromAmount.setObjectName("ConvertFromAmount")
        self.ConvertFromAmount.validator = QtGui.QDoubleValidator()
        self.ConvertFromAmount.textChanged.connect(self.convert)
        self.horizontalLayout_2.addWidget(self.ConvertFromAmount)
        #  convert button
        self.convertbtn = QtWidgets.QPushButton(parent=Form)
        self.convertbtn.setGeometry(QtCore.QRect(180, 220, 113, 32))
        self.convertbtn.setObjectName("convertbtn")
        #  layout for the convert to box
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(270, 150, 197, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        #  convert to label
        self.ConvertToLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_3)
        self.ConvertToLabel.setObjectName("ConvertToLabel")
        self.horizontalLayout_3.addWidget(self.ConvertToLabel)
        # convert to box
        self.convertToBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget_3)
        self.convertToBox.setObjectName("convertToBox")
        self.convertToBox.addItems(self.cur)
        self.horizontalLayout_3.addWidget(self.convertToBox)
        #  converted amount layout
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(parent=Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(270, 180, 201, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #  converted amount input
        self.ConvertedAmount = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_4)
        self.ConvertedAmount.setObjectName("ConvertedAmount")
        self.horizontalLayout_4.addWidget(self.ConvertedAmount)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    #  sets up the window
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Currency Convertor"))
        self.convertFromLabel.setText(_translate("Form", "Convert From:"))
        self.ConvertFromAmount.setPlaceholderText(_translate("Form", "Enter amount to convert here"))
        self.convertbtn.setText(_translate("Form", "Convert"))
        self.ConvertToLabel.setText(_translate("Form", "Convert To:"))
        self.ConvertedAmount.setPlaceholderText(_translate("Form", "Converted Amount"))
    
    #  gets data from the api
    def getData(self):
        return currencyapicom.Client("cur_live_CZ8QPY8bVVNSQm4Q8KQ1c7h1kZhJNyjqikspmMBz")
    
    
    #  gets all the currencies from the api
    def getAllCurrencies(self, data):
        cur = self.getCurrency(data)
        return cur
    
    #  gets the name of the currency
    def getCurrency(self, datas):
        arr = []
        for data in datas:
                arr.append(datas[data]["name"])
        return arr
    #  gets the symbol of the currency
    def getSymbol(self, datas, name):
        for data in datas:
            if(datas[data]["name"] == name):
                return datas[data]["code"]
    #  converts the currency
    def convert(self):
        fromCur = self.getSymbol(self.data["data"], self.convertFromBox.currentText())
        toCur = self.getSymbol(self.data["data"], self.convertToBox.currentText())
       
        amount = float(self.ConvertFromAmount.text())
        try:
            data = self.response.latest(fromCur)
            converted = amount * data["data"][toCur]["value"]
            converted = round(converted, 2)
            self.ConvertedAmount.setText(str(converted))
        except Exception as e:
            print("error")
            print(e)
            self.ConvertedAmount.setText("Error")
            self.ConvertedAmount.setStyleSheet("color: red")
    

# runs the window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
