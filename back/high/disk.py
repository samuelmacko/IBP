from back.low.vm import Vm
from back.low.disks import DisksList
from back.low.disks import Disk as disk_low
from back.low.disks import DiskStatisticsList
from back.low.vm import VmStatisticsList
from collections import OrderedDict
from back.high.bases.base import HighBase
import operator


class Disk(HighBase):
    def __init__(self, connection):
        super(Disk, self).__init__(connection=connection)
        self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def construct_table(self):
        table = []
        header = ['name']

        disks_list = DisksList(connection=self._connection).list()

        for n, disk_row in enumerate(disks_list):

            disk = disk_low(connection=self._connection, dk_id=disk_row.id)
            self.row_flags.append(1)
            table_row = []

            table_row.append(disk.name())



            vms = disk.vms()
            if n == 0:
                header.append('vms')
            if vms:
                table_row.append(vms[0])
            else:
                table_row.append('')


            vm_st_names = ['memory.installed', 'memory.used',
                           'cpu.current.guest', 'cpu.current.hypervisor',
                           'cpu.current.total', 'migration.progress',
                           'memory.buffered', 'memory.cached',
                           'memory.free']
            if vms:
                vm_st_list = VmStatisticsList(
                    connection=self._connection, vm_id=vms[0]).\
                    statistic_objects_list()
                for i, value in enumerate(vm_st_list):
                    if value:
                        if n == 0:
                            header.append(vm_st_list[i].name())
                        table_row.append(
                            str(vm_st_list[i].value()) + ' '
                            + str(vm_st_list[i].unit())
                        )
            else:
                for i in range(len(vm_st_names)):
                    if n == 0:
                        header.append(vm_st_names[i])
                    table_row.append('')




            method_dict = OrderedDict([
                ('status', disk.status), ('id', disk.id),
                ('actual size', disk.actual_size),
                ('provisioned size', disk.provisioned_size),
                ('format', disk.format), ('content type', disk.content_type),
                ('storage type', disk.storage_type)
            ])
            for i, method in enumerate(method_dict.items()):
                if n == 0:
                    header.append(method[0])
                table_row.append(method[1]())

            dk_st_list = DiskStatisticsList(
                connection=self._connection, dk_id=disk.id()).\
                statistic_objects_list()
            for i, value in enumerate(dk_st_list):
                if value:
                    if n == 0:
                        header.append(dk_st_list[i].name())
                    table_row.append(
                        str(dk_st_list[i].value()) + ' '
                            + str(dk_st_list[i].unit())
                    )

            table.append(table_row)



        self.data_list = table
        self.current_data_list = self.data_list
        self.headers_list = header
