'''
    this file serves as the Controller between Front and Back end
'''

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
        self.ui.btn_flush.clicked.connect(self.flush)
        self.ui.btn_save.clicked.connect(self.save)

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

    def _get_creation_attributes(self) -> dict:
        attributes = {}
        attributes['chain'] = self.ui.comboBoxChain.currentText()
        attributes['target'] = action = self.ui.comboBoxAction.currentText()
        attributes['option'] = self.ui.comboBoxOption.currentText()
        attributes['protocol'] = self.ui.comboBoxProtocol.currentText()
        attributes['dport'] = self.ui.spinBox_dPort.value()
        attributes['sport'] = self.ui.spinBox_sPort.value()
        attributes['source'] = self.ui.txt_sourceIp.text()
        attributes['destination'] = self.ui.txt_destIp.text()
        self._convert_into_create_rule_args(attributes)
        return attributes

    def _convert_into_create_rule_args(self, attributes):
        bottom = attributes.pop('option')
        attributes['bottom'] = bottom

    def create_rule(self):
        attributes = self._get_creation_attributes()
        self.reset_creation()
        if attributes['chain'] == '--' or attributes['bottom'] == '--' or attributes['target'] == '--':
            return
        if attributes['protocol'] == '--':
            DEFAULT_ARG_FOR_PROTOCOL = ''
            attributes['protocol'] = DEFAULT_ARG_FOR_PROTOCOL

        possibilities = ('-I', '-A')
        selected_action = attributes['bottom']
        attributes['bottom'] = bool(possibilities.index(selected_action))

        try:
            self.firewall.create_rule(**attributes)
        except Firewall.CommandError as exception:
            self.handle(exception)
        
        self.read_rules()

    def read_rules(self):
        table = []
        SHIFT_INDEX_RIGHT = +1
        try:
            table = self.firewall.read_rules(self.ui.comboBoxRead.currentText())
        except Firewall.CommandError as exception:
            self.handle(exception)

        self.ui.tableWidget.clear()
        if len(table) == 0:
            self.ui.tableWidget.setRowCount(SHIFT_INDEX_RIGHT)
            return

        self.ui.tableWidget.setRowCount(len(table))
        HIDDEN_COL_INDEX = 2
        for i, line in enumerate(table):
            line.pop(HIDDEN_COL_INDEX)
            for j, word in enumerate(line):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(word))

    def delete_rule(self):
        chain = self.ui.comboBoxRead.currentText()
        number = self.ui.spinBoxSelection.value()
        self.reset_deletion()
        try:
            NO_SELECTION = 0
            self.firewall.delete_rule(chain, number)
            self.ui.spinBoxSelection.setValue(NO_SELECTION)
            self.read_rules()
        except Firewall.CommandError as exception:
            self.handle(exception)

    def handle(self, exception):
        print(exception)

    def reset_creation(self):
        FIRST_INDEX = 0
        INVALID_PORT = 0
        DEFAULT_TEXT = '--'
        self.ui.comboBoxChain.setCurrentIndex(FIRST_INDEX)
        self.ui.comboBoxAction.setCurrentIndex(FIRST_INDEX)
        self.ui.comboBoxOption.setCurrentIndex(FIRST_INDEX)
        self.ui.comboBoxProtocol.setCurrentIndex(FIRST_INDEX)
        self.ui.txt_destIp.setText(DEFAULT_TEXT)
        self.ui.txt_sourceIp.setText(DEFAULT_TEXT)
        self.ui.spinBox_sPort.setValue(INVALID_PORT)
        self.ui.spinBox_dPort.setValue(INVALID_PORT)

    def reset_deletion(self):
        INVALID_INDEX = 0
        self.ui.spinBoxSelection.setValue(INVALID_INDEX)
    
    def flush(self):
        self.firewall.flush()

    def save(self):
        self.firewall.save()
