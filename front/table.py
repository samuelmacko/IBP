from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView


class Table(QTableWidget):

    def __init__(self, parent, data_list, headers_list):
    # def __init__(self, parent, table):
        super(Table, self).__init__(parent)
        self._set_data(data_list=data_list, headers_list=headers_list)
        # self.table = table
        # self._set_data()

    def _set_data(self, data_list, headers_list):
    # def _set_data(self):

        self.resize(500, 500)

        self.setRowCount(0)
        self.setColumnCount(len(headers_list))
        self.setHorizontalHeaderLabels(headers_list)

        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)

        if data_list:
            self.setRowCount(len(data_list))
            self.setColumnCount(len(data_list[0]))
            self.setHorizontalHeaderLabels(headers_list)

            for n, line in enumerate(data_list):
                for m, row in enumerate(data_list[n]):
                    item = QTableWidgetItem(row)
                    self.setItem(n, m, item)

        self.show()
