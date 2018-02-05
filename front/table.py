from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView


class Table(QTableWidget):

    def __init__(self, parent, data_list, headers_list):
        super(Table, self).__init__(parent)
        self._set_data(data_list=data_list, headers_list=headers_list)

    def _set_data(self, data_list, headers_list):

        self.resize(500, 500)
        self.setRowCount(len(data_list))
        self.setColumnCount(len(data_list[0]))

        self.setHorizontalHeaderLabels(headers_list)
        # just_data = data_list
        # del data_list[0]
        # del just_data[0]

        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        header.setSortIndicatorShown(True)

        for n, line in enumerate(data_list):
            for m, row in enumerate(data_list[n]):
        # for n, line in enumerate(just_data):
        #     for m, row in enumerate(just_data[n]):
                item = QTableWidgetItem(row)
                self.setItem(n, m, item)

        self.show()
