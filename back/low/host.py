from back.low.bases import base, statisctics_base
# from back.low.vm import Vm, VmList
from ovirtsdk4 import types
# import back.low.vm as Vm


class HostList(base.ListBase):

    def __init__(self, connection):
        super(HostList, self).__init__(connection=connection)
        self._service = connection.system_service().hosts_service()
        self._list = self._service.list()


class Host(base.SpecificBase):

    def __init__(self, connection, host_id):
        super(Host, self).__init__(connection=connection)
        self._service = connection.system_service().\
            hosts_service().host_service(id=host_id)
        self._info = self._service.get()

    def status(self):
        return self._info.status.name
        # status = self._info.status
        # if status is types.HostStatus.CONNECTING:
        #     return 'connecting'
        # if status is types.HostStatus.DOWN:
        #     return 'down'
        # if status is types.HostStatus.ERROR:
        #     return 'error'
        # if status is types.HostStatus.INITIALIZING:
        #     return 'initializing'
        # if status is types.HostStatus.INSTALLING:
        #     return 'installing'
        # if status is types.HostStatus.INSTALLING_OS:
        #     return 'initializing os'
        # if status is types.HostStatus.INSTALL_FAILED:
        #     return 'install failed'
        # if status is types.HostStatus.KDUMPING:
        #     return 'kdumping'
        # if status is types.HostStatus.MAINTENANCE:
        #     return 'maintenance'
        # if status is types.HostStatus.NON_OPERATIONAL:
        #     return 'non operational'
        # if status is types.HostStatus.NON_RESPONSIVE:
        #     return 'non responsive'
        # if status is types.HostStatus.PENDING_APPROVAL:
        #     return 'pending approval'
        # if status is types.HostStatus.PREPARING_FOR_MAINTENANCE:
        #     return 'preparing for maintenance'
        # if status is types.HostStatus.REBOOT:
        #     return 'reboot'
        # if status is types.HostStatus.UNASSIGNED:
        #     return 'unassigned'
        # if status is types.HostStatus.UP:
        #     return 'up'

    def address(self):
        return self._info.address

    def cluster(self):
        #todo vracia meno a nie objekt
        return self._connection.follow_link(self._info.cluster).name

    def nics(self):
        # nics = self._connection.follow_link(self._info.nics)
        # nics_list = []
        # for nic in nics:
        #     nic = self._connection.follow_link(nic)
        #     nics_list.append(nic)
        # if len(nics_list) > 0:
        #     return nics_list
        # else:
        #     return None
        nics = self._connection.follow_link(self._info.nics)
        # if nics:
        return [nic.name for nic in nics]
        # else:
        #     return None

    def vms(self):
        # from back.low.vm import Vm, VmList
        # vms = []
        # vm_list = VmList(connection=self._connection).list()
        # for vm in vm_list:
        #     vm_host = Vm(connection=self._connection, vm_id=vm.id).host()
        #     if vm_host and self._info.id == vm_host.id:
        #         vms.append(vm)
        # if len(vms) > 0:
        #     return vms
        # else:
        #     return None

        from back.low.vm import Vm, VmList
        vm_list = VmList(connection=self._connection).list()
        return [vm.name for vm in vm_list if self._info.name ==
                Vm(connection=self._connection, vm_id=vm.id).host()]


class HostStatisticsList(statisctics_base.StatisticsListBase):

    def __init__(self, connection, host_id):
        super(HostStatisticsList, self).__init__(
            connection=connection, id=host_id)
        self._service = self._service. \
            hosts_service().host_service(id=host_id).statistics_service()
        self._list = self._service.list()

    def statistic_objects_list(self):
        statistic_objects = []
        for i in range(17):
            statistic_objects.append(
                HostStatistic(connection=self._connection, host_id=self._id,
                              st_id=self._list[i].id)
            )
        return statistic_objects


class HostStatistic(statisctics_base.StatisticBase):

    def __init__(self, connection, host_id, st_id):
        super(HostStatistic, self).__init__(connection=connection)
        self._service = self._service.hosts_service().\
            host_service(id=host_id).statistics_service().\
            statistic_service(id=st_id)
        self._info = self._service.get()
