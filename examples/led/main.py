#!/usr/bin/python

from PySide.QtCore import *
import QmSystem
import time

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        led = QmSystem.QmLED(self)

        print "The led will be disabled in 5 seconds"
        time.sleep(5)
        print "LED has been disabled with success: %r" % led.disable()
        time.sleep(1)
        print "Enabling LED; success: %r" % led.enable()
        print "Trying to activating the LED; success: %r" % led.activate("PatternCommunication")
        print "Waiting 5 secs"
        time.sleep(5)
        print "Disactivating %r" % led.deactivate("PatternCommunication")
        print "TEST FINISHED"

def main():
    app = QCoreApplication([])
    c = client()
    return app.exec_()

if __name__ == '__main__':
    main()

