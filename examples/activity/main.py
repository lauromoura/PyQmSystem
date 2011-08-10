#!/usr/bin/python

from PySide.QtCore import *
import QmSystem

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        act = QmSystem.QmActivity(self)

        #TEST 1.
        print "TEST 1: get"
        activity = act.get()
        if activity == QmSystem.QmActivity.Inactive:
            print "Inactive"
        elif activity == QmSystem.QmActivity.Active:
            print "Active"
        else:
            print "ERROR"
            return

        #TEST 2.
        print "TEST2. Listening for activityChanged(QmActivity::Activity activity)"
        QObject.connect(act, SIGNAL('activityChanged(MeeGo::QmActivity::Activity)'), self.activityChanged)

    def activityChanged(self, activity):
        print "Activity changed to: %d" % (activity)

def main():
    app = QCoreApplication([])
    c = client()
    return app.exec_()

if __name__ == '__main__':
    main()

