from back.high.bases.base import HighBase


class Vm(HighBase):

    def __init__(self, connection, build_classes, col_flags=None):
        super(Vm, self).__init__(
            connection=connection, build_classes=build_classes
        )
        if col_flags:
            self.col_flags = col_flags
        else:
            self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.filter_restrictions = {0, 1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14}
        self.statistics = True


    # def construct_table(self):
    #     table = []
    #     # header = ['name']
    #     header = []
    #
    #     vms_list = self.build_classes.list_class(
    #         connection=self._connection).list()
    #
    #     for n, vm_row in enumerate(vms_list):
    #         self.row_flags.append(1)
    #         table_row = []
    #
    #         # vm = vm_low(connection=self._connection, id=vm_row.id,
    #         #             statistics_class=VmStatistic)
    #         entity = self.build_classes.entity_class(
    #             connection=self._connection, id=vm_row.id
    #         )
    #
    #         for method in entity.methods_list():
    #             cell = method()
    #             if n == 0:
    #                 header.append(cell.name)
    #             table_row.append(cell.value)
    #
    #         # st_list = VmStatisticsList(
    #         #     connection=self._connection, id=vm_row.id). \
    #         #         statistic_objects_list()
    #             # connection = self._connection, id = vm.id().). \
    #             #     statistic_objects_list()
    #         #
    #         # st_list = vm.statistics()
    #
    #         # for i, statistic in enumerate(vm.statistics()):
    #         #     if statistic:
    #         #         if n == 0:
    #         #             header.append(statistic.name())
    #         #             # table.append(st_list[i].name())
    #         #         table_row.append(
    #         #             str(statistic.value()) +' '+ str(statistic.unit())
    #         #         )
    #
    #         for statistic in entity.statistics():
    #             if n == 0:
    #                 header.append(statistic.name)
    #             table_row.append(statistic.value)
    #
    #         # _disks = vm._disks()
    #
    #         # if self._flags[18]:
    #         # if n == 0:
    #         #     header.append('disk id')
    #             # table.append('disk id')
    #
    #         # bootable_disk = vm.bootable_disk()
    #
    #         # _disks = vm._disks()
    #         #
    #         # dk_st_names = ['data.current.read', 'data.current.write',
    #         #                'disk.read.latency', 'disk.write.latency',
    #         #                'disk.flush.latency']
    #         #
    #         # # if bootable_disk:
    #         # if _disks:
    #         #     # table_row.append(bootable_disk.id)
    #         #     table_row.append(_disks)
    #         #     # dk_list = DiskStatisticsList(
    #         #     #     connection=self._connection, dk_id=bootable_disk.id).\
    #         #     #     statistic_objects_list()
    #         #     dk_list = DiskStatisticsList(
    #         #         connection=self._connection, dk_id=_disks[0].id). \
    #         #         statistic_objects_list()
    #         #     for i,  in enumerate(dk_list):
    #         #         if :
    #         #             if n == 0:
    #         #                 header.append(dk_st_names[i])
    #         #                 # table.append(dk_list[i].name())
    #         #             table_row.append(
    #         #                 str(dk_list[i].()) +' '+ str(dk_list[i].unit())
    #         #             )
    #         # else:
    #         #     for i in range(6):
    #         #         if n == 0:
    #         #             header.append(dk_st_names[i])
    #         #         # table_row.append('')
    #         #         table_row.append(None)
    #
    #         # _nics = vm._nics()
    #         # nics_st_names = ['data.current.rx', 'data.current.tx',
    #         #                  'data.current.rx.bps', 'data.current.tx.bps',
    #         #                  'errors.total.rx', 'errors.total.tx',
    #         #                  'data.total.rx', 'data.total.tx']
    #         #
    #         # if _nics:
    #         #     if n == 0:
    #         #         header.append('nic id')
    #         #         # table.append('nic id')
    #         #     table_row.append(_nics[0].id)
    #         #
    #         #     nic_list = NICStatisticsList(
    #         #         connection=self._connection, nic_id=_nics[0].id,
    #         #         vm_id=vm.id()).statistic_objects_list()
    #         #
    #         #     for i,  in enumerate(nic_list):
    #         #         if :
    #         #             if n == 0:
    #         #                 header.append(nics_st_names[i])
    #         #                 # table.append(nic_list[i].name())
    #         #             table_row.append(
    #         #                 str(nic_list[i].()) +' '+ str(nic_list[i].unit())
    #         #             )
    #         # else:
    #         #     for i in range(8):
    #         #         if n == 0:
    #         #             header.append(nics_st_names[i])
    #         #         # table_row.append('')
    #         #         table_row.append(None)
    #
    #
    #         table.append(table_row)
    #
    #     self.data_list = table
    #     # self.current_data_list = self.data_list
    #     # self.current_headers_list = copy.deepcopy(self.data_list)
    #     self.headers_list = header
    #     # self.current_headers_list = self.headers_list
    #     # self.current_headers_list = copy.copy(self.headers_list)

    # def validate_filter(self, filter):
    #     str_col = [1, 2, 3, 4, 7, 8, 18, 24]
    #     float_col = [5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21,
    #                  22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
    #
    #     if filter.column in str_col and \
    #         filter.operand == '=' and isinstance(filter.value, str):
    #         # filter.operand is operator.eq and isinstance(filter.value, str):
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



