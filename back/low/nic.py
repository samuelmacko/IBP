

from back.low.bases import base
from back.low.vm import Vm, VmList
from back.suplementary.cell_item import CellItem


class NICsList(base.ListBase):

    def __init__(self, connection):
        super(NICsList, self).__init__(connection=connection)
        self._service = self._service.vnic_profiles_service()
        self._list = self._service.list()


class NIC(base.SpecificBase):

    def __init__(self, connection, id):
        super(NIC, self).__init__(connection=connection, id=id)
        self._service = self._service.vnic_profiles_service().\
            profile_service(id=id)
        self._info = self._service.get()

    def data_center(self):
        name = 'Data center'
        from back.low.data_center import DataCenter
        data_center = self._connection.follow_link(self._info.network).\
            data_center

        return CellItem(
            name=name,
            value=DataCenter(
                connection=self._connection, id=data_center.id
            ).name().value
        )

    def network_obj(self):
        return self._connection.follow_link(self._info.network)

    def network(self):
        name = 'Network'
        return CellItem(
            name=name,
            value=self._connection.follow_link(self._info.network).name
        )

    def _vms_obj(self):
        vms = []
        vms_list = VmList(connection=self._connection).list()
        for vm in vms_list:
            vm_vnics = Vm(connection=self._connection, id=vm.id).vnics_obj()
            for vnic in vm_vnics:
                if vnic and vnic.id == self._info.id:
                    vms.append(vm)
        return vms

    def vms(self):
        name = 'VMs'
        return CellItem(name=name, value=[vm.name for vm in self._vms_obj()])

    def templates(self):
        name = 'Templates'
        from .template import Template, TemplateList
        templates_list = TemplateList(connection=self._connection).list()
        for template in templates_list:
            templates_vnics = Template(
                connection=self._connection, id=template.id).vnics_obj()
            return CellItem(
                name=name,
                value=[vnic for vnic in templates_vnics
                       if vnic and vnic.id == self._info.id]
            )

    def _vm_nic(self):
        for vm in self._vms_obj():
            for nic in Vm(connection=self._connection, id=vm.id).nics_obj():
                if (self._connection.follow_link(nic.vnic_profile).id ==
                        self._info.id):
                    return nic
        return None

    def mac_address(self):
        name = 'MAC address'
        if self._vm_nic():
            return CellItem(name=name, value=self._vm_nic().mac.address)
        else:
            return CellItem(name=name)

    def interface(self):
        name = 'Interface'
        if self._vm_nic():
            return CellItem(name=name, value=self._vm_nic().interface.name)
        else:
            return CellItem(name=name)

    def hosts(self):
        name = 'Hosts'
        from back.low.host import Host, HostList
        hosts = []
        hosts_list = HostList(connection=self._connection).list()
        for host in hosts_list:
            host_nics = Host(
                connection=self._connection, id=host.id).nics_obj()
            for host_nic in host_nics:
                if host_nic and host_nic.id == self._info.id:
                    hosts.append(host.name)
        return CellItem(name=name, value=hosts)

    def methods_list(self):
        return [
            self.name, self.id, self.data_center, self.network, self.vms,
            self.templates, self.mac_address, self.interface, self.hosts
        ]
