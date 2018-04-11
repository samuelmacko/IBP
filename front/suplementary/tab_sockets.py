from back.suplementary.custom_comparsion import Comparison
from front.suplementary.filter_handle import FilterHandler
from front.table import Table
from PyQt5 import QtCore, QtWidgets, QtGui


# from front.main_window import Ui_MainWindow as mw


class Tabs(object):

    def __init__(self, table, parent):
        self.parent = parent
        self.values_table = table
        self.printed_table = None

        self.table_layout = None

        self.chbox_list = []
        self.line_edit = None
        self.horizontal_layouts = [None] * 2
        self.vertical_layouts = None
        self.tab_widget = None
        self.tool_btn = None
        self.tool_menu = None
        self.refresh_btn = None

        # self.redirects = {}
        self.redirect_dict = None

        # self.col = None
        self.column_order = {}

    def print_table(self):
        self.values_table.table_from_flags()

        # if self.table_layout.count() > 1:
        if self.vertical_layouts.count() > 1:
            # self.table_layout.removeWidget(self.printed_table)
            self.vertical_layouts.removeWidget(self.printed_table)
        self.printed_table = Table(
                parent=self.parent, data_list=self.values_table.current_data_list,
                headers_list=self.values_table.current_headers_list
        )

        # self.table_layout.addWidget(self.printed_table)
        self.vertical_layouts.addWidget(self.printed_table)

    def checkbox_handle(self, sender):
        # print('check box handle')
        for i, ch_box in enumerate(self.chbox_list):
            if sender == ch_box and i < len(self.chbox_list):
                # if self.values_table.col_flags[i+1] == 1:
                #     self.values_table.col_flags[i + 1] = 0
                # else:
                #     self.values_table.col_flags[i + 1] = 1
                if self.values_table.col_flags[i] == 1:
                    self.values_table.col_flags[i] = 0
                else:
                    self.values_table.col_flags[i] = 1

        # self.table.table_from_flags()
        self.print_table()

    def line_edit_handle(self, text):
        # print('line edit handle')
        # text = sender.text()
        print('txt:', text)
        self.values_table.row_flags = [
            1 for _ in range(len(self.values_table.row_flags))
        ]

        if text == '':
            self.print_table()
            return

        # try:
        for single_filter in text.split(','):
            filter_handler = FilterHandler(
                table=self.values_table,
                filter_restrictions=self.values_table.filter_restrictions
            )
            filter = filter_handler.process_filter(text=single_filter)

            # if filter and self.values_table.validate_filter(filter=filter):
            if filter:
                filter_handler.apply_filter(filter=filter)
                # headers, data = filter_handler.table_from_flags()
                self.values_table.table_from_flags()
            # else:
            #     raise Exception
            else:
                print('wrong filter')
        self.print_table()
        # except Exception as e:
        #     print('wrong filter:', e)

    def sort_column(self, col):
        print('col:', col)

        shift = -1
        for i, flag in enumerate(self.values_table.col_flags):
            if flag:
                shift += 1
            if shift == col:
                col_shift = i
                break
        # col_shift = col

        if col_shift not in self.column_order:
            self.column_order[col_shift] = True

        print('col_shift:', col_shift)

        def temp(value):
            return Comparison(value[0][col_shift])

        rows_flags = zip(
            self.values_table.data_list, self.values_table.row_flags
        )
        sorted_rows_flags = sorted(
            rows_flags, key=temp, reverse=self.column_order[col_shift]
        )
        # print('sorted_row_flags:', sorted_rows_flags)
        # rows_flags.sort(
        #     rows_flags, key=temp, reverse=self.column_order[col_shift]
        # )
        self.values_table.data_list = [x[0] for x in sorted_rows_flags]
        self.values_table.row_flags = [x[1] for x in sorted_rows_flags]

        # self.table.table_from_flags()
        self.print_table()

        self.printed_table.header.setSortIndicator(
            col, self.column_order[col_shift])
        # self.column_order = not self.column_order
        self.column_order[col_shift] = not self.column_order[col_shift]

    # def redirect(self, row, col):
    #     if col in self.redirect_dict:



class VMsTab(Tabs):

    def __init__(self, table, parent):
        super(VMsTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {
            4: (4, 5), 6: (2, 6), 10: (6, 8), 11: (1, 7), 12: (7, 4),
            13: (8, 6)
        }


class DisksTab(Tabs):

    def __init__(self, table, parent):
        super(DisksTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {7: (0, 11)}


class HostsTab(Tabs):

    def __init__(self, table, parent):
        super(HostsTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {4: (4, 4), 5: (7, 8), 6: (0, 6), 7: (8, 5)}


class StorageDomainsTab(Tabs):

    def __init__(self, table, parent):
        super(StorageDomainsTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {9: (5, 4), 10: (0, 14), 11: (1, 9), 12: (6, 5)}


class ClustersTab(Tabs):

    def __init__(self, table, parent):
        super(ClustersTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {3: (5, 6), 4: (2, 4), 5: (0, 4), 9: (8, 4)}


class DataCentersTab(Tabs):

    def __init__(self, table, parent):
        super(DataCentersTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {4: (3, 9), 5: (8, 2), 6: (4, 3)}


class TemplatesTab(Tabs):

    def __init__(self, table, parent):
        super(TemplatesTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {
            3: (4, 10), 5: (5, 7), 8: (0, 10), 9: (7, 5), 10: (1, 10)
        }


class NICsTab(Tabs):

    def __init__(self, table, parent):
        super(NICsTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {2: (5, None), 3: (8, 3), 4: (0, 12), 5: (6, 9)}


class NetworksTab(Tabs):

    def __init__(self, table, parent):
        super(NetworksTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {
            2: (5, 5), 3: (7, 3), 4: (4, 9), 5: (2, 7), 6: (0, 13), 7: (6, 11)
        }
