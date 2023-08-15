import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import QModelIndex
import Firewall
import ParseFirewallOutput

from Ui_firewallGUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.firewall = Firewall.Firewall()
        self.read_rules()

        self.ui.spinBoxSelection.valueChanged.connect(self.sync_selection_spin_box)
        self.ui.tableWidget.itemSelectionChanged.connect(self.sync_spin_box_selection)

        self.ui.comboBoxRead.currentIndexChanged.connect(self.read_rules)
        self.ui.btn_display.clicked.connect(self.read_rules)
        self.ui.btn_create.clicked.connect(self.create_rule)
        self.ui.btn_delete.clicked.connect(self.delete_rule)
    
    def show(self):
        self.main_win.show()

    def sync_spin_box_selection(self):
        START_INDEX = +1
        index = self.ui.tableWidget.currentRow()
        self.ui.spinBoxSelection.setValue(index + START_INDEX)
    
    def sync_selection_spin_box(self):
        START_INDEX = -1
        index = self.ui.spinBoxSelection.value()
        self.ui.tableWidget.selectRow(index + START_INDEX)

    def create_rule(self):
        chain = self.ui.comboBoxChain.currentText()
        target = action = self.ui.comboBoxAction.currentText()
        option = self.ui.comboBoxOption.currentText()
        protocol = self.ui.comboBoxProtocol.currentText()
        port = self.ui.spinBoxPort.value()
        self.reset_creation()
        if chain == '--' or option == '--' or target == '--':
            return
        if protocol == '--':
            DEFAULT_ARG_FOR_PROTOCOL = ''
            protocol = DEFAULT_ARG_FOR_PROTOCOL

        possibilities = ('-I', '-A')
        option = bool(possibilities.index(option))

        try:
            self.firewall.create_rule(chain, target, bottom=option, protocol=protocol, port=port)
        except Firewall.CommandError as exception:
            self.handle(exception)

    def read_rules(self):
        SHIFT_INDEX_RIGHT = +1
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setHorizontalHeaderLabels(['Target', 'Protocol', 'Port'])
        try:
            table = self.firewall.read_rules(self.ui.comboBoxRead.currentText())
        except Firewall.CommandError as exception:
            self.handle(exception)

        if len(table) == 0:
            self.ui.tableWidget.setRowCount(1)
            return
        self.ui.tableWidget.setRowCount(len(table))
        for i, line in enumerate(table):
            self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(line[0]))
            self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(line[1]))
            self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(line[5]))

    def delete_rule(self):
        self.reset_deletion()
        START_INDEX = +1
        chain = self.ui.comboBoxRead.currentText()
        number = self.ui.tableWidget.currentRow() + START_INDEX
        try:
            self.firewall.delete_rule(chain, number)
        except Firewall.CommandError as exception:
            self.handle(exception)

    def handle(self, exception):
        print(exception)

    def reset_creation(self):
        FIRST_INDEX = 0
        INVALID_PORT = 0
        self.ui.comboBoxChain.setCurrentIndex(FIRST_INDEX)
        self.ui.comboBoxAction.setCurrentIndex(FIRST_INDEX)
        self.ui.comboBoxOption.setCurrentIndex(FIRST_INDEX)
        self.ui.comboBoxProtocol.setCurrentIndex(FIRST_INDEX)
        self.ui.spinBoxPort.setValue(INVALID_PORT)
    
    def reset_deletion(self):
        INVALID_INDEX = 0
        self.ui.spinBoxSelection.setValue(INVALID_INDEX)

