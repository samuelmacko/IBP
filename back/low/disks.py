from back.low.base import base, statisctics_base


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

    def id(self):
        return self._info.id

    def name(self):
        return self._info.name

    def status(self):
        return self._info.status


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