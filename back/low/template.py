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
        super(Template, self).__init__(connection=connection, id=id)
        self._service = connection.system_service().\
            templates_service().template_service(id=id)
        self._info = self._service.get()

    def status(self):
        name = 'Status'
        return CellItem(name=name, value=self._info._status.name)

    def cluster_obj(self):
        if self._info.cluster:
            return self._connection.follow_link(self._info.cluster)
        else:
            return None

    def cluster(self):
        name = 'Cluster'
        if self.cluster_obj():
            return CellItem(name=name, value=self.cluster_obj().name)
        else:
            return CellItem(name=name)

    def data_center_obj(self):
        if self.cluster_obj():
            from back.low.cluster import Cluster
            return Cluster(
                connection=self._connection, id=self.cluster_obj().id
            ).data_center_obj()
        else:
            return None

    def data_center(self):
        name = 'Data center'
        data_center = self.data_center_obj()
        if data_center:
            return CellItem(name=name, value=data_center.name)
        else:
            return CellItem(name=name)

    def os(self):
        name = 'OS'
        return CellItem(name=name, value=self._info.os.type)

    def memory(self):
        name = 'Memory'
        return CellItem(name=name, value=self._info.memory)

    def cpu_cores(self):
        name = 'CPU cores'
        return CellItem(name=name, value=self._info.cpu.topology.cores)

    def vms(self):
        name = 'VMs'
        vms = []
        vm_list = VmList(connection=self._connection).list()
        for vm in vm_list:
            vm_template = Vm(connection=self._connection, id=vm.id).\
                template_obj()
            if vm_template and self._info.id == vm_template.id:
                vms.append(vm.name)
        return CellItem(name=name, value=vms)

    def _nics_obj(self):
        return [nic for nic in self._connection.follow_link(self._info.nics)]

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

    def disks_obj(self):
        disk_attachments = self._connection. \
            follow_link(self._info.disk_attachments)
        disks_list = []
        if disk_attachments:
            for attachment in disk_attachments:
                disk = self._connection.follow_link(attachment.disk)
                disks_list.append(disk)
        return disks_list

    def disks(self):
        name = 'Disks'
        return CellItem(
            name=name, value=[disk.name for disk in self.disks_obj()]
        )

    def networks(self):
        name = 'Networks'
        return CellItem(
            name=name, value=[net.name for net in self.networks_obj()]
        )

    def storage_domains(self):
        name = 'Storage domains'
        from back.low.storage_domain import Storage, StorageList
        storage_domains = []
        storage_domains_list = StorageList(connection=self._connection).list()
        for st_domain in storage_domains_list:
            st_domain_templates = Storage(
                connection=self._connection, id=st_domain.id
            ).templates_obj()
            for st_domain_template in st_domain_templates:
                if (st_domain_template
                        and st_domain_template.id == self._info.id):
                    storage_domains.append(st_domain.name)
        return CellItem(name=name, value=storage_domains)

    def methods_list(self):
        return [
            self.name, self.id, self.status, self.cluster, self.os,
            self.data_center, self.memory, self.cpu_cores, self.vms, self.nics,
            self.disks, self.networks, self.storage_domains
        ]
