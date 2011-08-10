#!/usr/bin/python

from PySide.QtCore import *
import QmSystem
import sys

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        cabc = QmSystem.QmCABC(self)

        status = cabc.get()

        # TEST 1.
        print "* TEST 1 'CABCMode get() - CABC status:"
        if status == QmSystem.QmCABC.Mode.Off:
            print "  Off"
        elif status == QmSystem.QmCABC.Mode.Ui:
            print "  Ui"
        elif status == QmSystem.QmCABC.Mode.StillImage:
            print "  StillImage"
        elif status == QmSystem.QmCABC.Mode.MovingImage:
            print "  MovingImage"
        else:
            print "  ERROR"

        # TEST 2.
        print "* TEST 2. set(CABCMode mode) - Setting display to:"
        print "- Off: %r" % cabc.set(QmSystem.QmCABC.Mode.Off)
        print "- Ui: %r" % cabc.set(QmSystem.QmCABC.Mode.Ui)
        print "- StillImage: %r" % cabc.set(QmSystem.QmCABC.Mode.StillImage)
        print "- MovingImage: %r" % cabc.set(QmSystem.QmCABC.Mode.MovingImage)

def main():
    app = QCoreApplication([])
    c = client()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

