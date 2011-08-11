
from PySide.QtCore import QCoreApplication, QObject, SIGNAL
from QmSystem import QmTap


def callback(tap):

    print tap.direction, tap.type

def main():

    app = QCoreApplication([])
    tap = QmTap()

    QObject.connect(tap, SIGNAL('tapped(MeeGo::QmTapReading)'), callback)

    tap.requestSession()
    tap.start()

    return app.exec_()

if __name__ == '__main__':
    main()
