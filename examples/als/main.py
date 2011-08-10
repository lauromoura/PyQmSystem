#!/usr/bin/python

from PySide.QtCore import *
import QmSystem

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        als = QmSystem.QmALS(self)

        als.requestSession()

        if als.sessionType() == QmSystem.QmSensor.SessionTypeNone:
            print "Error while connecting to sensor: %s" % als.lastError()
            return
        else:
            print "Got session: %d" % als.sessionType()

        als.start()

        QObject.connect(als, SIGNAL('ALSChanged(const MeeGo::QmAlsReading)'), self.ALSChanged)

    def ALSChanged(self, value):
        print "[ALS]: [%d] %d lux" % (value.timestamp, value.value)

def main():
    app = QCoreApplication([])
    c = client()
    return app.exec_()

if __name__ == '__main__':
    main()

