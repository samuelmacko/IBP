from back.low.bases import base
from ovirtsdk4 import types


class DataCenterList(base.ListBase):

    def __init__(self, connection):
        super(DataCenterList, self).__init__(connection=connection)
        self._service = connection.system_service().data_centers_service()
        self._list = self._service.list()


class DataCenter(base.SpecificBase):

    def __init__(self, connection, dc_id):
        super(DataCenter, self).__init__(connection=connection)
        self._service = connection.system_service(). \
            data_centers_service().data_center_service(id=dc_id)
        self._info = self._service.get()

    def status(self):
        status = self._info.status
        if status is types.DataCenterStatus.CONTEND:
            return 'contend'
        if status is types.DataCenterStatus.MAINTENANCE:
            return 'maintenance'
        if status is types.DataCenterStatus.NOT_OPERATIONAL:
            return 'not operational'
        if status is types.DataCenterStatus.PROBLEMATIC:
            return 'problematic'
        if status is types.DataCenterStatus.UNINITIALIZED:
            return 'unitialized'
        if status is types.DataCenterStatus.UP:
            return 'up'

    def storage_domains(self):
        st_domains = self._connection.follow_link(self._info.storage_domains)
        st_domains_list = []
        for domain in st_domains:
            domain = self._connection.follow_link(domain)
            st_domains_list.append(domain)
        if len(st_domains_list) > 0:
            return st_domains_list
        else:
            return None

    def networks(self):
        networks = self._connection.follow_link(self._info.networks)
        network_list = []
        for network in networks:
            network = self._connection.follow_link(network)
            network_list.append(network)
        if len(network_list) > 0:
            return network_list
        else:
            return None

    def clusters(self):
        clusters = self._connection.follow_link(self._info.clusters)
        clusters_list = []
        for cluster in clusters:
            cluster = self._connection.follow_link(cluster)
            clusters_list.append(cluster)
        if len(clusters_list) > 0:
            return clusters_list
        else:
            return None


