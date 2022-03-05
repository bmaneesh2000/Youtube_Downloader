from pytube import YouTube
from pytube import Playlist
import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def ytvid(self):
        lnk=self.textEdit.toPlainText()
        if self.radioButton_3.isChecked() == True:
            try:
                yt = YouTube(lnk)
                print(yt)
                x=yt.streams.filter(progressive=True,res="360p").first()
                os.chdir('Z:/ytpjt')
                x.download()
                print(x)
            except:
                print("fk")
        if self.radioButton_4.isChecked() == True:
            try:
                yt = YouTube(lnk)
                print(yt)
                x=yt.streams.filter(progressive=True,res="720p").first()
                os.chdir('Z:/ytpjt')
                x.download()
                print(x)
            except:
                print("fk")
        if self.radioButton_2.isChecked() == True:
            try:
                yt = YouTube(lnk)
                print(yt)
                x=yt.streams.filter(only_audio=True).first()
                os.chdir('Z:/ytpjt')
                x.download()
                print(x)
            except:
                print("fk")

        if self.radioButton.isChecked() == True:
            try:
                playlist = Playlist(lnk)
                ss=playlist[1].title().lower()
                print('Number of videos in playlist: %s' % len(playlist.video_urls))
                os.mkdir('Z:/ytpjt')
                playlist.download_all()
            except:
                print("fk")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(455, 298)
        MainWindow.setMinimumSize(QtCore.QSize(455, 298))
        MainWindow.setStyleSheet("background-color:#DC143C;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 230, 281, 41))
        self.pushButton.setStyleSheet("background-color:#7FFF00;")
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 240, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(-1)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("font-size:20px;color:white")
        self.radioButton.setObjectName("radioButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 180, 421, 31))
        self.textEdit.setStyleSheet("background-color:white;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 251, 151))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("59a59a8d79bbfd1d008b601a.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(290, 30, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(-1)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("font-size:20px;color:white")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(290, 70, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(-1)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("font-size:20px;color:white")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(290, 110, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(-1)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("font-size:20px;color:white")
        self.radioButton_4.setObjectName("radioButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.ytvid)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "download"))
        self.radioButton.setText(_translate("MainWindow", "playlist"))
        self.radioButton_2.setText(_translate("MainWindow", "Audio "))
        self.radioButton_3.setText(_translate("MainWindow", "360"))
        self.radioButton_4.setText(_translate("MainWindow", "720"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
