# This is a widget that is responsible for shortening the url using pyshorteners
from PyQt6 import QtCore, QtGui, QtWidgets
import pyshorteners

#  url shortener class
class Ui_Title(object):
    def setupUi(self, Title):
        #  sets up base information for the window
        Title.setObjectName("Title")
        Title.resize(500, 500)
        #  label for the window
        self.label = QtWidgets.QLabel(parent=Title)
        self.label.setGeometry(QtCore.QRect(200, 80, 211, 16))
        self.label.setObjectName("label")
        #  shorten button
        self.shortbtn = QtWidgets.QPushButton(parent=Title)
        self.shortbtn.setGeometry(QtCore.QRect(200, 170, 120, 32))
        self.shortbtn.setObjectName("shortbtn")
        self.shortbtn.clicked.connect(self.shorten)
        #  url input for the url to shorten
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=Title)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 100, 481, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #  initial url label
        self.initialUrl = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.initialUrl.setObjectName("initialUrl")
        self.horizontalLayout.addWidget(self.initialUrl)
        #  initial url input
        self.initialUrlEdit = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget)
        self.initialUrlEdit.setObjectName("initialUrlEdit")
        self.horizontalLayout.addWidget(self.initialUrlEdit)
        #  shortened url label
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=Title)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 200, 481, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # shortened url label
        self.shortenLabel = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.shortenLabel.setObjectName("shortenLabel")
        self.horizontalLayout_2.addWidget(self.shortenLabel)
        #  shortened url input
        self.ShortenLine = QtWidgets.QLineEdit(parent=self.horizontalLayoutWidget_2)
        self.ShortenLine.setObjectName("ShortenLine")
        # hides the shortened url label and input
        self.shortenLabel.hide()
        self.ShortenLine.hide()
        self.horizontalLayout_2.addWidget(self.ShortenLine)
        

        self.retranslateUi(Title)
        QtCore.QMetaObject.connectSlotsByName(Title)
    #  sets up the window
    def retranslateUi(self, Title):
        _translate = QtCore.QCoreApplication.translate
        Title.setWindowTitle(_translate("Title", "Form"))
        self.label.setText(_translate("Title", "URL Shortener"))
        self.shortbtn.setText(_translate("Title", "Shorten"))
        self.initialUrl.setText(_translate("Title", "URL to Shorten:"))
        self.shortenLabel.setText(_translate("Title", "Shortened URL:"))
    #  shortens the url with pyshorteners
    def shorten(self):
        url = self.initialUrlEdit.text()
        s = pyshorteners.Shortener()
        self.ShortenLine.setText(s.tinyurl.short(url))
        self.ShortenLine.show()
        self.shortenLabel.show()

#  runs the window
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Title = QtWidgets.QWidget()
    ui = Ui_Title()
    ui.setupUi(Title)
    Title.show()
    sys.exit(app.exec())
