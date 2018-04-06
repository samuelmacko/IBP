from back.low.bases import base
from back.suplementary.cell_item import CellItem

class DataCenterList(base.ListBase):

    def __init__(self, connection):
        super(DataCenterList, self).__init__(connection=connection)
        self._service = connection.system_service().data_centers_service()
        self._list = self._service.list()


class DataCenter(base.SpecificBase):

    def __init__(self, connection, id):
        super(DataCenter, self).__init__(connection=connection)
        self._service = connection.system_service(). \
            data_centers_service().data_center_service(id=id)
        self._info = self._service.get()

    def status(self):
        name = 'Status'
        return CellItem(name=name, value=self._info._status.name)

    def version(self):
        name = 'Version'
        return CellItem(
            name=name, value=str(self._info.version.major) + '.' +
                             str(self._info.version.minor)
        )

    def storage_domains(self):
        name = 'Storage domains'
        st_domains = self._connection.follow_link(self._info.storage_domains)
        # st_domains_list = []
        # for domain in st_domains:
        #     domain = self._connection.follow_link(domain)
        #     st_domains_list.append(domain)
        # if len(st_domains_list) > 0:
        #     return st_domains_list
        # else:
        #     return None
        return CellItem(
            name=name, value=[st_domain.name for st_domain in st_domains]
        )

    # def _networks(self):
    #     _networks = self._connection.follow_link(self._info._networks)
    #     network_list = []
    #     for network in _networks:
    #         network = self._connection.follow_link(network)
    #         network_list.append(network)
    #     if len(network_list) > 0:
    #         return network_list
    #     else:
    #         return None

    def networks(self):
        name = 'Networks'
        networks = self._connection.follow_link(self._info._networks)
        return CellItem(name=name, value=[network for network in networks])

    def clusters(self):
        name = 'Cluster'
        clusters = self._connection.follow_link(self._info.clusters)
        return CellItem(
            name=name, value=[cluster.name for cluster in clusters]
        )

    def methods_list(self):
        return [self.name, self.id, self.status, self.version,
                self.storage_domains, self.networks, self.clusters]
