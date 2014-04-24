__author__ = 'Clemens Prescher'
import sys
from PyQt4 import QtGui
from Controller.XrsMainController import XrsMainController
from Controller.XrsCalibrationController import XrsCalibrationController


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    controller = XrsCalibrationController()
    app.exec_()