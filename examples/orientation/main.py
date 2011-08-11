
import sys

from PySide.QtCore import QCoreApplication, QObject, SIGNAL
from QmSystem import QmOrientation

class Client(QObject):

    def __init__(self, parent=None):
        QObject.__init__(self, parent)

        self.orientation = QmOrientation(self)

        QObject.connect(self.orientation, SIGNAL('orientationChanged(MeeGo::QmOrientationReading)'),
                        self.orientationChanged)

        self.orientation.requestSession()
        self.orientation.start()

    def orientationChanged(self, orientation):
        print str(orientation.value).split('.')[-1]

def main():

    app = QCoreApplication(sys.argv)

    c = Client()

    return app.exec_()

if __name__ == '__main__':
    main()
