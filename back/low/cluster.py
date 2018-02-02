from back.low.base import base


class ClusterList(base.ListBase):

    def __init__(self, connection):
        super(ClusterList, self).__init__(connection=connection)
        self._service = self._service.clusters_service()
        self._list = self._service.list()

    # def id(self):
    #     cls_id = {}
    #     for cl in self._list:
    #         cl = Cluster(connection=self._connection, id=cl.id)
    #         cls_id[cl.name()] = cl.id()
    #     return cls_id
    #
    # def version(self):
    #     cls_version = {}
    #     for cl in self._list:
    #         cl = Cluster(connection=self._connection, id=cl.id)
    #         cls_version[cl.name()] = cl.version()
    #     return cls_version



class Cluster(base.SpecificBase):

    def __init__(self, connection, id):
        super(Cluster, self).__init__(connection=connection)
        self._service = self._service.clusters_service().\
            cluster_service(id=id)
        self._info = self._service.get()

    def name(self):
        return self._info.name

    def id(self):
        return self._info.id

    def version(self):
        whole_version = str(self._info.version.major) + '.'\
                        + str(self._info.version.minor)
        return whole_version