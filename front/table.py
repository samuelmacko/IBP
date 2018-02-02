from PyQt4 import QtGui


class Table(QtGui.QTableWidget):

    def __init__(self, data_list, list_headers):
        super(Table, self).__init__()
        self._set_data(data_list=data_list, list_headers=list_headers)

    def _set_data(self, data_list, list_headers):

        self.resize(500, 500)
        self.setRowCount(len(data_list))
        self.setColumnCount(len(data_list[0]))

        self.setHorizontalHeaderLabels(list_headers)

        for n, line in enumerate(data_list):
            for m, row in enumerate(data_list[n]):
                item = QtGui.QTableWidgetItem(str(row))
                self.setItem(n, m, item)

        self.show()
