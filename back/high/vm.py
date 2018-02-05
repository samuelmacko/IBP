from back.low.vm import VmList, VmStatisticsList
from back.low.vm import Vm as vm_low
from back.low.disks import DiskStatisticsList
from back.low.nics import NICStatisticsList
from collections import OrderedDict
# import copy
import re
import operator


class Vm(object):

    # def __init__(self, connection, flags):
    def __init__(self, connection):
        self._connection = connection
        # self.flags = flags
        self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.row_flags = []
        self.data_list = None
        self.headers_list = None
        self.current_data_list = self.data_list

    def construct_table(self):
        table = []
        header = ['name']
        # table = ['name']

        vms_list = VmList(connection=self._connection).list()

        for n, vm_row in enumerate(vms_list):
            self.row_flags.append(1)
            table_row = []

            vm = vm_low(connection=self._connection, vm_id=vm_row.id)

            table_row.append(vm.name())

            method_dict = OrderedDict([
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


            #todo toto cele robit iba ked je zaskrtnuty nejaky flag 9-18
            # st_flags = []
            # for i in range(9, 18):
            #     st_flags.append(self._flags[i])
            # st_list = VmStatisticsList(
            #     connection=self._connection, vm_id=vm_row.id). \
            #     statistic_objects_list(flags=st_flags)
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


            #todo zatial uvazujem iba jeden disk, poriesit ako s viacerymi
            disks = vm.disks()

            # if self._flags[18]:
            if n == 0:
                header.append('disk id')
                # table.append('disk id')
            table_row.append(disks[0].id)

            #todo to iste aj pre disky, iba ked je nieco zaskrtnute

            # dk_flags = []
            # for i in range(19, 24):
            #     dk_flags.append(self._flags[i])
            dk_list = DiskStatisticsList(
                connection=self._connection, dk_id=disks[0].id).\
                statistic_objects_list()

            for i, value in enumerate(dk_list):
                if value:
                    if n == 0:
                        header.append(dk_list[i].name())
                        # table.append(dk_list[i].name())
                    table_row.append(
                        str(dk_list[i].value()) +' '+ str(dk_list[i].unit())
                    )


            #todo to iste pre nics
            nics = vm.nics()

            # if self._flags[18]:
            if n == 0:
                header.append('nic id')
                # table.append('nic id')
            table_row.append(nics[0].id)

            # nic_flags = []
            # for i in range(23, 31):#31
            #     nic_flags.append(self._flags[i])
            nic_list = NICStatisticsList(
                connection=self._connection, nic_id=nics[0].id,
                vm_id=vm.id()).statistic_objects_list()

            for i, value in enumerate(nic_list):
                if value:
                    if n == 0:
                        header.append(nic_list[i].name())
                        # table.append(nic_list[i].name())
                    table_row.append(
                        str(nic_list[i].value()) +' '+ str(nic_list[i].unit())
                    )


            table.append(table_row)

        self.data_list = table
        self.current_data_list = self.data_list
        self.headers_list = header

    def table_from_flags(self):
        headers = []
        data = []

        for i, flag in enumerate(self.col_flags):
            if flag == 1:
                headers.append(self.headers_list[i])

        for j, row in enumerate(self.data_list):
            data_row = []
            for i, flag in enumerate(self.col_flags):
                if flag == 1:
                    data_row.append(row[i])
            if self.row_flags[j]:
                data.append(data_row)

        return headers, data

    def process_filter(self, text):

        class Filter(object):

            def __init__(self, column, operand, value):
                self.column = column
                self.operand = operand
                self.value = value

        ops = {
            '>': operator.gt, '<': operator.lt, '=': operator.eq}

        filter_regex = r'*(\s*)|(\s*(\S+)\s*(>|<|=)\s*(\S+)\s)*'
        match = re.match(filter_regex, text, re.I)
        attribute = match.group(1)
        operand = ops[match.group(2)]
        value = match.group(3)

        if match:
            attribute_column = None
            for i, header in enumerate(self.headers_list):
                # print(header)
                if attribute == header:
                    attribute_column = i
                    break

            if attribute_column is not None:
                filter = Filter(
                    column=attribute_column, operand=operand, value=value)
                return filter
            else:
                return None
        else:
            return None

    def apply_filter(self, filter):
        for i, row in enumerate(self.current_data_list):
            if filter.operand(row[filter.column], filter.value) is False:
                # print('naslo', row[0])
                # del self.current_data_list[i]
                self.row_flags[i] = 0
