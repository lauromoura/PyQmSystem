#!/usr/bin/python

from PySide.QtCore import *
import QmSystem

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        hk = QmSystem.QmKeys(self)

        hk.volumeDownMoved.connect(self.volumeDownMoved)
        hk.volumeUpMoved.connect(self.volumeUpMoved)

    def volumeDownMoved(self):
        print "Volume down moved"

    def volumeUpMoved(self):
        print "Volume up moved"

def main():
    app = QCoreApplication([])
    c = client()
    return app.exec_()

if __name__ == '__main__':
    main()

