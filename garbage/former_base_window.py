# from PyQt4 import QtGui
# from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem


class BaseWindow(QWidget):

    # def __init__(self):
    #     super(BaseWindow, self).__init__()
    #     self.initUI()

    def __init__(self, data_list, list_headers):
        super(BaseWindow, self).__init__()
        self.initUI(data_list=data_list, list_headers=list_headers)

    def initUI(self, data_list, list_headers):
    # def initUI(self):
        # QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        # btn = QtGui.QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())
        # btn.move(50, 50)

        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle('Ovirt data presenter')

        # table = Table(data_list=data_list, list_headers=list_headers)
        # table = QtGui.QTableWidget()

        # table.move(10, 10)

        # self.centralwidget =

        self.tableWidget = QTableWidget(self.centralwidget)

        self.tableWidget.setRowCount(len(data_list))
        self.tableWidget.setColumnCount(len(data_list[0]))

        self.tableWidget.setHorizontalHeaderLabels(list_headers)

        for n, line in enumerate(data_list):
            for m, row in enumerate(data_list[n]):
                item = QTableWidgetItem(str(row))
                # item = QTableWidgetItem(str(row))
                self.tableWidget.setItem(n, m, item)

        # layout = QtGui.QHBoxLayout()
        # layout.setContentsMargins(0, 0, 0, 0)
        # layout.setSpacing(0)
        # layout.addWidget(table)
        # self.setLayout(layout)

        # hbox = QtGui.QVBoxLayout()
        # hbox.addStretch(1)
        # hbox.addWidget(table)
        #
        # self.setLayout(hbox)


        # self.show()
