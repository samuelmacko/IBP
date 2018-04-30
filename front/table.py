

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore


class Table(QTableWidget):

    def __init__(self, parent, data_list, headers_list, sort=None):
        super(Table, self).__init__(parent)
        self.header = self.horizontalHeader()
        self.header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.header.setSortIndicatorShown(True)
        self.sort = sort
        self._set_data(data_list=data_list, headers_list=headers_list)

    def _set_data(self, data_list, headers_list):

        self.resize(500, 500)

        self.setRowCount(0)
        self.setColumnCount(len(headers_list))
        self.setHorizontalHeaderLabels(headers_list)

        self.header.setSectionResizeMode(QHeaderView.ResizeToContents)

        if data_list:
            self.setRowCount(len(data_list))
            self.setColumnCount(len(data_list[0]))
            self.setHorizontalHeaderLabels(headers_list)

            for n, line in enumerate(data_list):
                for m, col in enumerate(data_list[n]):
                    if col:
                        if isinstance(col, list):
                            item = QTableWidgetItem(
                                str(col[0]) + ' (' + str(len(col) - 1) + ')')
                        else:
                            item = QTableWidgetItem(str(col))
                    else:
                        item = QTableWidgetItem('')
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.setItem(n, m, item)
                    self.setAlternatingRowColors(True)

        if self.sort:
            self.header.setSortIndicator(self.sort[0], self.sort[1])

        self.show()
