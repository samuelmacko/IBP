from back.suplementary.cell_item import CellItem
from ovirtsdk4 import types


class EntityBase(object):

    def __init__(self, connection):
        self._connection = connection
        self._service = connection.system_service()
        self._info = None


class ListBase(EntityBase):

    def __init__(self, connection):
        super(ListBase, self).__init__(connection=connection)
        self._list = None

    def list(self):
        return self._list


class SpecificBase(EntityBase):

    def __init__(self, connection, id):
        super(SpecificBase, self).__init__(connection=connection)
        self._id = id
        self._info = None

    def id(self):
        name = 'ID'
        return CellItem(name=name, value=self._info.id)

    def name(self):
        name = 'Name'
        return CellItem(name=name, value=self._info.name)

    def methods_list(self):
        raise NotImplementedError

    def statistics(self):
        service = self._service.statistics_service()
        statistics_list = service.list()

        statistic_objects = []
        for statistic in statistics_list:
            statistic_objects.append(
                Statistic(
                    connection=self._connection, obj_id=self.id().value,
                    st_id=statistic.id, service=service
                )
            )

        statistics = []
        for statistic in statistic_objects:
            statistics.append(
                CellItem(
                    name=statistic.name(),
                    value=str(statistic.value()) +' '+str(statistic.unit())
                )
            )
        return statistics


class Statistic(EntityBase):

    def __init__(self, connection, obj_id, st_id, service):
        super(Statistic, self).__init__(connection=connection)
        self._service = service.statistic_service(id=st_id)
        self._info = self._service.get()

    def name(self):
        return self._info.name

    def type(self):
        return self._info.type

    def unit(self):
        # return self._info.unit.name
        unit = self._info.unit
        if unit == types.StatisticUnit.BITS_PER_SECOND:
            return 'b/s'
        if unit == types.StatisticUnit.BYTES:
            return 'B'
        if unit == types.StatisticUnit.BYTES_PER_SECOND:
            return 'B/s'
        if unit == types.StatisticUnit.COUNT_PER_SECOND:
            return 'c/s'
        if unit == types.StatisticUnit.NONE:
            return ''
        if unit == types.StatisticUnit.PERCENT:
            return '%'
        if unit == types.StatisticUnit.SECONDS:
            return 's'

    def value(self):
        #todo poriesit ako to bude s viacerimi hodnotami
        # if len(self._info.values) > 0:
        if self._info.values:
            return self._info.values[0].datum
        else:
            return '--'
