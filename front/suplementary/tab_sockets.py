from back.high.bases.custom_comparsion import Comparison
from front.suplementary.filter_handle import FilterHandle
from front.table import Table


# from front.main_window import Ui_MainWindow as mw


class Tabs(object):

    def __init__(self, table, parent):
        self.parent = parent
        self.chbox_list = []
        self.line_edit = None
        self.table = table
        self.printed_table = None
        self.table_layout = None

        # self.col = None
        self.column_order = False

    def print_table(self):
        self.table.table_from_flags()

        if self.table_layout.count() > 1:
            self.table_layout.removeWidget(self.printed_table)
        self.printed_table = Table(
                parent=self.parent, data_list=self.table.current_data_list,
                headers_list=self.table.current_headers_list)
        self.table_layout.addWidget(self.printed_table)

    def checkbox_handle(self, sender):
        # print('check box handle')
        for i, ch_box in enumerate(self.chbox_list):
            if sender == ch_box and i < len(self.chbox_list):
                if self.table.col_flags[i+1] == 1:
                    self.table.col_flags[i+1] = 0
                else:
                    self.table.col_flags[i+1] = 1

        # self.table.table_from_flags()
        self.print_table()

    def line_edit_handle(self, sender):
        # print('line edit handle')
        text = sender.text()
        self.table.row_flags = [1 for _ in
                                range(len(self.table.row_flags))]

        if text == '':
            self.print_table()
            return

        # try:
        for single_filter in text.split(','):
            filter_handler = FilterHandle(table=self.table)
            filter = filter_handler.process_filter(text=single_filter)

            if filter and self.table.validate_filter(filter=filter):
                filter_handler.apply_filter(filter=filter)
                # headers, data = filter_handler.table_from_flags()
                self.table.table_from_flags()
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
        for i, flag in enumerate(self.table.col_flags):
            if flag:
                shift += 1
            if shift == col:
                col = i
                break

        # print('sh col:', col)

        def temp(value):
            return Comparison(value[0][col])

        rows_flags = zip(
            self.table.data_list, self.table.row_flags)
        rows_flags = sorted(rows_flags, key=temp, reverse=self.column_order)
        self.table.data_list = [x[0] for x in rows_flags]
        self.table.row_flags = [x[1] for x in rows_flags]
        self.column_order = not self.column_order

        # self.table.table_from_flags()
        self.print_table()


class VmTab(Tabs):

    def __init__(self, table, parent):
        super(VmTab, self).__init__(table=table, parent=parent)


class DiskTab(Tabs):

    def __init__(self, table, parent):
        super(DiskTab, self).__init__(table=table, parent=parent)


class HostTab(Tabs):

    def __init__(self, table, parent):
        super(HostTab, self).__init__(table=table, parent=parent)


class TpltTab(Tabs):

    def __init__(self, table, parent):
        super(TpltTab, self).__init__(table=table, parent=parent)





