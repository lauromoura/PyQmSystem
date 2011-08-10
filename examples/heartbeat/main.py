#!/usr/bin/python

from PySide.QtCore import *
import QmSystem

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        hb = QmSystem.QmHeartbeat(self)

        print "Open returns: %r" % hb.open(QmSystem.QmHeartbeat.SignalNeeded)
        print "getFD = %d" % hb.getFD()
        print "close"
        hb.close()

        print "getFD after closing: %d" % hb.getFD()

        print "Open again, returns: %r" % hb.open(QmSystem.QmHeartbeat.SignalNeeded)
        print "getFD = %d" % hb.getFD()
        print "Listening for wakeup signals..."
        QObject.connect(hb, SIGNAL('wakeUp(QTime)'), self.wakeUp)

        print  "Don't wait for Heartbeat, then waiting time is: ",
        print hb.wait(0, 10, QmSystem.QmHeartbeat.DoNotWaitHeartbeat).toString()

        print "Waiting for heartbeat..."
        print "Heartbeat received after: ",
        print hb.wait(0, 10, QmSystem.QmHeartbeat.WaitHeartbeat).toString()
        
    def wakeUp(self):
        print "wakeUp signal received:"


def main():
    app = QCoreApplication([])
    c = client()
    return app.exec_()

if __name__ == '__main__':
    main()

