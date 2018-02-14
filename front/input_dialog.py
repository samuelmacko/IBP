# from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets, QtCore

import ovirtsdk4 as sdk


class InputDialog(QtWidgets.QWidget):

    def __init__(self):
        super(InputDialog, self).__init__()
        self.connection = None

        self.initUI()

    def initUI(self):
        self.resize(700, 100)
        self.setWindowTitle('Input')

        self.username_input = QtWidgets.QLineEdit('admin@internal', self)
        self.username_input.setPlaceholderText('username')
        self.password_input = QtWidgets.QLineEdit('qum5net', self)
        self.password_input.setPlaceholderText('password')
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.url_input = QtWidgets.QLineEdit(
            'https://10-37-137-222.rhev.lab.eng.brq.redhat.com/ovirt-engine/api', self)
        self.url_input.setPlaceholderText('url')

        self.layout_1 = QtWidgets.QVBoxLayout(self)
        self.layout_1.addWidget(self.username_input)
        self.layout_1.addWidget(self.password_input)
        self.layout_1.addWidget(self.url_input)

        self.layout_2 = QtWidgets.QHBoxLayout()

        self.ok_btn = QtWidgets.QPushButton('ok', self)
        self.ok_btn.clicked['bool'].connect(self.ok_btn_clicked)
        self.cancel_btn = QtWidgets.QPushButton('cancel', self)
        self.cancel_btn.clicked['bool'].connect(self.cancel_btn_clicked)

        self.layout_2.addWidget(self.ok_btn)
        self.layout_2.addWidget(self.cancel_btn)

        self.layout_1.addLayout(self.layout_2)

        self.show()

        while not self.connection:
            QtCore.QCoreApplication.processEvents()

        self.ok_btn.setDisabled(True)
        self.cancel_btn.setDisabled(True)

    def ok_btn_clicked(self, clicked):
        username = self.username_input.text()
        password = self.password_input.text()
        url = self.url_input.text()

        connection = sdk.Connection(
            username=username, password=password, insecure=True,
            url=url,
            # ca_file=ca_file,
        )
        if connection.test(raise_exception=False):
            self.connection = connection
        else:
            print('chybne udaje')
            self.username_input.setText('')
            self.password_input.setText('')
            self.url_input.setText('')

    def cancel_btn_clicked(self, clicked):
        print('cancel')
        self.username_input.setText('')
        self.password_input.setText('')
        self.url_input.setText('')

    def get_connection(self):
        return self.connection

    def closeEvent(self, QCloseEvent):
        #todo zleeeee
        exit(0)

