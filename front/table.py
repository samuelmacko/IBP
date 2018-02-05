from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView


class Table(QTableWidget):

    def __init__(self, parent, data_list, list_headers):
        super(Table, self).__init__(parent)
        self._set_data(data_list=data_list, list_headers=list_headers)

    def _set_data(self, data_list, list_headers):

        self.resize(500, 500)
        self.setRowCount(len(data_list))
        self.setColumnCount(len(data_list[0]))

        self.setHorizontalHeaderLabels(list_headers)

        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSortIndicatorShown(True)

        for n, line in enumerate(data_list):
            for m, row in enumerate(data_list[n]):
                item = QTableWidgetItem(row)
                self.setItem(n, m, item)

        self.show()
