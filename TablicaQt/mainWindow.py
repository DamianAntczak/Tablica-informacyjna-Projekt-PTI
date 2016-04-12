#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import sys, time
from PyQt4 import QtGui, QtCore
import urllib, json
import feedparser


class DateTimeWidget(QtGui.QWidget):

    def __init__(self,parent=None):
        super(DateTimeWidget, self).__init__(parent)
	
        self.initUI()
        
    def displayTime(self):
		timeString = QtCore.QTime.currentTime().toString();
		self.label.setText(timeString)

    def initUI(self):

        self.setGeometry(300,300,250,150)
        
        
        
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
        

class RssWidget(QtGui.QWidget):

    def __init__(self,parent=None):
        super(RssWidget, self).__init__(parent)
	
        self.initUI()
        
    def displayRSS(self):
		self.labelRss.setText(self.feed["items"][self.i]["title"])
		if self.i == len(self.feed['items']) - 1:
			self.i = 0
		else:
			self.i += 1

    def initUI(self):
		
		self.i = 1
		self.setGeometry(300,600,250,150)
		self.timer2 = QtCore.QTimer(self)
		self.timer2.setInterval(5000)
		self.timer2.timeout.connect(self.displayRSS)
		self.timer2.start()
        
		python_wiki_rss_url = "http://wiadomosci.wp.pl/kat,1329,ver,rss,rss.xml"
		self.feed = feedparser.parse( python_wiki_rss_url )
		print(self.feed[ "channel" ][ "title" ])
        
		self.labelRss = QtGui.QLabel(self.feed["items"][0]["title"]+"                                                                   ", self)
		self.labelRss.setStyleSheet("font-size: 24px")
		
		
class WeathercastWidget(QtGui.QWidget):

    def __init__(self,parent=None):
        super(WeathercastWidget, self).__init__(parent)
	
        self.initUI()
        

    def initUI(self):
		
		self.setGeometry(300,600,250,150)
		self.c = QtGui.QLabel(self)
		self.opis = QtGui.QLabel(self)
		self.cisnienie = QtGui.QLabel(self)
		self.wilgotnosc = QtGui.QLabel(self)
		
		url = "http://api.openweathermap.org/data/2.5/weather?q=Poznan,pl&APPID=b4ea1aaa3e45dfff27f3557cdd18c301&lang=pl&units=metric"
		response = urllib.urlopen(url)
		data = json.loads(response.read())
		print data
		
		screenShape = QtGui.QDesktopWidget().screenGeometry()
		
		self.c.setText('Poznan ' + str(data['main']['temp'])+'℃'.decode('utf-8'))
		self.opis.setText(data['weather'][0]['description'])
		self.cisnienie.setText(str(data['main']['pressure'])+' hPa')
		self.wilgotnosc.setText(str(data['main']['humidity'])+'%')
		
		self.c.move(0,10)
		self.opis.move(0,35)
		self.cisnienie.move(0,65)
		self.wilgotnosc.move(0,85)
		
		self.c.setStyleSheet("font-size: 24px")
		self.opis.setStyleSheet("font-size: 22px")

        

class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):               

        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setStyleSheet("background-color: #99e6ff") 
        
        self.dateTimeWidget = DateTimeWidget(self)
        self.rssWidget = RssWidget(self)
        self.rssWidget.move(0,200)
        
        self.weathercastWidget = WeathercastWidget(self)
        
        
        self.showFullScreen()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
        


