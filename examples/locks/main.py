#!/usr/bin/python

from PySide.QtCore import *
import QmSystem
import time

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        locks = QmSystem.QmLocks(self)

        #TEST1
        print "Getting device lock state: %d" % locks.getState(QmSystem.QmLocks.Device)
        time.sleep(1)
        print "Getting touchscreen/keyboard lock state: %d" % locks.getState(QmSystem.QmLocks.TouchAndKeyboard)
        time.sleep(1)

        #TEST2
        print "Setting device lock state to locked: %r" % locks.setState(QmSystem.QmLocks.Device, QmSystem.QmLocks.Locked)
        time.sleep(1)
        print "Getting device lock state: %d" % locks.getState(QmSystem.QmLocks.Device)
        time.sleep(1)
        print "Setting device lock state to unlocked: %r" % locks.setState(QmSystem.QmLocks.Device, QmSystem.QmLocks.Unlocked)
        time.sleep(1)
        print "Getting device lock state: %d" % locks.getState(QmSystem.QmLocks.Device)
        time.sleep(1)

        #TEST3
        print "Setting touchscreen/keyboard lock state to locked: %r" % locks.setState(QmSystem.QmLocks.TouchAndKeyboard, QmSystem.QmLocks.Locked)
        time.sleep(1)
        print "Getting touchscreen/keyboard lock state: %d" % locks.getState(QmSystem.QmLocks.TouchAndKeyboard)
        time.sleep(1)
        print "Setting touchscreen/keyboard lock state to unlocked %r" % locks.setState(QmSystem.QmLocks.TouchAndKeyboard, QmSystem.QmLocks.Unlocked)
        time.sleep(1)
        print "Getting touchscreen/keyboard lock state: %d" % locks.getState(QmSystem.QmLocks.TouchAndKeyboard)
        time.sleep(1)

        #TEST4
        print "Listeining for deviice and keyboard lock signals..."
        QObject.connect(locks, SIGNAL('stateChanged(MeeGo::QmLocks::Lock, MeeGo::QmLocks::State'),self.stateChanged)

    def stateChanged(self, lock, state):
        print lock, state


def main():
    app = QCoreApplication([])
    c = client()
    return app.exec_()

if __name__ == '__main__':
    main()

