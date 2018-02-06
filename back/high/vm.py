from back.low.vm import VmList, VmStatisticsList
from back.low.vm import Vm as vm_low
from back.low.disks import DiskStatisticsList
from back.low.nics import NICStatisticsList
from back.high.bases.base import HighBase
from collections import OrderedDict
import operator


class Vm(HighBase):

    # def __init__(self, connection, flags):
    def __init__(self, connection):
        super(Vm, self).__init__(connection=connection)
        # self._connection = connection
        self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                          1, 1, 1]
        # self.row_flags = []
        # self.data_list = None
        # self.headers_list = None
        # self.current_data_list = self.data_list
        # self.construct_table()

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
                ('id', vm.id), ('clVersion', vm.cl_version), ('hosts', vm.host),
                ('memory', vm.memory), ('maxMemory', vm.memory_max),
                ('os', vm.os), ('template', vm.template)
            ])
            for i, method in enumerate(method_dict.items()):
                # if self._flags[i]:
                if n == 0:
                    header.append(method[0])
                    # table.append(method[0])
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
            if n == 0:
                header.append('disk id')
                # table.append('disk id')

            bootable_disk = vm.bootable_disk()
            dk_st_names = ['data.current.read', 'data.current.write',
                           'disk.read.latency', 'disk.write.latency',
                           'disk.flush.latency']

            if bootable_disk:
                table_row.append(bootable_disk.id)
                dk_list = DiskStatisticsList(
                    connection=self._connection, dk_id=bootable_disk.id).\
                    statistic_objects_list()
                for i, value in enumerate(dk_list):
                    if value:
                        if n == 0:
                            header.append(dk_st_names[i])
                            # table.append(dk_list[i].name())
                        table_row.append(
                            str(dk_list[i].value()) +' '+ str(dk_list[i].unit())
                        )
            else:
                for i in range(6):
                    if n == 0:
                        header.append(dk_st_names[i])
                    table_row.append('')


            nics = vm.nics()
            nics_st_names = ['data.current.rx', 'data.current.tx',
                             'data.current.rx.bps', 'data.current.tx.bps',
                             'errors.total.rx', 'errors.total.tx',
                             'data.total.rx', 'data.total.tx']

            if nics:
                if n == 0:
                    header.append('nic id')
                    # table.append('nic id')
                table_row.append(nics[0].id)

                nic_list = NICStatisticsList(
                    connection=self._connection, nic_id=nics[0].id,
                    vm_id=vm.id()).statistic_objects_list()

                for i, value in enumerate(nic_list):
                    if value:
                        if n == 0:
                            header.append(nics_st_names[i])
                            # table.append(nic_list[i].name())
                        table_row.append(
                            str(nic_list[i].value()) +' '+ str(nic_list[i].unit())
                        )
            else:
                for i in range(8):
                    if n == 0:
                        header.append(nics_st_names[i])
                    table_row.append('')


            table.append(table_row)

        self.data_list = table
        self.current_data_list = self.data_list
        self.headers_list = header

    def validate_filter(self, filter):
        str_col = [0,1,2,3,6,7,17,23]
        float_col = [4,5,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24
                    ,25,26,27,28,29,30,31]

        if filter.column in str_col and \
            filter.operand is operator.eq and isinstance(filter.value, str):
            return True

        if filter.column in float_col:
            try:
                float(filter.value)
                return True
            except ValueError:
                return False

        return False



