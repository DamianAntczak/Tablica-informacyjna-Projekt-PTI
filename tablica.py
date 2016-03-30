# -*- coding: utf-8 -*-

import sys, time
from PyQt4 import QtGui, QtCore
import urllib, json

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
	
        self.initUI()

		

    def initUI(self):

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Tablica')
        self.setStyleSheet("background-color: #99e6ff")
        
        self.label = QtGui.QLabel(QtCore.QTime.currentTime().toString(), self)
        self.label.setStyleSheet("font-size: 24px")
        self.label.move(10,10)
        
        self.labelDate = QtGui.QLabel(time.strftime("%d %B %Y"), self)
        self.labelDate.setStyleSheet("font-size: 24px")
        self.labelDate.move(10,40)
        
        self.labelWeekDay = QtGui.QLabel(time.strftime("%A").decode('utf-8'), self)
        self.labelWeekDay.setStyleSheet("font-size: 24px")
        self.labelWeekDay.move(10,70)
                
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.displayTime)
        self.timer.start()
        
        self.showFullScreen()
    
    def displayTime(self):
		timeString = QtCore.QTime.currentTime().toString();
		self.label.setText(timeString)

    def keyPressEvent(self, e):

        if e.key() == QtCore.Qt.Key_Escape:
            self.close()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    b = QtGui.QLabel(ex)
    b.setText('Witamy')
    b.move(150,120)
    b.setStyleSheet("color: red; font-size: 64px")
    b.show()
    
    c = QtGui.QLabel(ex)
    opis = QtGui.QLabel(ex)
    cisnienie = QtGui.QLabel(ex)
    wilgotnosc = QtGui.QLabel(ex)
    
    url = "http://api.openweathermap.org/data/2.5/weather?q=Poznan,pl&APPID=b4ea1aaa3e45dfff27f3557cdd18c301&lang=pl&units=metric"
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    print data
    
    screenShape = QtGui.QDesktopWidget().screenGeometry()
    
    c.setText('Poznan ' + str(data['main']['temp'])+'℃'.decode('utf-8'))
    opis.setText(data['weather'][0]['description'])
    cisnienie.setText(str(data['main']['pressure'])+' hPa')
    wilgotnosc.setText(str(data['main']['humidity'])+'%')
    
    c.move(screenShape.width()-200,10)
    opis.move(screenShape.width()-200,40)
    cisnienie.move(screenShape.width()-200,70)
    wilgotnosc.move(screenShape.width()-200,85)
    
    c.setStyleSheet("font-size: 24px")
    opis.setStyleSheet("font-size: 22px")
    c.show()
    opis.show()
    cisnienie.show()
    wilgotnosc.show()
    
    b.move(screenShape.width()/2 - b.width()/2, screenShape.height()/2 - b.height()/2)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
