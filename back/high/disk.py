from back.low.vm import Vm
from back.low.disks import DisksList
from back.low.disks import Disk as disk_low
from back.low.disks import DiskStatisticsList
from back.low.vm import VmStatisticsList
from collections import OrderedDict
from back.high.bases.base import HighBase
import operator


class Disk(HighBase):

    def __init__(self, connection, col_flags=None):
        super(Disk, self).__init__(connection=connection)
        if col_flags:
            self.col_flags = col_flags
        else:
            self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                              1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def construct_table(self):
        table = []
        header = []

        disks_list = DisksList(connection=self._connection).list()

        for n, disk_row in enumerate(disks_list):

            disk = disk_low(connection=self._connection, dk_id=disk_row.id)
            # self.row_flags.append(1)
            # table_row = []

            vms = disk.vms()
            if vms:
                for vm in vms:
                    if n == 0:
                        header, row = self.create_row(
                            vm=vm, disk=disk, first_row=True)

                    else:
                        row = self.create_row(
                            vm=vm, disk=disk, first_row=False)
                    # table_row = row
                    table.append(row)
            else:
                if n == 0:
                    header, row = self.create_row(
                        vm=None, disk=disk, first_row=True)

                else:
                    row = self.create_row(
                        vm=None, disk=disk, first_row=False)
                # table_row = row
                table.append(row)
            # table.append(table_row)


        self.data_list = table
        # self.current_data_list = self.data_list
        self.headers_list = header

    def create_row(self, vm, disk, first_row):

        self.row_flags.append(1)

        table_row = []
        header = ['name']

        table_row.append(disk.name())

        vm_st_names = ['vm', 'memory.installed', 'memory.used',
                       'cpu.current.guest', 'cpu.current.hypervisor',
                       'cpu.current.total', 'migration.progress',
                       'memory.buffered', 'memory.cached',
                       'memory.free']

        if vm:
            if first_row:
                header.append('vm')
            table_row.append(vm.name)

            vm_st_list = VmStatisticsList(
                connection=self._connection, vm_id=vm.id). \
                statistic_objects_list()
            for i, value in enumerate(vm_st_list):
                if value:
                    if first_row:
                        header.append(vm_st_list[i].name())
                    table_row.append(
                        str(vm_st_list[i].value()) + ' '
                        + str(vm_st_list[i].unit())
                    )
        else:
            for i in range(len(vm_st_names)):
                if first_row:
                    # if i == 0:
                    #     header.append('vm')
                    header.append(vm_st_names[i])
                # table_row.append('')
                table_row.append(None)


        method_dict = OrderedDict([
            ('status', disk.status), ('id', disk.id),
            ('actual size', disk.actual_size),
            ('provisioned size', disk.provisioned_size),
            ('format', disk.format), ('content type', disk.content_type),
            ('storage type', disk.storage_type)
        ])
        for i, method in enumerate(method_dict.items()):
            if first_row:
                header.append(method[0])
            table_row.append(method[1]())

        dk_st_list = DiskStatisticsList(
            connection=self._connection, dk_id=disk.id()). \
            statistic_objects_list()
        for i, value in enumerate(dk_st_list):
            if value:
                if first_row:
                    header.append(dk_st_list[i].name())
                table_row.append(
                    str(dk_st_list[i].value()) + ' '
                    + str(dk_st_list[i].unit())
                )

        if first_row:
            # print(table_row)
            return header, table_row
        else:
            # print(table_row)
            return table_row

    def validate_filter(self, filter):
        # print('col', filter.column)
        # print('op', filter.operand)
        # print('val', filter.value)
        str_col = [0, 1, 2, 11, 12, 15, 16, 17]
        float_col = [3, 4, 5, 6, 7, 8, 9, 10, 13, 14, 18, 19, 20,
                     21, 22]

        if filter.column in str_col and \
            filter.operand == '=' and isinstance(filter.value, str):
            return True

        if filter.column in float_col:
            try:
                float(filter.value)
                return True
            except ValueError:
                return False

        return False