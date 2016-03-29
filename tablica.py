import sys
from PyQt4 import QtGui, QtCore

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
    b.setText('Tablica')
    b.move(150,120)
    b.setStyleSheet("color: white; font-size: 64px")
    b.show()
    
    screenShape = QtGui.QDesktopWidget().screenGeometry()
    b.move(screenShape.width()/2 - b.width()/2, screenShape.height()/2 - b.height()/2)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
