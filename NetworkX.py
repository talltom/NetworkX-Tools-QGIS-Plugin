"""
/***************************************************************************
Name			 	 : NetworkX Plugin
Description          : Perform network analysis using the NetworkX package
Date                 : 03/Jan/12 
copyright            : (C) 2012 by Tom Holderness /Newcastle University
email                : tom.holderness@ncl.ac.uk 
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
import qgis
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from NetworkXDialog import NetworkXDialog
from NetworkXDialog import NetworkXDialogPath
from NetworkXDialog import NetworkXDialogBuild

class NetworkX: 

  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface

  def initGui(self):  
    # Create actions that will start plugin configuration (seperate action for each tool)
    self.actionBuild = QAction(QIcon(":/plugins/NetworkX/icon.png"), \
        "Build Network", self.iface.mainWindow())
    self.actionPath = QAction(QIcon(":/plugins/NetworkX/icon.png"), \
        "Find Shortest Path", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.actionBuild, SIGNAL("activated()"), self.runBuild) 
    QObject.connect(self.actionPath, SIGNAL("activated()"), self.runPath)
    # Add toolbar button and menu item
    #self.iface.addToolBarIcon(self.action)
    self.iface.addPluginToMenu("&NetworkX Plugin", self.actionBuild)
    self.iface.addPluginToMenu("&NetworkX Plugin", self.actionPath)
  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removePluginMenu("&NetworkX Plugin",self.actionBuild)
    self.iface.removePluginMenu("&NetworkX Plugin",self.actionPath)    
    #self.iface.removeToolBarIcon(self.action)




  # run methods that performs all the real work (one run method per tool)
  def runBuild(self): 
    # create and show the dialog 
    dlg = NetworkXDialogBuild() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    #if result == 1:
    	#dlg.comboBoxInput.setEnabled(False)
    	

  def runPath(self): 
    # create and show the dialog 
    dlg = NetworkXDialogPath() 
    # show the dialog
    dlg.show()
    result = dlg.exec_() 
    # See if OK was pressed
    #if result == 1:
    	#process here. 
	#  pass       
