from back.low.cluster import Cluster
from back.low.base import base, statisctics_base


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
        return Cluster(connection=self._connection, id=cl.id).version()

    def disks(self):
        disk_attachments = self._connection.\
            follow_link(self._info.disk_attachments)
        disks_list = []
        for attachment in disk_attachments:
            disk = self._connection.follow_link(attachment.disk)
            disks_list.append(disk)
        return disks_list

    def host(self):
        if self._info.host == None:
            return None
        else:
            return self._connection.follow_link(self._info.host).name

    def memory(self):
        return self._info.memory

    def memory_max(self):
        return self._info.memory_policy.max

    def nics(self):
        nics = self._connection.follow_link(self._info.nics)
        nics_list = []
        for nic in nics:
            nic = self._connection.follow_link(nic)
            nics_list.append(nic)
        return nics_list

    def os(self):
        return self._info.os.type

    def template(self):
        template = self._connection.follow_link(self._info.template).name
        if template == 'Blank':
            return None
        else:
            return template

    def st_memory_installed(self):
        return self._connection.follow_link(self._info.statistics)


class VmStatisticsList(statisctics_base.StatisticsListBase):

    def __init__(self, connection, vm_id):
        super(VmStatisticsList, self).__init__(connection=connection, id=vm_id)
        self._service = self._service. \
            vms_service().vm_service(id=vm_id).statistics_service()
        self._list = self._service.list()

    def statistic_objects_list(self, flags):
        statistic_objects = []
        for i, flag_val in enumerate(flags):
            if flag_val:
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
