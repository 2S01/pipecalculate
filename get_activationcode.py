from ast import Try
from re import S
import sys
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QPushButton,QGroupBox,QGridLayout,QLineEdit,QLabel,QTextBrowser
from PyQt5.QtGui import QRegExpValidator, QIcon
from PyQt5.QtCore import Qt, QFileInfo, QRegExp
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTreeWidgetItem, \
    QFileIconProvider, QMenu, QHeaderView, QTableWidgetItem, QInputDialog, QListWidgetItem



class ActivationWidget(QMainWindow):
    def __init__(self, parent=None):
        super(ActivationWidget, self).__init__(parent)

        self.maptable = [[4,8,3,1,7,5,2,6,9,0],
            [8,1,6,7,2,9,3,4,0,5],
            [6,7,2,4,1,5,0,9,8,3],
            [3,8,0,5,1,4,6,2,7,9],
            [8,1,3,6,0,7,9,4,5,2],
            [7,4,9,2,5,0,8,3,6,1],
            [0,9,5,2,6,4,1,7,3,8],
            [5,1,3,8,0,7,9,4,2,6],
            [9,6,0,4,5,1,8,2,3,7],
            [1,8,5,9,6,3,7,4,0,2]]

        self.setWindowTitle("获取激活码")
        self.resize(600, 400)
        self.setCentralWidget(QWidget())
        self.main_layout = QVBoxLayout(self.centralWidget())

        self.holder = QGroupBox()
        vbox = QGridLayout()
        self.macadress = QLineEdit("")
        self.macadress.setObjectName('macadress')
        lb1 = QLabel('物理地址:')
        vbox.addWidget(lb1,0,3,1,1)
        vbox.addWidget(self.macadress,0,5,1,1)
        self.activationcode = QLineEdit()
        lb2 = QLabel('激活码:')
        vbox.addWidget(lb2,1,3,1,1)
        vbox.addWidget(self.activationcode,1,5,1,1)
        
        self.holder.setLayout(vbox)
        self.main_layout.addWidget(self.holder)
        #self.savepathbutton.clicked.connect(self.choosepath)
        # self.holder.hide()

        self.loginbutton = QPushButton()
        self.loginbutton.setText("生成激活码")
        self.main_layout.addWidget(self.loginbutton)
        self.loginbutton.clicked.connect(self.get_verify_code)



    def get_verify_code(self):
        Etherstr = ''
        Etheraddress = self.get_value('macadress')
        etable = {'A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
        for c in Etheraddress:
            if c != '-' and c != ':': 
                if c.isalpha():
                    try:
                        Etherstr += str(int(etable[c.upper()])%10)
                    except Exception as e: 
                        QMessageBox.critical(
                            None,
                            '错误',
                            '存在非法字符')            
                else:
                    Etherstr += c  

        if len(Etherstr) == 12:
            i = 1
            sum = 0
            for x in Etherstr:
                sum += i*int(x)
                i += 1

            index = sum%10
            licence = ''
            i = 0
            for x in Etherstr:
                licence += str(self.maptable[((index+i+int(x))%10)][int(x)])
                i += 1

            self.activationcode.setText(licence)
            return licence
        else:
            QMessageBox.critical(
                            None,
                            '错误',
                            '物理地址必须为12个')

    def get_value(self, object_name):
        try:
            return self.findChild(QLineEdit, object_name).text()
        except Exception as e:
            print(object_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    get_activation_widget = ActivationWidget()
    get_activation_widget.show()
    sys.exit(app.exec_())
                


    

    


    

    