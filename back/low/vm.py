from back.low.cluster import Cluster
from back.low.bases import base, statisctics_base
from ovirtsdk4 import types


class VmList(base.ListBase):

    def __init__(self, connection):
        super(VmList, self).__init__(connection=connection)
        self._service = self._service.vms_service()
        self._list = self._service.list()


class Vm(base.SpecificBase):

    def __init__(self, connection, vm_id):
        super(Vm, self).__init__(connection=connection)
        self._service = self._service.vms_service().vm_service(id=vm_id)
        self._info = self._service.get()

    def cl_version(self):
        cl = self._connection.follow_link(self._info.cluster)
        return Cluster(connection=self._connection, cl_id=cl.id).version()

    def bootable_disk(self):
        disk_attachments = self._connection. \
            follow_link(self._info.disk_attachments)
        for attachment in disk_attachments:
            if attachment.bootable:
                return attachment
        return None
        # return ''

    def disks(self):
        disk_attachments = self._connection.\
            follow_link(self._info.disk_attachments)
        disks_list = []
        for attachment in disk_attachments:
            disk = self._connection.follow_link(attachment.disk)
            disks_list.append(disk)
        return disks_list

    def host(self):
        if self._info.host:
            return self._connection.follow_link(self._info.host)
            # return ''
        else:
            # return self._connection.follow_link(self._info.host).name
            return None

    def memory(self):
        # return str(self._info.memory)
        return self._info.memory

    def memory_max(self):
        # return str(self._info.memory_policy.max)
        return self._info.memory_policy.max

    def nics(self):
        nics = self._connection.follow_link(self._info.nics)
        nics_list = []
        for nic in nics:
            nic = self._connection.follow_link(nic)
            nics_list.append(nic)
        if len(nics_list) > 0:
            return nics_list
        else:
            return None
            # return ''

    def os(self):
        return self._info.os.type

    def template(self):
        #todo vracia meno a nie objekt
        template = self._connection.follow_link(self._info.template).name
        if template == 'Blank':
            return None
            # return ''
        else:
            return template

    def st_memory_installed(self):
        return self._connection.follow_link(self._info.statistics)

    def status(self):
        status = self._info.status
        if status is types.VmStatus.DOWN:
            return 'down'
        if status is types.VmStatus.IMAGE_LOCKED:
            return 'image locked'
        if status is types.VmStatus.MIGRATING:
            return 'migrating'
        if status is types.VmStatus.NOT_RESPONDING:
            return 'not responding'
        if status is types.VmStatus.PAUSED:
            return 'paused'
        if status is types.VmStatus.POWERING_DOWN:
            return 'powering down'
        if status is types.VmStatus.REBOOT_IN_PROGRESS:
            return 'reboot in progress'
        if status is types.VmStatus.RESTORING_STATE:
            return 'restoring state'
        if status is types.VmStatus.SAVING_STATE:
            return 'saving state'
        if status is types.VmStatus.SUSPENDED:
            return 'suspended'
        if status is types.VmStatus.UNASSIGNED:
            return 'unassigned'
        if status is types.VmStatus.UNKNOWN:
            return 'unknown'
        if status is types.VmStatus.UP:
            return 'up'
        if status is types.VmStatus.WAIT_FOR_LAUNCH:
            return 'wait for launch'

    def storage_domain(self):
        pass

    def cluster(self):
        #todo vracia meno a nie objekt
        return self._info.cluster.name


class VmStatisticsList(statisctics_base.StatisticsListBase):

    def __init__(self, connection, vm_id):
        super(VmStatisticsList, self).__init__(connection=connection, id=vm_id)
        self._service = self._service. \
            vms_service().vm_service(id=vm_id).statistics_service()
        self._list = self._service.list()

    # def statistic_objects_list(self, flags):
    def statistic_objects_list(self):
        statistic_objects = []
        # for i, flag_val in enumerate(flags):
        #     if flag_val:
        for i in range(9):
            statistic_objects.append(
                VmStatistic(connection=self._connection, vm_id=self._id,
                            st_id=self._list[i].id)
            )
        return statistic_objects


class VmStatistic(statisctics_base.StatisticBase):

    def __init__(self, connection, vm_id, st_id):
        super(VmStatistic, self).__init__(connection=connection)
        self._service = self._service.vms_service().vm_service(id=vm_id).\
            statistics_service().statistic_service(id=st_id)
        self._info = self._service.get()
