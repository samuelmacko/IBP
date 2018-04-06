from back.high.bases.base import HighBase
from back.suplementary.filter_restrictions import FilterRestrictions


class Host(HighBase):

    def __init__(self, connection, build_classes, col_flags=None):
        super(Host, self).__init__(connection=connection,
                                   build_classes=build_classes)
        if col_flags:
            self.col_flags = col_flags
        else:
            self.col_flags = [1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1]
        self.filter_restrictions = FilterRestrictions(
            str_col=[],
            float_col=[]
        )
        self.statistics = True

    # def construct_table(self):
    #     table = []
    #     header = []
    #
    #     hosts_list = HostList(connection=self._connection).list()
    #
    #     for n, host_row in enumerate(hosts_list):
    #         self.row_flags.append(1)
    #         table_row = []
    #
    #         host = host_low(connection=self._connection, id=host_row.id)
    #
    #         # table_row.append(host.name())
    #
    #         # method_dict = OrderedDict([
    #         #     ('_status', host._status), ('id', host.id),
    #         #     ('_address', host._address), ('_cluster', host._cluster),
    #         #     ('nic', host._nics)
    #         # ])
    #         # for method in method_dict.items():
    #         #     if n ==0:
    #         #         header.append(method[0])
    #         #     table_row.append(method[1]())
    #
    #         for method in host.methods_list():
    #             cell = method()
    #             if n == 0:
    #                 header.append(cell.name)
    #             table_row.append(cell.value)
    #
    #         # st_list = HostStatisticsList(
    #         #     connection=self._connection, id=host.id().value). \
    #         #     statistic_objects_list()
    #         # for i, value in enumerate(st_list):
    #         #     if value:
    #         #         if n == 0:
    #         #             header.append(st_list[i].name())
    #         #             # table.append(st_list[i].name())
    #         #         table_row.append(
    #         #             str(st_list[i].value()) + ' ' + str(st_list[i].unit())
    #         #         )
    #
    #         table.append(table_row)
    #
    #     self.data_list = table
    #     self.headers_list = header
    #
    #     # for n, host_row in enumerate(hosts_list):
    #     #     _host = host_low(connection=self._connection,
    #     #                     host_id=host_row.id)
    #     #     # self.row_flags.append(1)
    #     #     # table_row = []
    #     #
    #     #     _vms = _host._vms()
    #     #     if _vms:
    #     #         for vm in _vms:
    #     #             if n == 0:
    #     #                 header, row = self.create_row(
    #     #                     vm=vm, _host=_host, first_row=True)
    #     #
    #     #             else:
    #     #                 row = self.create_row(
    #     #                     vm=vm, _host=_host, first_row=False)
    #     #             # table_row = row
    #     #             table.append(row)
    #     #             # table_row.extend(row)
    #     #     else:
    #     #         if n == 0:
    #     #             header, row = self.create_row(
    #     #                 vm=None, _host=_host, first_row=True)
    #     #
    #     #         else:
    #     #             row = self.create_row(
    #     #                 vm=None, _host=_host, first_row=False)
    #     #         # table_row = row
    #     #             table.append(row)
    #     #     # table.append(table_row)
    #     #     # table.extend(table_row)
    #     #
    #     # self.data_list = table
    #     # # self.data_list.extend(table)
    #     # # self.current_data_list = self.data_list
    #     # self.headers_list = header
    #     # # self.headers_list.extend('a')
    #     # # self.headers_list.extend(header)

    # def create_row(self, vm, host, first_row):
    #
    #     self.row_flags.append(1)
    #
    #     table_row = []
    #     header = ['name']
    #
    #     table_row.append(host.name())
    #
    #     vm_st_names = ['vm', '_memory.installed', '_memory.used',
    #                    'cpu.current.guest', 'cpu.current.hypervisor',
    #                    'cpu.current.total', 'migration.progress',
    #                    '_memory.buffered', '_memory.cached',
    #                    '_memory.free']
    #
    #     if vm:
    #         if first_row:
    #             header.append('vm')
    #         table_row.append(vm.name)
    #
    #         vm_st_list = VmStatisticsList(
    #             connection=self._connection, id=vm.id). \
    #             statistic_objects_list()
    #         for i, value in enumerate(vm_st_list):
    #             if value:
    #                 if first_row:
    #                     header.append(vm_st_list[i].name())
    #                 table_row.append(
    #                     str(vm_st_list[i].value()) + ' '
    #                     + str(vm_st_list[i].unit())
    #                 )
    #     else:
    #         for i in range(len(vm_st_names)):
    #             if first_row:
    #                 # if i == 0:
    #                 #     header.append('vm')
    #                 header.append(vm_st_names[i])
    #             # table_row.append('')
    #             table_row.append(None)
    #
    #     method_dict = OrderedDict([
    #         ('_status', host._status), ('id', host.id),
    #         ('_address', host._address), ('_cluster', host._cluster),
    #         ('nic', host._nics)
    #     ])
    #     for i, method in enumerate(method_dict.items()):
    #         if first_row:
    #             header.append(method[0])
    #         if method[0] == 'nic':
    #             table_row.append(method[1]()[0].name)
    #             continue
    #         table_row.append(method[1]())
    #
    #     host_st_list = HostStatisticsList(
    #         connection=self._connection, id=host.id()). \
    #         statistic_objects_list()
    #     for i, value in enumerate(host_st_list):
    #         if value:
    #             if first_row:
    #                 header.append(host_st_list[i].name())
    #             table_row.append(
    #                 str(host_st_list[i].value()) + ' '
    #                 + str(host_st_list[i].unit())
    #             )
    #
    #     if first_row:
    #         return header, table_row
    #     else:
    #         return table_row

    # def validate_filter(self, filter):
    #     str_col = [1, 2, 12, 13, 14, 15, 16, ]
    #     float_col = [3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 18, 19, 20, 21, 22, 23,
    #                  24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
    #
    #     if filter.column in str_col and \
    #         filter.operand == '=' and isinstance(filter.value, str):
    #         return True
    #
    #     if filter.column in float_col:
    #         try:
    #             float(filter.value)
    #             return True
    #         except ValueError:
    #             return False
    #
    #     return False