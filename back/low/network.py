from back.low.bases import base, statisctics_base
from ovirtsdk4 import types
from back.suplementary.cell_item import CellItem


class NetworkList(base.ListBase):

    def __init__(self, connection):
        super(NetworkList, self).__init__(connection=connection)
        self._service = self._service.networks_service()
        self._list = self._service.list()


class Network(base.SpecificBase):

    def __init__(self, connection, id):
        super(Network, self).__init__(connection=connection)
        self._service = self._service.networks_service().\
            network_service(id=id)
        self._info = self._service.get()

    def data_center(self):
        name = 'Data center'
        # from back.low.data_centers import DataCenter
        return CellItem(
            name=name,
            value=self._connection.follow_link(self._info.data_center).name
        )

    def nics(self):
        name = 'NICs'
        from .nic import NIC, NICsList
        nics = []
        nics_list = NICsList(connection=self._connection).list()
        for nic in nics_list:
            nic_net = NIC(connection=self._connection, id=nic.id).\
                network_obj()
            if nic_net and nic_net.id == self.id():
                nics.append(nic.name)
        return CellItem(name=name, value=nics)

    def clusters(self):
        name = 'Clusters'
        from .cluster import Cluster, ClusterList
        clusters = []
        cl_list = ClusterList(connection=self._connection).list()
        for cl in cl_list:
            cl_nets = Cluster(connection=self._connection, id=cl.id).\
                networks_obj()
            for cl_net in cl_nets:
                if cl_net and cl_net.id == self.id():
                    clusters.append(cl.name)
        return CellItem(name=name, value=clusters)

    def hosts(self):
        name = 'Hosts'
        from .host import Host, HostList
        hosts = []
        host_list = HostList(connection=self._connection).list()
        for host in host_list:
            host_nets = Host(connection=self._connection, id=host.id). \
                networks_obj()
            for host_net in host_nets:
                if host_net and host_net.id == self.id():
                    hosts.append(host.name)
        return CellItem(name=name, value=hosts)

    def vms(self):
        name = 'VMs'
        from .vm import Vm, VmList
        vms = []
        vms_list = VmList(connection=self._connection).list()
        for vm in vms_list:
            vm_obj = Vm(connection=self._connection, id=vm.id)
            if vm_obj._status() == types.VmStatus.UP.name:
                vm_nets = vm_obj.networks_obj()
                for vm_net in vm_nets:
                    if vm_net and vm_net.id == self.id():
                        vms.append(vm.name)
        return CellItem(name=name, value=vms)


    def templates(self):
        name = 'Templates'
        from .template import Template, TemplateList
        tmps = []
        tmps_list = TemplateList(connection=self._connection).list()
        for tmp in tmps_list:
            tmp_nets = Template(connection=self._connection, id=tmp.id). \
                networks_obj()
            for tmp_net in tmp_nets:
                if tmp_net and tmp_net.id == self.id():
                    tmps.append(tmp.name)
        return CellItem(name=name, value=tmps)

    def methods_list(self):
        return [self.name, self.id, self.data_center, self.nics, self.clusters,
                self.hosts, self.vms, self.templates]
