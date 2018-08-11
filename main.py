#/usr/bin/python3.6
#-*- coding=utf-8 -*-
"""
Created on Wed Jun  1 10:30:04 2018
@author: crunch
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class MyApplication(QWidget):
    colorindex = 0
    timesindex = 0
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.palette = QPalette()
        self.colorlist = []
        self.colorlist.append("black.jpeg")
        self.colorlist.append("green.jpg")
        self.colorlist.append("blue.jpg")
        self.colorlist.append("red.jpg")
        self.colorlist.append("yellow.jpg")
        self.timerColor = QTimer()
        self.timerColor.setInterval(1000)
        self.timerBlack = QTimer()
        self.timerBlack.setInterval(500)
        self.timerBlack.timeout.connect(self.BlackEnd)
        self.clour = ""
        ##########################整体########################
        self.setWindowTitle(u'EGG')
        self.setAutoFillBackground(True)
        self.resize(1000,500)
        self.move(500,200)
        ##############################左侧#############################
        #########并列部分
        self.btnSelfile = QPushButton(u"SELECT")
        self.btnSelfile.setFlat(True)   #边缘消失
        self.labColor = QLabel()
        self.labColor.setAutoFillBackground(True)
        self.palette.setBrush(QPalette.Window, QBrush(QPixmap(self.colorlist[MyApplication.colorindex])))
        self.labColor.setPalette(self.palette)
        self.vboxcolor = QVBoxLayout()
        self.vboxcolor.addWidget(self.labColor)
        self.btnTrain = QPushButton(u"TRAIN")
        self.btnTrain.setFlat(True)  # 边缘消失
        vboxleft  = QVBoxLayout()
        vboxleft.addWidget(self.btnSelfile)
        vboxleft.addLayout(self.vboxcolor)
        vboxleft.addWidget(self.btnTrain)
        ##########################右侧############################
        self.labTruth = QLabel(u"Truth")
        labDect = QLabel(u"Dect")
        ########下方右侧布局
        vboxright = QVBoxLayout()
        vboxright.addWidget(self.labTruth)
        vboxright.addWidget(labDect)
        ##########################整体布局############################
        ########下方左中右
        hboxall = QHBoxLayout()
        hboxall.addLayout(vboxleft)
        hboxall.addLayout(vboxright)
        self.setLayout(hboxall)
        ##########################按钮链接初始化##########################
        self.__connect__()
    def __connect__(self):
        self.btnSelfile.clicked.connect(self.button_openfile_click)
        self.btnTrain.clicked.connect(self.button_train_click)
    def button_openfile_click(self):
        absulute_path = QFileDialog.getOpenFileName(self, 'Open File', '.', 'jpg files(*.jpg)')
        for i in range(len(self.colorlist)):
            if self.colorlist[i] in absulute_path[0]:
                MyApplication.colorindex = i
                print(i)
                break
            else:
                continue
    def button_train_click(self):
        self.labTruth.setText(self.colorlist[MyApplication.colorindex][-10:-4])  # @##########################5
       # MyApplication.colorindex=1
        self.palette.setBrush(QPalette.Window, QBrush(QPixmap(self.colorlist[MyApplication.colorindex])))
        self.labColor.setPalette(self.palette)
        self.timesindex=0
        self.timerColor.start()
        self.timerColor.timeout.connect(self.ColorEnd)
    def ColorEnd(self):
        self.timerColor.stop()
        #MyApplication.colorindex = 0
        self.palette.setBrush(QPalette.Window, QBrush(QPixmap(self.colorlist[0])))
        self.labColor.setPalette(self.palette)
        self.timerBlack.start()
    def BlackEnd(self):
        self.timerBlack.stop()
        if self.timesindex != 10:
            self.timesindex += 1
            #MyApplication.colorindex = 1
            self.palette.setBrush(QPalette.Window, QBrush(QPixmap(self.colorlist[MyApplication.colorindex])))
            self.labColor.setPalette(self.palette)
            self.timerColor.start()
        else:
            self.timesindex = 0
            self.colorindex = 0
if __name__ == '__main__':
    app = QApplication(sys.argv)
    foo = MyApplication()
    foo.show()
    sys.exit(app.exec_())
