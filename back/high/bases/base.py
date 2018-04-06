# from back.suplementary.build_classes import BuildClasses
# from back.low.vm import *
# from back.low.disks import *
from back.low.host import *
from back.suplementary.filter_restrictions import FilterRestrictions


class HighBase(object):

    def __init__(self, connection, build_classes):
        self._connection = connection
        self.col_flags = []
        self.row_flags = []
        self.data_list = None
        self.headers_list = None
        # self.data_list = []
        # self.headers_list = []
        self.current_data_list = []
        self.current_headers_list = []

        self.build_classes = build_classes
        self.statistics = False

        self.filter_restrictions = None

        self.construct_table()

    # def construct_table(self):
    #     table = []
    #     # header = ['name']
    #     header = []
    #
    #     vms_list = VmList(connection=self._connection).list()
    #
    #     for n, vm_row in enumerate(vms_list):
    #         self.row_flags.append(1)
    #         table_row = []
    #
    #         # vm = vm_low(connection=self._connection, id=vm_row.id,
    #         #             statistics_class=VmStatistic)
    #         entity = self.build_classes(
    #             connection=self._connection, id=vm_row.id,
    #             statistics_class=VmStatistic
    #         )
    #
    #         for method in entity.methods_list():
    #             cell = method()
    #             if n == 0:
    #                 header.append(cell.name)
    #             table_row.append(cell.value)
    #         for statistic in entity.statistics():
    #             if n == 0:
    #                 header.append(statistic.name)
    #             table_row.append(statistic.value)
    #         table.append(table_row)
    #
    #     self.data_list = table
    #     self.headers_list = header

    def construct_table(self):
        table = []
        header = []
        # print('ent:', len(entity.statistics())) nie tuna
        entity_list = self.build_classes.list_class(
            connection=self._connection).list()

        for n, entity_row in enumerate(entity_list):
            self.row_flags.append(1)
            table_row = []

            entity = self.build_classes.entity_class(
                connection=self._connection, id=entity_row.id
            )

            for method in entity.methods_list():
                cell = method()
                if n == 0:
                    header.append(cell.name)
                table_row.append(cell.value)

            # if self.build_classes.entity_class is Host:
            #     print('aaaaaaa')
            #     continue

            # aaa = entity.statistics()
            # for statistic in aaa:
            if self.statistics:
                for statistic in entity.statistics():
                    if n == 0:
                        header.append(statistic.name)
                    table_row.append(statistic.value)

            table.append(table_row)

        self.data_list = table
        self.headers_list = header

    def table_from_flags(self):
        # headers = []
        # data = []
        self.current_headers_list = []
        self.current_data_list = []

        for i, flag in enumerate(self.col_flags):
            if flag == 1:
                self.current_headers_list.append(self.headers_list[i])

        for j, row in enumerate(self.data_list):
            if self.row_flags[j]:
                data_row = []
                for i, flag in enumerate(self.col_flags):
                    if flag == 1:
                        data_row.append(row[i])
                self.current_data_list.append(data_row)

        # return headers, data

    def validate_filter(self, filter):
        # str_col = [1, 2, 3, 4, 7, 8, 18, 24]
        # float_col = [5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21,
        #              22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

        if filter.column in self.filter_restrictions.str_col and \
            filter.operand == '=' and isinstance(filter.value, str):
            # filter.operand is operator.eq and isinstance(filter.value, str):
            return True

        if filter.column in self.filter_restrictions.float_col:
            try:
                float(filter.value)
                return True
            except ValueError:
                return False

        return False
