from back.low.bases import base, statisctics_base
from ovirtsdk4 import types
from back.low.vm import Vm, VmList
from back.suplementary.cell_item import CellItem


class DisksList(base.ListBase):

    def __init__(self, connection):
        super(DisksList, self).__init__(connection=connection)
        self._service = self._service.disks_service()
        self._list = self._service.list()

    # def disks_list(self):
    #     return self._list


class Disk(base.SpecificBase):

    def __init__(self, connection, id):
        super(Disk, self).__init__(connection=connection, id=id)
        self._service = self._service.disks_service().disk_service(id=id)
        self._info = self._service.get()

    def _status(self):
        name = 'Status'
        return CellItem(name=name, value=self._info._status.name)

    def _actual_size(self):
        name = 'Actual size'
        return CellItem(name=name, value=str(self._info._actual_size))
        # return self._info._actual_size

    def _provisioned_size(self):
        name = 'Provisioned size'
        return CellItem(name=name, value=str(self._info._provisioned_size))
        # return self._info._provisioned_size

    def _format(self):
        name = 'Format'
        return CellItem(name=name, value=self._info._format.name)

    def _content_type(self):
        name = 'Content type'
        return CellItem(name=name, value=self._info._content_type.name)

    def _storage_type(self):
        name = 'Storage type'
        return CellItem(name=name, value=self._info._storage_type.name)

    def _vms(self):
        name = 'VMs'
        vms = []
        vm_list = VmList(connection=self._connection).list()
        for vm in vm_list:
            vm_disks = Vm(connection=self._connection, id=vm.id).disks_obj()
            for vm_disk in vm_disks:
                # if self._info.id == vm_disk.id:
                if vm_disk and self._info.id == vm_disk.id:
                    vms.append(vm.name)
        return CellItem(name=name, value=vms)

    # def statistics(self):
    #     service = self._service.statistics_service()
    #     statistics_list = service.list()
    #
    #     statistic_objects = []
    #     for i in range(5):
    #         statistic_objects.append(
    #             DiskStatistic(
    #                 connection=self._connection, obj_id=self.id().value,
    #                 st_id=statistics_list[i].id)
    #         )
    #
    #     statistics = []
    #     for statistic in statistic_objects:
    #         statistics.append(
    #             CellItem(
    #                 name=statistic.name(),
    #                 value=str(statistic.value()) +' '+str(statistic.unit()))
    #         )
    #     return statistics

    def methods_list(self):
        return [self.name, self.id, self._status,
                self._actual_size, self._provisioned_size,
                self._format, self._content_type, self._vms,
                self._storage_type]
