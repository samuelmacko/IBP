

from back.suplementary.custom_comparsion import Comparison
from front.suplementary.filter_handle import FilterHandler
from front.suplementary.compute_shift import compute_shift
from front.table import Table


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
        self.redirect_dict = None

        self.column_order = {}

    def print_table(self, sort=None):
        self.values_table.table_from_flags()

        if self.vertical_layouts.count() > 1:
            self.vertical_layouts.removeWidget(self.printed_table)
        self.printed_table = Table(
            parent=self.parent, data_list=self.values_table.current_data_list,
            headers_list=self.values_table.current_headers_list,
            sort=sort
        )

        self.vertical_layouts.addWidget(self.printed_table)

    def checkbox_handle(self, sender):
        for i, ch_box in enumerate(self.chbox_list):
            if sender == ch_box and i < len(self.chbox_list):
                if self.values_table.col_flags[i] == 1:
                    self.values_table.col_flags[i] = 0
                else:
                    self.values_table.col_flags[i] = 1

        self.print_table()

    def line_edit_handle(self, text):
        # print('txt:', text)
        self.values_table.row_flags = [
            1 for _ in range(len(self.values_table.row_flags))
        ]

        if text == '':
            self.print_table()
            return

        for single_filter in text.split(','):
            filter_handler = FilterHandler(
                table=self.values_table,
                filter_restrictions=self.values_table.filter_restrictions
            )
            filter = filter_handler.process_filter(text=single_filter)

            if filter:
                filter_handler.apply_filter(filter=filter)
                self.values_table.table_from_flags()
            else:
                print('wrong filter')
        self.print_table()

    def sort_column(self, col):
        # print('col:', col)

        # shift = -1
        # for i, flag in enumerate(self.values_table.col_flags):
        #     if flag:
        #         shift += 1
        #     if shift == col:
        #         col_shift = i
        #         break

        col_shift = compute_shift(
            col_flags=self.values_table.col_flags,
            current_col=col
        )

        if col_shift not in self.column_order:
            self.column_order[col_shift] = True

        # print('col_shift:', col_shift)

        def temp(value):
            return Comparison(value[0][col_shift])

        rows_flags = zip(
            self.values_table.data_list, self.values_table.row_flags
        )
        sorted_rows_flags = sorted(
            rows_flags, key=temp, reverse=self.column_order[col_shift]
        )
        self.values_table.data_list = [x[0] for x in sorted_rows_flags]
        self.values_table.row_flags = [x[1] for x in sorted_rows_flags]

        self.column_order[col_shift] = not self.column_order[col_shift]

        self.print_table(sort=(col, self.column_order[col_shift]))


class VMsTab(Tabs):

    def __init__(self, table, parent):
        super(VMsTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {
            4: (4, 5), 6: (2, 6), 10: (6, 8), 11: (1, 7), 12: (7, 4),
            13: (8, 6), 14: (3, 10)
        }


class DisksTab(Tabs):

    def __init__(self, table, parent):
        super(DisksTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {7: (0, 11), 9: (3, 11), 10: (6, 10)}


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
        self.redirect_dict = {
            3: (5, 6), 4: (2, 4), 5: (0, 4), 9: (8, 4), 10: (6, 3)
        }


class DataCentersTab(Tabs):

    def __init__(self, table, parent):
        super(DataCentersTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {4: (3, 9), 5: (8, 2), 6: (4, 3), 7: (6, 5)}


class TemplatesTab(Tabs):

    def __init__(self, table, parent):
        super(TemplatesTab, self).__init__(table=table, parent=parent)
        self.redirect_dict = {
            3: (4, 10), 5: (5, 7), 8: (0, 10), 9: (7, 5), 10: (1, 10),
            11: (8, 7), 12: (3, 12)
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
