from back.low.bases import base, statisctics_base
# from back.low.vm import Vm, VmList
from ovirtsdk4 import types
# import back.low.vm as Vm
from back.suplementary.cell_item import CellItem


class HostList(base.ListBase):

    def __init__(self, connection):
        super(HostList, self).__init__(connection=connection)
        self._service = connection.system_service().hosts_service()
        self._list = self._service.list()


class Host(base.SpecificBase):

    def __init__(self, connection, id):
        super(Host, self).__init__(connection=connection, id=id)
        self._service = connection.system_service().\
            hosts_service().host_service(id=id)
        self._info = self._service.get()

    def _status(self):
        name = 'Status'
        return CellItem(name=name, value=self._info.status.name)

    def _address(self):
        name = 'Address'
        return CellItem(name=name, value=self._info.address)

    def cluster_obj(self):
        return self._connection.follow_link(self._info.cluster)

    def cluster(self):
        name = 'Cluster'
        return CellItem(name=name, value=self.cluster_obj().name)

    def nics_obj(self):
        nics = self._connection.follow_link(self._info.nics)
        return [nic for nic in nics]

    def _nics(self):
        name = 'NICs'
        return CellItem(name=name, value=[nic.name for nic in self.nics_obj()])

    def _vms(self):
        name = 'VMs'
        # from back.low.vm import Vm, VmList
        # _vms = []
        # vm_list = VmList(connection=self._connection).list()
        # for vm in vm_list:
        #     vm_host = Vm(connection=self._connection, vm_id=vm.id)._host()
        #     if vm_host and self._info.id == vm_host.id:
        #         _vms.append(vm)
        # if len(_vms) > 0:
        #     return _vms
        # else:
        #     return None

        from back.low.vm import Vm, VmList
        vms = []
        vm_list = VmList(connection=self._connection).list()
        for vm in vm_list:
            vm_host = Vm(connection=self._connection, id=vm.id).host_obj()
            if self._info.name == vm_host:
                vms.append(vm.name)
        return CellItem(name=name, value=vms)

    def networks_obj(self):
        network_attachments = self._connection.follow_link(
            self._info.network_attachments)
        return [self._connection.follow_link(network_att.network)
                for network_att in network_attachments]

    def _networks(self):
        name = 'Networks'
        return CellItem(name=name,
                        value=[net.name for net in self.networks_obj()])

    def methods_list(self):
        return [
            self.name, self.id, self._status, self._address, self.cluster,
            self._nics, self._vms, self._networks
        ]
