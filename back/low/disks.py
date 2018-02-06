from back.low.bases import base, statisctics_base
from ovirtsdk4 import types
from back.low.vm import Vm, VmList


class DisksList(base.ListBase):

    def __init__(self, connection):
        super(DisksList, self).__init__(connection=connection)
        self._service = self._service.disks_service()
        self._list = self._service.list()

    # def disks_list(self):
    #     return self._list


class Disk(base.SpecificBase):

    def __init__(self, connection, dk_id):
        super(Disk, self).__init__(connection=connection)
        self._service = self._service.disks_service().disk_service(id=dk_id)
        self._info = self._service.get()

    # def id(self):
    #     return self._info.id
    #
    # def name(self):
    #     return self._info.name

    def status(self):
        status = self._info.status
        if status == types.DiskStatus.ILLEGAL:
            return 'illegal'
        if status == types.DiskStatus.LOCKED:
            return 'locked'
        if status == types.DiskStatus.OK:
            return 'ok'

    def size(self):
        return self._info.size

    def format(self):
        return self._info.format

    def type(self):
        return self._info.type

    def storage_type(self):
        return self._info.storage_type

    def vms(self):
        vms = []
        vm_list = VmList(connection=self._connection).list()
        for vm in vm_list:
            vm_disks = Vm(connection=self._connection, vm_id=vm.id).disks()
            if self.name() in vm_disks:
                vms.append(vm)
        return vms







class DiskStatisticsList(statisctics_base.StatisticsListBase):

    def __init__(self, connection, dk_id):
        super(DiskStatisticsList, self).__init__(
            connection=connection, id=dk_id)
        self._service = self._service.disks_service().\
            disk_service(id=dk_id).statistics_service()
        self._list = self._service.list()

    # def statistic_objects_list(self, flags):
    def statistic_objects_list(self):
        statistic_objects = []
        for i in range(5):
        # for i, flag_val in enumerate(flags):
        #     if flag_val:
            statistic_objects.append(
                DiskStatistic(connection=self._connection, dk_id=self._id,
                            st_id=self._list[i].id)
            )
        return statistic_objects


class DiskStatistic(statisctics_base.StatisticBase):

    def __init__(self, connection, dk_id, st_id):
        super(DiskStatistic, self).__init__(connection=connection)
        self._service = self._service.disks_service().disk_service(id=dk_id).\
            statistics_service().statistic_service(id=st_id)
        self._info = self._service.get()