#!/usr/bin/python

from PySide.QtCore import *
import QmSystem

class AppWidget(QObject):
    def __init__(self):
        QObject.__init__(self)
        compass = QmSystem.QmCompass(self)

        if compass.requestSession() == QmSystem.QmSensor.SessionTypeControl:
            print "Got control session."
        elif compass.requestSession() == QmSystem.QmSensor.SessionTypeListen:
            print "Got listen session."
        elif compass.requestSession() == QmSystem.QmSensor.SessionTypeNone:
            print "FAIL: did not get control/listen session."

        QObject.connect(compass, SIGNAL('dataAvailable(const MeeGo::QmCompassReading)'), self.setValues)

        if compass.start():
            print "Compass Started."
        else:
            print "Compass couldn't start!!!"

    def setValues(self, value):
        print "Compass changed: [ %d ] %d --> %d" % (value.timestamp, value.level, value.degrees)


def main():
    app = QCoreApplication([])
    c = AppWidget()
    return app.exec_()

if __name__ == '__main__':
    main()

