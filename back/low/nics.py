from back.low.base import base, statisctics_base


class NICsList(base.ListBase):

    def __init__(self, connection, vm_id):
        super(NICsList, self).__init__(connection=connection)
        self._service = self._service.vms_service().vm_service(id=vm_id). \
            nics_service()
        self._list = self._service.list()


class NIC(base.SpecificBase):

    def __init__(self, connection, nic_id, vm_id):
        super(NIC, self).__init__(connection=connection)
        self._service = self._service.vms_service().vm_service(id=vm_id).\
            nics_service().nic_service(id=nic_id)
        self._info = self._service.get()


class NICStatisticsList(statisctics_base.StatisticsListBase):

    def __init__(self, connection, nic_id, vm_id):
        super(NICStatisticsList, self).__init__(
            connection=connection, id=nic_id)
        self._service = self._service.vms_service().vm_service(id=vm_id).\
            nics_service().nic_service(id=nic_id).statistics_service()
        self._list = self._service.list()
        self._vm_id = vm_id

    def statistic_objects_list(self, flags):
        statistic_objects = []
        for i, flag_val in enumerate(flags):
            if flag_val:
                statistic_objects.append(
                    NICStatistic(connection=self._connection, nic_id=self._id,
                                st_id=self._list[i].id, vm_id=self._vm_id)
                )
        return statistic_objects


class NICStatistic(statisctics_base.StatisticBase):

    def __init__(self, connection, nic_id, st_id, vm_id):
        super(NICStatistic, self).__init__(connection=connection)
        self._service = self._service.vms_service().vm_service(id=vm_id).\
            nics_service().nic_service(id=nic_id).statistics_service().\
            statistic_service(id=st_id)
        self._info = self._service.get()
