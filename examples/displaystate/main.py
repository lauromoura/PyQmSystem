#!/usr/bin/python

from PySide.QtCore import *
import QmSystem
import sys

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        ds = QmSystem.QmDisplayState(self)

        displayStatus = ds.get()

        # TEST 1.
        print "* TEST 1 'DisplayState get() - Screen status:"
        if displayStatus:
            if displayStatus == QmSystem.QmDisplayState.Off:
                print "  Off"
            elif displayStatus == QmSystem.QmDisplayState.Dimmed:
                print "  Dimmed"
            elif displayStatus == QmSystem.QmDisplayState.On:
                print "  On"
            else:
                print "  ERROR"

        # TEST 2.
        print "* TEST 2. set(DisplayState state) - Setting display to:"
        print "- Dimmed: %r" % ds.set(QmSystem.QmDisplayState.Dimmed)
        print "- On: %r" % ds.set(QmSystem.QmDisplayState.On)

        print "setbrightnessvalue(1)"; ds.setDisplayBrightnessValue(1)
        print "getbrightnessvalue(): %d" % ds.getDisplayBrightnessValue()

        print "setDisplayDimTimeout(6)"; ds.setDisplayDimTimeout(6)
        print "getDisplayDimTimeout(): %d" % ds.getDisplayDimTimeout()


        # TEST 3.
        print "* TEST 3. bool setBlankingPause(void) - method called with success: %r" % ds.setBlankingPause()

        # TEST 4.
        print "* TEST 4. Listening for display status changes..."
        QObject.connect(ds, SIGNAL('displayStateChanged(MeeGo::QmDisplayState::DisplayState)'), self.displayStateChanged)

    def displayStateChanged(self, state):
        print "  State changed to: %d" % state

def main():
    app = QCoreApplication([])
    c = client()
    return app.exec_()

if __name__ == '__main__':
    main()

