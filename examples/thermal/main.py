
from PySide.QtCore import QCoreApplication, QObject, SIGNAL
from QmSystem import QmThermal


def callback(state):
    print state

def main():

    app = QCoreApplication([])
    therm = QmThermal()
    print("Thermal state: %s" % therm.get())

    QObject.connect(therm, SIGNAL('thermalChanged(MeeGo::QmThermal::ThermalState)'), callback)

    while True:
        therm.setObjectName('aaaa')

    return app.exec_()

if __name__ == '__main__':
    main()
