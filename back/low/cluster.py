from back.low.bases import base
from back.suplementary.cell_item import CellItem


class ClusterList(base.ListBase):

    def __init__(self, connection):
        super(ClusterList, self).__init__(connection=connection)
        self._service = self._service.clusters_service()
        self._list = self._service.list()


class Cluster(base.SpecificBase):

    def __init__(self, connection, id):
        super(Cluster, self).__init__(connection=connection, id=id)
        self._service = self._service.clusters_service().\
            cluster_service(id=id)
        self._info = self._service.get()

    def version(self):
        name = 'Version'
        whole_version = str(self._info.version.major) + '.'\
                        + str(self._info.version.minor)
        return CellItem(name=name, value=whole_version)

    def data_center_obj(self):
        return self._connection.follow_link(self._info.data_center)

    def data_center(self):
        name = 'Data center'
        return CellItem(name=name, value=self.data_center_obj().name)

    def hosts(self):
        name = 'Hosts'
        from back.low.host import Host, HostList
        hosts = []
        host_list = HostList(connection=self._connection).list()
        for host in host_list:
            host_cluster = Host(
                connection=self._connection, id=host.id).cluster_obj()
            if host_cluster and self._info.id == host_cluster.id:
                hosts.append(host.name)
        return CellItem(name=name, value=hosts)

    def vms(self):
        name = 'VMs'
        from back.low.vm import Vm, VmList
        vms = []
        vm_list = VmList(connection=self._connection).list()
        for vm in vm_list:
            vm_cluster = Vm(connection=self._connection, id=vm.id).\
                cluster_obj()
            if vm_cluster and self._info.id == vm_cluster.id:
                vms.append(vm.name)
        return CellItem(name=name, value=vms)

    #todo asi moze byt aj ine ako on_error (href?)
    def error_handling(self):
        name = 'Error handling'
        return CellItem(
            name=name, value=self._info.error_handling.on_error.name
        )

    def cpu(self):
        name = 'Name'
        return CellItem(
            name=name,
            value=str(self._info.cpu.architecture) + ' ' +
                  str(self._info.cpu.type)
        )

    def firewall(self):
        name = 'Firewall'
        return CellItem(name=name, value=self._info.firewall_type.name)

    def networks_obj(self):
        return [network for network in
                self._connection.follow_link(self._info.networks)]

    def networks(self):
        name = 'Networks'
        return CellItem(
            name=name,
            value=[network.name for network in self.networks_obj()]
        )

    def templates(self):
        name = 'Templates'
        from back.low.template import Template, TemplateList
        templates_list = TemplateList(connection=self._connection).list()
        for template in templates_list:
            template_cluster = Template(
                connection=self._connection, id=template.id
            ).cluster_obj()
            if template_cluster and template_cluster.id == self._info.id:
                return CellItem(name=name, value=template_cluster.name)
        return CellItem(name=name)

    def methods_list(self):
        return [
            self.name, self.id, self.version, self.data_center, self.hosts,
            self.vms, self.error_handling, self.cpu, self.firewall,
            self.networks, self.templates
        ]
