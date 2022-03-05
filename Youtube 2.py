from pytube import YouTube
from pytube import Playlist
import os
import time
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
d={}


class Ui_MainWindow(object):
    def download(self):
        try:
            lnk=self.textEdit.toPlainText()
            if self.comboBox.currentText()=="Playlist":
                try:
                    playlist = Playlist(lnk)
                    ss=playlist[1].title().lower()
                    print('Number of videos in playlist: %s' % len(playlist.video_urls))
                    os.mkdir('Z:/ytpjt/'+lnk)
                    os.chdir('Z:/ytpjt/'+lnk)
                    playlist.download_all()
                except:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Enter Playlist daa pota")
                    x = msg.exec_() 
            else:
                os.chdir('Z:/ytpjt')
                d[self.comboBox_2.currentText()].download()
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Submit Link and category first")
            x = msg.exec_() 
        
    def var(self):
        try:
            lnk=self.textEdit.toPlainText()
            ct=self.comboBox.currentText()
            if ct=="All":
                yt = YouTube(lnk)
                x=yt.streams
                self.comboBox.clear()  
                for xx in x:
                    d[str(xx)]=xx
                    self.comboBox_2.addItem(str(xx))
            if ct=="progressive":
                yt = YouTube(lnk)
                x=yt.streams.filter(progressive=True)
                self.comboBox.clear()  
                for xx in x:
                    d[str(xx)]=xx
                    self.comboBox_2.addItem(str(xx))
            if ct=="adaptive":
                yt = YouTube(lnk)
                x=yt.streams.filter(adaptive=True)
                self.comboBox.clear()  
                for xx in x:
                    d[str(xx)]=xx
                    self.comboBox_2.addItem(str(xx))
            if ct=="720p":
                yt = YouTube(lnk)
                x=yt.streams.filter(progressive=True,res="360p")
                self.comboBox.clear()  
                for xx in x:
                    d[str(xx)]=xx
                    self.comboBox_2.addItem(str(xx))
            if ct=="480p":
                yt = YouTube(lnk)
                x=yt.streams.filter(progressive=True,res="480p")
                self.comboBox.clear()  
                for xx in x:
                    d[str(xx)]=xx
                    self.comboBox_2.addItem(str(xx))
            if ct=="360p":
                yt = YouTube(lnk)
                self.comboBox.clear()  
                x=yt.streams.filter(progressive=True,res="360p")
                for xx in x:
                    d[str(xx)]=xx
                    self.comboBox_2.addItem(str(xx))
            if ct=="Audio":
                yt = YouTube(lnk)
                x=yt.streams.filter(only_audio=True)
                self.comboBox.clear()  
                for xx in x:
                    d[str(xx)]=xx
                    self.comboBox_2.addItem(str(xx))
        except:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Enter the Link ")
            x = msg.exec_() 


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 438)
        MainWindow.setMaximumSize(QtCore.QSize(468, 438))
        MainWindow.setStyleSheet("background-color:#CD5C5C")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 190, 441, 31))
        self.comboBox.setStyleSheet("background-color:#ADFF2F;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem('All')
        self.comboBox.addItem('progressive')
        self.comboBox.addItem('adaptive')
        self.comboBox.addItem('720p')
        self.comboBox.addItem('360p')
        self.comboBox.addItem('480p')
        self.comboBox.addItem('Audio')
        self.comboBox.addItem('Playlist')
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 260, 441, 31))
        self.comboBox_2.setStyleSheet("background-color:#ADFF2F;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 20, 161, 141))
        self.label.setMaximumSize(QtCore.QSize(161, 141))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ty.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 131, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 121, 21))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 320, 441, 101))
        self.pushButton.setStyleSheet("background-color:skyblue;")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(60, 80))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 271, 71))
        self.textEdit.setStyleSheet("background-color:white")
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("OCR A Extended")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 271, 23))
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setStyleSheet("background-color:#98FB98;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.var)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.download)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Category:-"))
        self.label_3.setText(_translate("MainWindow", "Varient:-"))
        self.label_4.setText(_translate("MainWindow", "Link:-"))
        self.pushButton_2.setText(_translate("MainWindow", "SUBMIT (Link and Category)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
