

class EntityBase(object):

    def __init__(self, connection):
        self._connection = connection
        self._service = connection.system_service()


class ListBase(EntityBase):

    def __init__(self, connection):
        super(ListBase, self).__init__(connection=connection)
        self._list = None

    def list(self):
        return self._list


class SpecificBase(EntityBase):

    def __init__(self, connection):
        super(SpecificBase, self).__init__(connection=connection)
        self._info = None

    def id(self):
        return self._info.id

    def name(self):
        return self._info.name
