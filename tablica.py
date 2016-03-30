# -*- coding: utf-8 -*-

import sys, time
from PyQt4 import QtGui, QtCore
import urllib, json
import feedparser

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
        
        self.timer2 = QtCore.QTimer(self)
        self.timer2.setInterval(5000)
        self.timer2.timeout.connect(self.displayRSS)
        self.timer2.start()
        
        python_wiki_rss_url = "http://wiadomosci.wp.pl/kat,1329,ver,rss,rss.xml"
        self.feed = feedparser.parse( python_wiki_rss_url )
        print(self.feed[ "channel" ][ "title" ])
        
        self.labelRss = QtGui.QLabel(self.feed["items"][0]["title"]+"                                                                   ", self)
        self.labelRss.setStyleSheet("font-size: 24px")
        self.labelRss.move(100,600)
        
        self.labelImg = QtGui.QLabel(self)
        self.labelImg.move(500,400)
        self.labelImg.setFixedSize(200,200)
        myPixmap = QtGui.QPixmap('/home/damian/Dokumenty/earth.png')
        myScaledPixmap = myPixmap.scaled(self.labelImg.size(), QtCore.Qt.KeepAspectRatio)
        self.labelImg.setPixmap(myScaledPixmap)
			

        
        self.showFullScreen()
        
        self.i = 1
        
    def displayRSS(self):
		self.labelRss.setText(self.feed["items"][self.i]["title"])
		if self.i == len(self.feed['items']) - 1:
			self.i = 0
		else:
			self.i += 1
		
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
    
    c.move(screenShape.width()-300,10)
    opis.move(screenShape.width()-300,40)
    cisnienie.move(screenShape.width()-300,70)
    wilgotnosc.move(screenShape.width()-300,85)
    
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
