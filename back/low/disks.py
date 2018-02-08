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
        if status is types.DiskStatus.ILLEGAL:
            return 'illegal'
        if status is types.DiskStatus.LOCKED:
            return 'locked'
        if status is types.DiskStatus.OK:
            return 'ok'

    def actual_size(self):
        # return str(self._info.actual_size)
        return self._info.actual_size

    def provisioned_size(self):
        # return str(self._info.provisioned_size)
        return self._info.provisioned_size

    def format(self):
        format = self._info.format
        if format is types.DiskFormat.RAW:
            return 'raw'
        if format is types.DiskFormat.COW:
            return 'cow'

    def content_type(self):
        content_type = self._info.content_type
        if content_type is types.DiskContentType.DATA:
            return 'data'
        if content_type is types.DiskContentType.ISO:
            return 'iso'
        if content_type is types.DiskContentType.MEMORY_DUMP_VOLUME:
            return 'memory dump volume'
        if content_type is types.DiskContentType.MEMORY_METADATA_VOLUME:
            return 'memory metadata volume'
        if content_type is types.DiskContentType.OVF_STORE:
            return 'ovf store'

    def storage_type(self):
        storage_type = self._info.storage_type
        if storage_type is types.DiskStorageType.CINDER:
            return 'cinder'
        if storage_type is types.DiskStorageType.IMAGE:
            return 'image'
        if storage_type is types.DiskStorageType.LUN:
            return 'lun'

    def vms(self):
        vms = []
        vm_list = VmList(connection=self._connection).list()
        for vm in vm_list:
            vm_disks = Vm(connection=self._connection, vm_id=vm.id).disks()
            for vm_disk in vm_disks:
                if self._info.id == vm_disk.id:
                    # vms.append(vm.name)
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