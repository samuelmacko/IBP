from PyQt4 import QtGui


class BaseWindow(QtGui.QWidget):

    def __init__(self):
        super(BaseWindow, self).__init__()
        self.initUI()

    # def __init__(self, data_list, list_headers):
    #     super(BaseWindow, self).__init__()
    #     self.initUI(data_list=data_list, list_headers=list_headers)

    # def initUI(self, data_list, list_headers):
    def initUI(self):
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 500, 150)
        self.setWindowTitle('Ovirt data presenter')

        # table = Table(data_list=data_list, list_headers=list_headers)
        # table = QtGui.QTableWidget()

        # table.move(10, 10)

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
