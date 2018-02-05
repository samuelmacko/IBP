from back.low.vm import VmList, VmStatisticsList
from back.low.vm import Vm as vm_low
from back.low.disks import DiskStatisticsList
from back.low.nics import NICStatisticsList
from collections import OrderedDict


class Vm(object):

    def __init__(self, connection, flags):
        self._connection = connection
        self._flags = flags

    def construct_table(self):
        table = []
        header = ['name']

        vms_list = VmList(connection=self._connection).list()

        for n, vm_row in enumerate(vms_list):
            table_row = []

            vm = vm_low(connection=self._connection, vm_id=vm_row.id)

            table_row.append(vm.name())

            # method_dict = {
            #     'id': vm.id, 'cl version': vm.cl_version, 'hosts': vm.host,
            #     'memory': vm.memory, 'max memory': vm.memory_max,
            #     'os': vm.os, 'template': vm.template
            # }
            method_dict = OrderedDict([
                ('id', vm.id), ('cl version', vm.cl_version), ('hosts', vm.host),
                ('memory', vm.memory), ('max memory', vm.memory_max),
                ('os', vm.os), ('template', vm.template)
            ])
            for i, method in enumerate(method_dict.items()):
                if self._flags[i]:
                    if n == 0:
                        header.append(method[0])
                    table_row.append(method[1]())


            #todo toto cele robit iba ked je zaskrtnuty nejaky flag 9-18
            st_flags = []
            for i in range(9, 18):
                st_flags.append(self._flags[i])
            st_list = VmStatisticsList(
                connection=self._connection, vm_id=vm_row.id). \
                statistic_objects_list(flags=st_flags)

            for i, value in enumerate(st_list):
                if value:
                    if n == 0:
                        header.append(st_list[i].name())
                    table_row.append(
                        str(st_list[i].value()) +' '+ str(st_list[i].unit())
                    )


            #todo zatial uvazujem iba jeden disk, poriesit ako s viacerymi
            disks = vm.disks()

            if self._flags[18]:
                if n == 0:
                    header.append('disk id')
                table_row.append(disks[0].id)

            #todo to iste aj pre disky, iba ked je nieco zaskrtnute

            dk_flags = []
            for i in range(19, 24):
                dk_flags.append(self._flags[i])
            dk_list = DiskStatisticsList(
                connection=self._connection, dk_id=disks[0].id).\
                statistic_objects_list(flags=dk_flags)

            for i, value in enumerate(dk_list):
                if value:
                    if n == 0:
                        header.append(dk_list[i].name())
                    table_row.append(
                        str(dk_list[i].value()) +' '+ str(dk_list[i].unit())
                    )


            #todo to iste pre nics
            nics = vm.nics()

            if self._flags[18]:
                if n == 0:
                    header.append('nic id')
                table_row.append(nics[0].id)

            nic_flags = []
            for i in range(23, 31):#31
                nic_flags.append(self._flags[i])
            nic_list = NICStatisticsList(
                connection=self._connection, nic_id=nics[0].id,
                vm_id=vm.id()).statistic_objects_list(flags=nic_flags)

            for i, value in enumerate(nic_list):
                if value:
                    if n == 0:
                        header.append(nic_list[i].name())
                    table_row.append(
                        str(nic_list[i].value()) +' '+ str(nic_list[i].unit())
                    )


            table.append(table_row)



        return header, table
