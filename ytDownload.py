import PyQt6 
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
import sys
from pathlib import Path
from math import floor
import pytube


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.ytDownload = QPushButton(parent=Form)
        self.ytDownload.setGeometry(QtCore.QRect(170, 150, 113, 32))
        self.ytDownload.setObjectName("ytDownload")
        self.ytDownload.clicked.connect(self.download)
        self.yturl = QLineEdit(parent=Form)
        self.yturl.setGeometry(QtCore.QRect(25, 70, 450, 21))
        self.yturl.setObjectName("yturl")
        self.horizontalLayoutWidget_3 = QWidget(parent=Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 100, 481, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.YtSaveLabel = QLabel(parent=self.horizontalLayoutWidget_3)
        self.YtSaveLabel.setObjectName("YtSaveLabel")
        self.horizontalLayout.addWidget(self.YtSaveLabel)
        self.ytSaveline = QLineEdit(parent=self.horizontalLayoutWidget_3)
        self.ytSaveline.setObjectName("ytSaveline")
        self.horizontalLayout.addWidget(self.ytSaveline)
        self.ytBrowse = QPushButton(parent=self.horizontalLayoutWidget_3)
        self.ytBrowse.setObjectName("ytBrowse")
        self.ytBrowse.clicked.connect(self.openDir)
        self.horizontalLayout.addWidget(self.ytBrowse)
        self.progressBar = QProgressBar(parent=Form)
        self.progressBar.setGeometry(QtCore.QRect(170, 190, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayoutWidget = QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 220, 461, 61))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QLabel(parent=self.verticalLayoutWidget)
        self.title.setObjectName("Title")
        self.verticalLayout.addWidget(self.title)
        self.length = QLabel(parent=self.verticalLayoutWidget)
        self.length.setObjectName("length")
        self.verticalLayout.addWidget(self.length)
        self.account = QLabel(parent=self.verticalLayoutWidget)
        self.account.setObjectName("account")
        self.verticalLayout.addWidget(self.account)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ytDownload.setText(_translate("Form", "Download"))
        self.yturl.setText(_translate("Form", "Enter Link Here"))
        self.YtSaveLabel.setText(_translate("Form", "Save To:"))
        self.ytBrowse.setText(_translate("Form", "Browse"))
        self.title.setText(_translate("Form", "Title:"))
        self.length.setText(_translate("Form", "Length:"))
        self.account.setText(_translate("Form", "Creator:"))
    def download(self):
        try:
            link = self.yturl.text()
            yt = pytube.YouTube(link)
            print("Title: ",yt.title)
            # video = yt.streams.get_highest_resolution()
            print("Length: ",yt.length)

            self.title.setText(f'Title: {yt.title}')
            self.length.setText(f'Length: {floor(yt.length/60)} Minutes {yt.length%60} Seconds')

        
            self.account.setText(f'Creator: {yt.author}')
            
           
            
            yt.register_on_progress_callback(self.progress)
            
            yt.streams.get_highest_resolution().download(self.ytSaveline.text())
            
            self.progressBar.setValue(100)
            

            
        except Exception as e:
            print(e)
    def openDir(self):
        print("open Dir clicked")
        folder = QFileDialog.getExistingDirectory()
        
        if folder:
            path = Path(folder)
            self.ytSaveline.setText(str(path))
            print(path)
    def progress(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        progress = (float(abs(bytes_remaining-size)/size))*float(100)
        self.progressBar.setValue(int(progress))
        print(f"{progress}% downloaded")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
