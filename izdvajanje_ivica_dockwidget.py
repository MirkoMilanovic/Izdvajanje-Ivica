# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IzdvajanjeIvicaDockWidget
                                 A QGIS plugin
 Izdvajanje ivica
                             -------------------
        begin                : 2017-09-07
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Mirko Milanovic
        email                : milanovic_mirko@ymail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal

import random
import processing
from qgis.core import QgsRasterLayer
from PyQt4.QtCore import QFileInfo


FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'izdvajanje_ivica_dockwidget_base.ui'))

# Constants
LAPLACIAN = 1
LOG = 2

class IzdvajanjeIvicaDockWidget(QtGui.QDockWidget, FORM_CLASS):

    closingPlugin = pyqtSignal()

    def __init__(self, parent=None):
        """Constructor."""
        super(IzdvajanjeIvicaDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        # polja
        self.activeLayer = None
        self.iface = None

        self.buttonDo.clicked.connect(self.process_layer) # Povezuje dogadjaj click dugmeta sa metodom process_layer


    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()


    def getKernelModL(self):
    	return self.comboKernelL.currentIndex()

    def getSigmaL(self):
        return self.doubleSpinBoxSigmaL.value()

    def getRadijusL(self):
        return self.doubleSpinBoxRadijusL.value()


    def getKernelModG(self):
        return self.comboKernelG.currentIndex()

    def getSigmaG(self):
        return self.doubleSpinBoxSigmaG.value()

    def getRadijusG(self):
        return self.doubleSpinBoxRadijusG.value()


    def getFilter(self):
    	if self.radioLaplacian.isChecked():
    		return LAPLACIAN
    	elif self.radioLoG.isChecked():
    		return LOG
    	return None # null u javi -> None

    def process_layer(self):
    	self.layer = self.iface.activeLayer()
        print("Izdvajanje ivica. Filter {0}".format(self.getFilter()))

        if self.getFilter() == LAPLACIAN:
            result = self.laplacian(self.layer)
        else:
            result = self.gauss(self.layer)

        self.iface.addRasterLayer(result["RESULT"], "rezultat")

    def laplacian(self, layer):

# PARAMETRI ZA LAPLACIAN
#         Grid [raster]
# <put parameter description here>
# Method [selection]
# <put parameter description here>

# Options:

# 0 — [0] standard kernel 1
# 1 — [1] standard kernel 2
# 2 — [2] Standard kernel 3
# 3 — [3] user defined kernel
# Default: 0

# Standard Deviation (Percent of Radius) [number]
# <put parameter description here>

# Default: 0

# Radius [number]
# <put parameter description here>

# Default: 1

# Search Mode [selection]
# <put parameter description here>

# Options:

# 0 — [0] square
# 1 — [1] circle
# Default: 0
        sigma = self.getSigmaL()
        radius = self.getRadijusL()
        mode = self.getKernelModL()
        fileName = "C:\laplace{0}.tif".format(random.randint(0, 1000000))
        return processing.runalg('saga:laplacianfilter', self.layer, 3, sigma, radius, mode, fileName)

    def gauss(self, layer):

# PARAMETRI ZA GAUSOV FILTAR
        #         Grid [raster]
# <put parameter description here>
# Standard Deviation [number]
# <put parameter description here>

# Default: 1

# Search Mode [selection]
# <put parameter description here>

# Options:

# 0 — [0] Square
# 1 — [1] Circle
# Default: 0

# Search Radius [number]
# <put parameter description here>

# Default: 3
        sigmaG = self.getSigmaG()
        modeG = self.getKernelModG()
        radiusG = self.getRadijusG()
        fileNameG = "C:\gauss{0}.tif".format(random.randint(0, 1000000))
        return processing.runalg('saga:gaussianfilter', self.layer, sigmaG, modeG, radiusG, fileNameG)

