#!/usr/bin/python

from PySide.QtCore import *
import QmSystem
import sys, time

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        cs = QmSystem.QmCallState(self)

        print "Call state: %d" % cs.getState()
        print "Call type: %d" % cs.getType()

        print "Setting state to None and Type Normal: %r" % cs.setState(QmSystem.QmCallState.None, QmSystem.QmCallState.Normal)
        print "Listening for call status changes..."
        QObject.connect(cs, SIGNAL('stateChanged(MeeGo::QmCallState::State, MeeGo::QmCallState::Type)'), self.stateChanged)
        time.sleep(3)
        print "Setting state to Service and Type Emergency: %r" % cs.setState(QmSystem.QmCallState.Service, QmSystem.QmCallState.Emergency)

    def stateChanged(self, state, tp):
        print "State changed: new state is %d, new type is %d" % (state, tp)
        
def main():
    app = QCoreApplication([])
    c = client()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

