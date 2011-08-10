#!/usr/bin/python

from PySide.QtCore import *
import QmSystem

class client(QObject):
    def __init__(self):
        QObject.__init__(self)
        self.batt = QmSystem.QmBattery(self)

        self.printData()

        self.chargeAnimationTimer = QTimer(self)
        self.maxBars = self.batt.getMaxBars()
        self.percentage = self.batt.getRemainingCapacityPct()
        self.bars = self.batt.getRemainingCapacityBars()
        self.showBars = self.bars
        self.batteryState = self.batt.getBatteryState()
        self.chargingState = self.batt.getChargingState()
        self.chargerType = self.batt.getChargerType()
        self.chargingTime = self.batt.getRemainingChargingTime()
        self.chargeAnimationPhase = 0
        self.current = 0


        self.printStatusLine()

        QObject.connect(self.chargeAnimationTimer, SIGNAL('timeout()'), self.chargeAnimationHandler)
        QObject.connect(self.batt, SIGNAL('batteryStateChanged(MeeGo::QmBattery::BatteryState)'), self.batteryStateChanged)
        QObject.connect(self.batt, SIGNAL('batteryRemainingCapacityChanged(int, int)'), self.batteryRemainingCapacityChanged)
        QObject.connect(self.batt, SIGNAL('chargingStateChanged(MeeGo::QmBattery::ChargingState)'), self.chargingStateChanged)
        QObject.connect(self.batt, SIGNAL('chargerEvent(MeeGo::QmBattery::ChargerType)'), self.chargerEvent)
        QObject.connect(self.batt, SIGNAL('batteryCurrent(int)'), self.batteryCurrent)

        if not self.batt.startCurrentMeasurement(QmSystem.QmBattery.RATE_5000ms):
            print "startCurrentMeasurement failed"

        if self.isChargeAnimation():
            self.startChargeAnimation()

    def batteryStateChanged(self, newBatteryState):
        print "Battery state changed to: %d" % newBatteryState

        self.batteryState = newBatteryState
        if not self.isChargeAnimation():
            self.stopChargeAnimation()
        self.printStatusLine()

    def batteryRemainingCapacityChanged(self, newPercentage, newBars):
        self.percentage = newPercentage
        self.bars = newBars
        self.setBarCount()
        self.printStatusLine()

    def chargingStateChanged(self, newChargingState):
        print "Charging state changed to %d (charger type: %d)" % (newChargingState, self.batt.getChargerType())

        self.chargingState = newChargingState
        if self.isChargeAnimation():
            self.startChargeAnimation()
        else:
            self.stopChargeAnimation()
        self.chargingTime = self.batt.getRemainingChargingTime()
        self.printStatusLine()

    def chargerEvent(self, newChargerType):
        print "Charger type changed to: %d" % newChargerType

        self.chargerType = newChargerType
        self.printStatusLine()

    def printData(self):
        # battery state
        batteryState = self.batt.getBatteryState()
        self.printBatteryState(batteryState)

        # nominal capacity
        nominalCapa = self.batt.getNominalCapacity()
        print "Nominal capacity = %d mAh" % nominalCapa

        # Voltage
        voltage = self.batt.getVoltage()
        print "Voltage = %d mV" % voltage

        # Battery capacity mAh
        mAh = self.batt.getRemainingCapacitymAh()
        print "Remaining capacity = %d mAh" % mAh

        # Battery percentage
        self.percentage = self.batt.getRemainingCapacityPct()
        print "Percentage = %d " % self.percentage

        # Battery bars
        self.bars = self.batt.getRemainingCapacityBars()
        print "Bars = %d" % self.bars

        # Charger Type
        chargerType = self.batt.getChargerType()
        self.printChargerType(chargerType)

        # charging state
        chargingState = self.batt.getChargingState()
        self.printChargingState(chargingState)

        # Remaining idle time
        idleTime = self.batt.getRemainingIdleTime(QmSystem.QmBattery.NormalMode)
        print "Remaining idle time = %d seconds" % idleTime
 
        # Remaining talk time
        talkTime = self.batt.getRemainingTalkTime(QmSystem.QmBattery.NormalMode)
        print "Remaing talk time = %d seconds" % talkTime

        # Remaining charging time
        chargingTime = self.batt.getRemainingChargingTime()
        print "Remaining charging time = %d seconds" % chargingTime

        # Battery condition
        batteryCondition = self.batt.getBatteryCondition()
        self.printBatteryCondition(batteryCondition)


    def printBatteryState(self, batteryState):
        if batteryState == QmSystem.QmBattery.StateEmpty:
            print "Battery state empty"
        elif batteryState == QmSystem.QmBattery.StateLow:
            print "Battery state low"
        elif batteryState == QmSystem.QmBattery.StateOK:
            print "Battery state OK"
        elif batteryState == QmSystem.QmBattery.StateFull:
            print "Battery state full"
        elif batteryState == QmSystem.QmBattery.StateError:
            print "Battery state error"
        else:
            print "Unexpected battery state: %d" % batteryState


    def printChargerType(self, chargerType):
        if chargerType == QmSystem.QmBattery.Unknown:
            print "Charger type Unknown"
        elif chargerType == QmSystem.QmBattery.None:
            print "Charger type None"
        elif chargerType == QmSystem.QmBattery.Wall:
            print "Charger type Wall"
        elif chargerType == QmSystem.QmBattery.USB_500mA:
            print "Charger type USB_500mA"
        elif chargerType == QmSystem.QmBattery.USB_100mA:
            print "Charger type USB_100mA"
        else:
            print "Unexpected charger type: %d" % chargerType

    def printChargingState(self, chargingState):
        if chargingState == QmSystem.QmBattery.StateNotCharging:
            print "ChargingState not charging"
        elif chargingState == QmSystem.QmBattery.StateCharging:
            print "ChargingState charging"
        elif chargingState == QmSystem.QmBattery.StateChargingFailed:
            print "ChargingState charging falied"
        else:
            print "Unexpected charging state: %d" % chargingState

    def printBatteryCondition(self, batteryCondition):
        if batteryCondition == QmSystem.QmBattery.ConditionGood:
            print "BatteryCondition Good"
        elif batteryCondition == QmSystem.QmBattery.ConditionPoor:
            print "BatteryCondition Good"
        elif batteryCondition == QmSystem.QmBattery.ConditionUnknown:
            print "BatteryCondition Unknown"
        else:
            print "Unexpected battery condition: %d" % batteryCondition

    def printStatusLine(self):
        print "[",
        for i in range(0,self.showBars + 1):
            print '|',
        for i in range(self.showBars + 1, self.maxBars):
            print '.'
        print "] %d %d mA " % (self.percentage, self.current),

        if self.batteryState == QmSystem.QmBattery.StateEmpty:
            print " [Recharge battery]               ",
        elif self.batteryState == QmSystem.QmBattery.StateLow:
            print " [Battery low]                    ",
        elif self.batteryState == QmSystem.QmBattery.StateOK:
            if self.chargingTime != -1:
                print "%d minutes to full            " % (self.chargingTime /60),
            else:
                print "                              ",
        elif self.batteryState == QmSystem.QmBattery.StateFull:
            print " [Battery full]                   ",
        elif self.batteryState == QmSystem.QmBattery.StateError:
            print " [Battery error]                  ",
        else:
            print " [Unknown battery state: %d]      " % self.batteryState,

        if self.chargerType == QmSystem.QmBattery.None:
            print "                          ",
        elif self.chargerType == QmSystem.QmBattery.Wall:
            print " [WALL charger]           ",
        elif self.chargerType == QmSystem.QmBattery.USB_500mA:
            print " [USB 500 charger]        ",
        elif self.chargerType == QmSystem.QmBattery.USB_100mA:
            print " [USB 100 charger]        ",
        else:
            print " [Unknown charger type: %d]" % self.chargerType,
        print "\n"

    def setBarCount(self):
        if self.isChargeAnimation():
            self.chargeAnimationPhase += 1
            if self.chargeAnimationPhase > self.maxBars:
                if self.bars == self.maxBars:
                    self.chargeAnimationPhase = self.maxBars -1
                else:
                    self.chargeAnimationPhase = self.bars
            self.showBars = self.chargeAnimationPhase
        else:
            self.showBars = self.bars
         
    def isChargeAnimation(self):
        if self.chargingState == QmSystem.QmBattery.StateCharging and self.batteryState != QmSystem.QmBattery.StateFull:
            return True
        else:
            return False

    def startChargeAnimation(self):
        self.chargeAnimationPhase = self.bars
        self.setBarCount()
        self.chargeAnimationTimer.start(1000)

    def stopChargeAnimation(self):
        self.chargeAnimationTimer.stop()
        self.setBarCount()

    def chargeAnimationHandler(self):
        self.setBarCount()
        self.chargingTime = self.batt.getRemainingChargingTime()
        self.printStatusLine()

    def batteryCurrent(self, newCurrent):
        self.current = newCurrent
        self.printStatusLine()

def main():
    app = QCoreApplication([])
    c = client()
    return app.exec_()

if __name__ == '__main__':
    main()

