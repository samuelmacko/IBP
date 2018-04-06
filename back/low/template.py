from back.low.bases import base, statisctics_base
from back.low.vm import Vm, VmList
from ovirtsdk4 import types
from back.suplementary.cell_item import CellItem


class TemplateList(base.ListBase):

    def __init__(self, connection):
        super(TemplateList, self).__init__(connection=connection)
        self._service = connection.system_service().templates_service()
        self._list = self._service.list()


class Template(base.SpecificBase):

    def __init__(self, connection, id):
        super(Template, self).__init__(connection=connection)
        self._service = connection.system_service().\
            templates_service().template_service(id=id)
        self._info = self._service.get()

    def status(self):
        name = 'Status'
        return CellItem(name=name, value=self._info._status.name)

    def _cluster_obj(self):
        return self._connection.follow_link(self._info._cluster)

    def cluster(self):
        name = 'Cluster'
        return CellItem(name=name, value=self._cluster_obj().name)

    def data_center(self):
        name = 'Data center'
        from back.low.cluster import Cluster
        return CellItem(
            name=name,
            value=Cluster(
                connection=self._connection, id=self._cluster_obj().id
            ).data_center()
        )

    def os(self):
        name = 'OS'
        return CellItem(name=name, value=self._info._os.type)

    def memory(self):
        name = 'Memory'
        return CellItem(name=name, value=self._info._memory)

    def cpu_cores(self):
        name = 'CPU cores'
        return CellItem(name=name, value=self._info.cpu.topology.cores)

    def vms(self):
        name = 'VMs'
        vms = []
        vm_list = VmList(connection=self._connection).list()
        for vm in vm_list:
            vm_template = Vm(connection=self._connection, id=vm.id).\
                _template()
            if vm_template and self.name() == vm_template:
                vms.append(vm.name)
        return CellItem(name=name, value=vms)

    def _nics_obj(self):
        return [nic for nic in self._connection.follow_link(self._info._nics)]

    def nics(self):
        name = 'NICs'
        return CellItem(
            name=name,
            value=[nic.name for nic in self._nics_obj()]
        )

    def vnics_obj(self):
        return [self._connection.follow_link(nic.vnic_profile)
                for nic in self._nics_obj()]

    def networks_obj(self):
        return [self._connection.follow_link(vnic.network)
                for vnic in self.vnics_obj()]

    def disks(self):
        name = 'Disks'
        disk_attachments = self._connection.\
            follow_link(self._info.disk_attachments)
        disks_list = []
        if disk_attachments:
            for attachment in disk_attachments:
                disk = self._connection.follow_link(attachment.disk)
                disks_list.append(disk.name)
        return CellItem(name=name, value=disks_list)

    def networks(self):
        name = 'Networks'
        return CellItem(
            name=name, value=[net.name for net in self.networks_obj()]
        )

    def methods_list(self):
        return [self.name, self.id, self.status, self.cluster, self.os,
                self.data_center, self.memory, self.cpu_cores, self.vms,
                self.nics, self.disks, self.networks_obj]
