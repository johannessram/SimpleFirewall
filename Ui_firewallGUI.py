# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firewallGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 680)
        MainWindow.setMinimumSize(QtCore.QSize(800, 680))
        MainWindow.setMaximumSize(QtCore.QSize(800, 680))
        MainWindow.setStyleSheet("background-color:#009999;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 131, 31))
        self.label.setStyleSheet("font-size:18px;\n"
"font-weight:bold;")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 40, 741, 181))
        self.groupBox.setStyleSheet("border:3px solid white;\n"
"font-size:15px;\n"
"background-color:#336699;\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.comboBoxChain = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxChain.setGeometry(QtCore.QRect(40, 50, 91, 31))
        self.comboBoxChain.setStyleSheet("border:none;\n"
"background-color:white;\n"
"color:black;")
        self.comboBoxChain.setFrame(False)
        self.comboBoxChain.setObjectName("comboBoxChain")
        self.comboBoxChain.addItem("")
        self.comboBoxChain.addItem("")
        self.comboBoxChain.addItem("")
        self.comboBoxChain.addItem("")
        self.comboBoxOption = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxOption.setGeometry(QtCore.QRect(40, 120, 91, 31))
        self.comboBoxOption.setStyleSheet("border:none;\n"
"background-color:white;\n"
"padding-left:10px;\n"
"color:black;")
        self.comboBoxOption.setObjectName("comboBoxOption")
        self.comboBoxOption.addItem("")
        self.comboBoxOption.addItem("")
        self.comboBoxOption.addItem("")
        self.comboBoxProtocol = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxProtocol.setGeometry(QtCore.QRect(170, 50, 101, 31))
        self.comboBoxProtocol.setStyleSheet("border:none;\n"
"background-color:white;\n"
"padding-left:10px;\n"
"color:black;")
        self.comboBoxProtocol.setObjectName("comboBoxProtocol")
        self.comboBoxProtocol.addItem("")
        self.comboBoxProtocol.addItem("")
        self.comboBoxProtocol.addItem("")
        self.comboBoxProtocol.addItem("")
        self.comboBoxAction = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxAction.setGeometry(QtCore.QRect(170, 120, 101, 31))
        self.comboBoxAction.setStyleSheet("background-color:white;\n"
"border:none;\n"
"padding-left:10px;\n"
"color:black;")
        self.comboBoxAction.setObjectName("comboBoxAction")
        self.comboBoxAction.addItem("")
        self.comboBoxAction.addItem("")
        self.comboBoxAction.addItem("")
        self.comboBoxAction.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 61, 16))
        self.label_2.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 61, 21))
        self.label_3.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(180, 20, 81, 31))
        self.label_4.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(190, 100, 61, 16))
        self.label_5.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"")
        self.label_5.setObjectName("label_5")
        self.btn_create = QtWidgets.QPushButton(self.groupBox)
        self.btn_create.setGeometry(QtCore.QRect(610, 120, 91, 31))
        self.btn_create.setStyleSheet("background-color: #009933;\n"
"border:none;\n"
"border-radius:10px;\n"
"color:white;")
        self.btn_create.setObjectName("btn_create")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(320, 90, 91, 31))
        self.label_8.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(310, 20, 111, 31))
        self.label_9.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(480, 90, 71, 31))
        self.label_10.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.txt_destIp = QtWidgets.QLineEdit(self.groupBox)
        self.txt_destIp.setGeometry(QtCore.QRect(460, 120, 111, 31))
        self.txt_destIp.setAutoFillBackground(False)
        self.txt_destIp.setStyleSheet("background-color:white;\n"
"border:none;\n"
"color:black;")
        self.txt_destIp.setMaxLength(15)
        self.txt_destIp.setObjectName("txt_destIp")
        self.spinBox_sPort = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_sPort.setGeometry(QtCore.QRect(310, 50, 111, 31))
        self.spinBox_sPort.setStyleSheet("background-color:white;\n"
"border:none;\n"
"padding-left:5px;\n"
"color:black;")
        self.spinBox_sPort.setMaximum(99999)
        self.spinBox_sPort.setObjectName("spinBox_sPort")
        self.txt_sourceIp = QtWidgets.QLineEdit(self.groupBox)
        self.txt_sourceIp.setGeometry(QtCore.QRect(460, 50, 111, 31))
        self.txt_sourceIp.setAutoFillBackground(False)
        self.txt_sourceIp.setStyleSheet("background-color:white;\n"
"border:none;\n"
"color:black;")
        self.txt_sourceIp.setMaxLength(15)
        self.txt_sourceIp.setObjectName("txt_sourceIp")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(470, 20, 101, 31))
        self.label_11.setStyleSheet("border:none;\n"
"font-size:20px;\n"
"")
        self.label_11.setObjectName("label_11")
        self.spinBox_dPort = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_dPort.setGeometry(QtCore.QRect(310, 120, 111, 31))
        self.spinBox_dPort.setStyleSheet("background-color:white;\n"
"border:none;\n"
"padding-left:5px;\n"
"color:black;")
        self.spinBox_dPort.setMaximum(99999)
        self.spinBox_dPort.setObjectName("spinBox_dPort")
        self.comboBoxChain.raise_()
        self.comboBoxOption.raise_()
        self.comboBoxAction.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.btn_create.raise_()
        self.label_8.raise_()
        self.comboBoxProtocol.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.txt_destIp.raise_()
        self.spinBox_sPort.raise_()
        self.label_11.raise_()
        self.txt_sourceIp.raise_()
        self.spinBox_dPort.raise_()
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 741, 391))
        self.groupBox_2.setStyleSheet("border:3px solid white;\n"
"font-size:15px;\n"
"background-color:#336699;\n"
"font:white;")
        self.groupBox_2.setObjectName("groupBox_2")
        self.comboBoxRead = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBoxRead.setGeometry(QtCore.QRect(40, 40, 91, 31))
        self.comboBoxRead.setStyleSheet("border:none;\n"
"color:black;\n"
"background-color:white;\n"
"")
        self.comboBoxRead.setFrame(False)
        self.comboBoxRead.setObjectName("comboBoxRead")
        self.comboBoxRead.addItem("")
        self.comboBoxRead.addItem("")
        self.comboBoxRead.addItem("")
        self.btn_display = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_display.setGeometry(QtCore.QRect(220, 40, 91, 31))
        self.btn_display.setStyleSheet("background-color:#ff9900;\n"
"border:none;\n"
"border-radius:10px;\n"
"color:white;")
        self.btn_display.setObjectName("btn_display")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(40, 90, 661, 181))
        self.scrollArea.setStyleSheet("border:none;\n"
"background-color:#85adad;\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 661, 181))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 651, 181))
        self.tableWidget.setMaximumSize(QtCore.QSize(651, 16777215))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(208)
        self.tableWidget.verticalHeader().setDefaultSectionSize(38)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.btn_delete = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_delete.setGeometry(QtCore.QRect(610, 330, 91, 31))
        self.btn_delete.setStyleSheet("border:none;\n"
"background-color:#cc0000;\n"
"border-radius:10px;\n"
"color:white;")
        self.btn_delete.setObjectName("btn_delete")
        self.spinBoxSelection = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBoxSelection.setGeometry(QtCore.QRect(491, 331, 61, 31))
        self.spinBoxSelection.setStyleSheet("background-color:white;\n"
"border:none;\n"
"padding-left:5px;\n"
"color:black;")
        self.spinBoxSelection.setObjectName("spinBoxSelection")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(40, 250, 661, 61))
        self.label_7.setStyleSheet("font-size:25px;\n"
"border:none;\n"
"font-weight:bold;")
        self.label_7.setObjectName("label_7")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(40, 330, 301, 21))
        self.label_12.setStyleSheet("font-size:13px;\n"
"border:none;")
        self.label_12.setObjectName("label_12")
        self.comboBoxRead.raise_()
        self.btn_display.raise_()
        self.btn_delete.raise_()
        self.spinBoxSelection.raise_()
        self.label_7.raise_()
        self.scrollArea.raise_()
        self.label_12.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "MY FIREWALL"))
        self.groupBox.setTitle(_translate("MainWindow", "CREATE RULE"))
        self.comboBoxChain.setItemText(0, _translate("MainWindow", "--"))
        self.comboBoxChain.setItemText(1, _translate("MainWindow", "INPUT"))
        self.comboBoxChain.setItemText(2, _translate("MainWindow", "OUTPUT"))
        self.comboBoxChain.setItemText(3, _translate("MainWindow", "FORWARD"))
        self.comboBoxOption.setItemText(0, _translate("MainWindow", "--"))
        self.comboBoxOption.setItemText(1, _translate("MainWindow", "-A"))
        self.comboBoxOption.setItemText(2, _translate("MainWindow", "-I"))
        self.comboBoxProtocol.setItemText(0, _translate("MainWindow", "--"))
        self.comboBoxProtocol.setItemText(1, _translate("MainWindow", "tcp"))
        self.comboBoxProtocol.setItemText(2, _translate("MainWindow", "udp"))
        self.comboBoxProtocol.setItemText(3, _translate("MainWindow", "icmp"))
        self.comboBoxAction.setItemText(0, _translate("MainWindow", "--"))
        self.comboBoxAction.setItemText(1, _translate("MainWindow", "ACCEPT"))
        self.comboBoxAction.setItemText(2, _translate("MainWindow", "REJECT"))
        self.comboBoxAction.setItemText(3, _translate("MainWindow", "DROP"))
        self.label_2.setText(_translate("MainWindow", "chain"))
        self.label_3.setText(_translate("MainWindow", "option"))
        self.label_4.setText(_translate("MainWindow", "protocol"))
        self.label_5.setText(_translate("MainWindow", "action"))
        self.btn_create.setText(_translate("MainWindow", "CREATE"))
        self.label_8.setText(_translate("MainWindow", "dest port"))
        self.label_9.setText(_translate("MainWindow", "source port"))
        self.label_10.setText(_translate("MainWindow", "dest IP"))
        self.txt_destIp.setText(_translate("MainWindow", "--"))
        self.txt_sourceIp.setText(_translate("MainWindow", "--"))
        self.label_11.setText(_translate("MainWindow", "source IP"))
        self.groupBox_2.setTitle(_translate("MainWindow", "READ OR DELETE RULE"))
        self.comboBoxRead.setItemText(0, _translate("MainWindow", "INPUT"))
        self.comboBoxRead.setItemText(1, _translate("MainWindow", "OUTPUT"))
        self.comboBoxRead.setItemText(2, _translate("MainWindow", "FORWARD"))
        self.btn_display.setText(_translate("MainWindow", "DISPLAY"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Target"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Destination"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "SourcePort"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "DestPort"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.btn_delete.setText(_translate("MainWindow", "DELETE"))
        self.label_7.setText(_translate("MainWindow", "_______________________________________________________"))
        self.label_12.setText(_translate("MainWindow", "select the index of the rule you wish to delete"))
