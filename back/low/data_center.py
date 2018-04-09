from back.low.bases import base
from back.suplementary.cell_item import CellItem

class DataCenterList(base.ListBase):

    def __init__(self, connection):
        super(DataCenterList, self).__init__(connection=connection)
        self._service = connection.system_service().data_centers_service()
        self._list = self._service.list()


class DataCenter(base.SpecificBase):

    def __init__(self, connection, id):
        super(DataCenter, self).__init__(connection=connection, id=id)
        self._service = connection.system_service(). \
            data_centers_service().data_center_service(id=id)
        self._info = self._service.get()

    def status(self):
        name = 'Status'
        return CellItem(name=name, value=self._info._status.name)

    def version(self):
        name = 'Version'
        return CellItem(
            name=name,
            value=str(self._info.version.major) + '.' +
                  str(self._info.version.minor)
        )

    def storage_domains(self):
        name = 'Storage domains'
        st_domains = self._connection.follow_link(self._info.storage_domains)
        return CellItem(
            name=name, value=[st_domain.name for st_domain in st_domains]
        )

    def networks(self):
        name = 'Networks'
        networks = self._connection.follow_link(self._info.networks)
        return CellItem(name=name, value=[network.name for network in networks])

    def clusters(self):
        name = 'Cluster'
        clusters = self._connection.follow_link(self._info.clusters)
        return CellItem(
            name=name, value=[cluster.name for cluster in clusters]
        )

    def templates(self):
        name = 'Templates'
        from back.low.template import Template, TemplateList
        templates = []
        templates_list = TemplateList(connection=self._connection).list()
        for template in templates_list:
            template_data_center = Template(
                connection=self._connection, id=template.id
            ).data_center_obj()
            if (template_data_center
                    and template_data_center.id == self._info.id):
                templates.append(template.name)
        return CellItem(name=name, value=templates)

    def methods_list(self):
        return [
            self.name, self.id, self.status, self.version,
            self.storage_domains, self.networks, self.clusters, self.templates
        ]
