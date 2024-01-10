from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys
import convert 
import ytDownload
import UrlShortener
import currencyConverter

class Ui_Form(QWidget):
    def setupUi(self, Form):
        # sets up the Base window
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.tabWidget = QtWidgets.QTabWidget(parent=Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setObjectName("tabWidget")
        
        # implements all the widgets onto the page
        self.yt = ytDownload.Ui_Form()
        self.ytTab = QtWidgets.QWidget()
        self.ytTab.setObjectName("Youtube Downloader")
        self.yt.setupUi(self.ytTab)
        self.tabWidget.addTab(self.ytTab, "Youtube Downloader")

        self.convertWindow = convert.Ui_Form()   
        self.convertTab = QtWidgets.QWidget()
        self.convertTab.setObjectName("fileConvertor")
        self.convertWindow.setupUi(self.convertTab)
        # self.tab_3 = self.tab_3.setupUi(Form)
        self.tabWidget.addTab(self.convertTab, "File Convertor")

        self.shortener = UrlShortener.Ui_Title()
        self.shortenerTab = QtWidgets.QWidget()
        self.shortenerTab.setObjectName("urlShortener")
        self.shortener.setupUi(self.shortenerTab)
        self.tabWidget.addTab(self.shortenerTab, "URL Shortener")

        self.currency = currencyConverter.Ui_Form()
        self.currencyTab = QtWidgets.QWidget()
        self.currencyTab.setObjectName("currencyConverter")
        self.currency.setupUi(self.currencyTab)
        self.tabWidget.addTab(self.currencyTab, "Currency Converter")
        


        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())