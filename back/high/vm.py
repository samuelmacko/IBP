from back.low.vm import VmList, VmStatisticsList
from back.low.vm import Vm as vm_low
from back.low.disks import DiskStatisticsList
from back.low.nics import NICStatisticsList
from back.high.bases.base import HighBase
from collections import OrderedDict
import operator
import copy


class Vm(HighBase):

    def __init__(self, connection, col_flags):
    # def __init__(self, connection, col_flags=None):
        super(Vm, self).__init__(connection=connection)
        # if col_flags:
        self.col_flags = col_flags
        # else:
        #     self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        #                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        #                       1, 1, 1]

    def construct_table(self):
        table = []
        header = ['name']

        vms_list = VmList(connection=self._connection).list()

        for n, vm_row in enumerate(vms_list):
            self.row_flags.append(1)
            table_row = []

            vm = vm_low(connection=self._connection, vm_id=vm_row.id)

            table_row.append(vm.name())

            method_dict = OrderedDict([
                ('status', vm.status),
                ('id', vm.id), ('clVersion', vm.cl_version), ('host', vm.host),
                ('memory', vm.memory), ('maxMemory', vm.memory_max),
                ('os', vm.os), ('template', vm.template), ('disks', vm.disks),
                ('NICs', vm.nics)
            ])
            for method in method_dict.items():
                # if self._flags[i]:
                if n == 0:
                    header.append(method[0])
                    # table.append(method[0])
                # if method[0] == 'host':
                #     if method[1]():
                #         table_row.append(method[1]().name)
                #     else:
                #         table_row.append('')
                #     continue
                table_row.append(method[1]())

            st_list = VmStatisticsList(
                connection=self._connection, vm_id=vm_row.id). \
                statistic_objects_list()

            for i, value in enumerate(st_list):
                if value:
                    if n == 0:
                        header.append(st_list[i].name())
                        # table.append(st_list[i].name())
                    table_row.append(
                        str(st_list[i].value()) +' '+ str(st_list[i].unit())
                    )

            # disks = vm.disks()

            # if self._flags[18]:
            # if n == 0:
            #     header.append('disk id')
                # table.append('disk id')

            # bootable_disk = vm.bootable_disk()

            # disks = vm.disks()
            #
            # dk_st_names = ['data.current.read', 'data.current.write',
            #                'disk.read.latency', 'disk.write.latency',
            #                'disk.flush.latency']
            #
            # # if bootable_disk:
            # if disks:
            #     # table_row.append(bootable_disk.id)
            #     table_row.append(disks)
            #     # dk_list = DiskStatisticsList(
            #     #     connection=self._connection, dk_id=bootable_disk.id).\
            #     #     statistic_objects_list()
            #     dk_list = DiskStatisticsList(
            #         connection=self._connection, dk_id=disks[0].id). \
            #         statistic_objects_list()
            #     for i, value in enumerate(dk_list):
            #         if value:
            #             if n == 0:
            #                 header.append(dk_st_names[i])
            #                 # table.append(dk_list[i].name())
            #             table_row.append(
            #                 str(dk_list[i].value()) +' '+ str(dk_list[i].unit())
            #             )
            # else:
            #     for i in range(6):
            #         if n == 0:
            #             header.append(dk_st_names[i])
            #         # table_row.append('')
            #         table_row.append(None)

            # nics = vm.nics()
            # nics_st_names = ['data.current.rx', 'data.current.tx',
            #                  'data.current.rx.bps', 'data.current.tx.bps',
            #                  'errors.total.rx', 'errors.total.tx',
            #                  'data.total.rx', 'data.total.tx']
            #
            # if nics:
            #     if n == 0:
            #         header.append('nic id')
            #         # table.append('nic id')
            #     table_row.append(nics[0].id)
            #
            #     nic_list = NICStatisticsList(
            #         connection=self._connection, nic_id=nics[0].id,
            #         vm_id=vm.id()).statistic_objects_list()
            #
            #     for i, value in enumerate(nic_list):
            #         if value:
            #             if n == 0:
            #                 header.append(nics_st_names[i])
            #                 # table.append(nic_list[i].name())
            #             table_row.append(
            #                 str(nic_list[i].value()) +' '+ str(nic_list[i].unit())
            #             )
            # else:
            #     for i in range(8):
            #         if n == 0:
            #             header.append(nics_st_names[i])
            #         # table_row.append('')
            #         table_row.append(None)


            table.append(table_row)

        self.data_list = table
        # self.current_data_list = self.data_list
        # self.current_headers_list = copy.deepcopy(self.data_list)
        self.headers_list = header
        # self.current_headers_list = self.headers_list
        # self.current_headers_list = copy.copy(self.headers_list)

    def validate_filter(self, filter):
        str_col = [1, 2, 3, 4, 7, 8, 18, 24]
        float_col = [5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21,
                     22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

        if filter.column in str_col and \
            filter.operand == '=' and isinstance(filter.value, str):
            # filter.operand is operator.eq and isinstance(filter.value, str):
            return True

        if filter.column in float_col:
            try:
                float(filter.value)
                return True
            except ValueError:
                return False

        return False



