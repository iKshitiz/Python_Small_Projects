# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 14:25:27 2017

@author: skarpy
"""

import sys
from PyQt4 import QtGui, uic
import random
import time

 
qtCreatorFile = "dice_GUI.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

print("*"*50)
print("Welcome to the Dice Game!")
print("A Game of Luck")
print("*"*50)
print("Roll the die and if you roll a lucky six; You Win! :)")
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.push1)
        self.lineEdit_2.setText('Game on,\t Roll!')
        self.pushButton_2.clicked.connect(self.push2)
        self.pushButton_3.clicked.connect(self.push3)
        
    def push1(self):
        num = random.randint(1,6)
        time.sleep(2.0)
        if(num == 6):
            self.lineEdit.setText("Yay! You won!\t  You got:    " +str(num))
        else:
            self.lineEdit.setText("Aww, You Lost!\t  You got:    "+str(num))
            
        self.lineEdit_3.setText("Press Yes to Play again\tPress No to Exit Game\t")

    def push2(self):
        
        return
    
    def push3(self):
        
        sys.exit()
        
   
#   user_input = input("Click Roll to Roll\n")
#        
#    if(user_input == 'None' or user_input == None):
#            
#                
#            choice = input("Press Y to Play again\nPress N to Exit Game\n")
#            
#            if	(choice == 'Y' or choice == 'y'):
#                continue
#            
#            elif (choice == 'N' or choice == 'n'):
#                break
#            
#            else:   
#                print("\nPlease Enter Y/N.")
#                
#    else:
#                print("\nNot a valid option")
    
#  
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
    
