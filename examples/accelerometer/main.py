#!/usr/bin/python

from PySide.QtCore import *
import QmSystem
import sys

class widget(QObject):
    def __init__(self):
        QObject.__init__(self)
        acc = QmSystem.QmAccelerometer(self)

        acc.requestSession(QmSystem.QmSensor.SessionTypeControl)

        if acc.sessionType() == QmSystem.QmSensor.SessionTypeNone:
            print "Error while connecting to sensor: %s" % acc.lastError()
            return
        else:
            print "Got session: %d" % acc.sessionType()

        QObject.connect(acc, SIGNAL("dataAvailable(const MeeGo::QmAccelerometerReading&)"), self.dataAvailable)

        acc.start()

    def dataAvailable(self, data):
        print "Time: %d X: %d Y: %d Z: %d" % (data.timestamp, data.x, data.y, data.z)

def main():
    app = QCoreApplication([])
    c = widget()
    return app.exec_()

if __name__ == '__main__':
    main()

