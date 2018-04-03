from back.low.bases import base, statisctics_base
from back.low.vm import Vm, VmList
from ovirtsdk4 import types


class TemplateList(base.ListBase):

    def __init__(self, connection):
        super(TemplateList, self).__init__(connection=connection)
        self._service = connection.system_service().templates_service()
        self._list = self._service.list()


class Template(base.SpecificBase):

    def __init__(self, connection, tplt_id):
        super(Template, self).__init__(connection=connection)
        self._service = connection.system_service().\
            templates_service().template_service(id=tplt_id)
        self._info = self._service.get()

    def status(self):
        return self._info.status.name
        # status = self._info.status
        # if status is types.TemplateStatus.ILLEGAL:
        #     return 'illegal'
        # if status is types.TemplateStatus.LOCKED:
        #     return 'locked'
        # if status is types.TemplateStatus.OK:
        #     return 'ok'

    def _cluster_obj(self):
        return self._connection.follow_link(self._info.cluster)

    def cluster(self):
        return self._cluster_obj().name

    def data_center(self):
        from back.low.cluster import Cluster
        return Cluster(
            connection=self._connection, cl_id=self._cluster_obj().id).\
            data_center()


    def os(self):
        return self._info.os.type

    def memory(self):
        return self._info.memory

    def cpu_cores(self):
        return self._info.cpu.topology.cores

    def vms(self):
        vms = []
        vm_list = VmList(connection=self._connection).list()
        for vm in vm_list:
            vm_template = Vm(connection=self._connection, vm_id=vm.id).\
                template()
            if vm_template and self.name() == vm_template:
                vms.append(vm.name)
        return vms

    def _nics_obj(self):
        return [nic for nic in self._connection.follow_link(self._info.nics)]

    def nics(self):
        return [nic.name for nic in self._nics_obj()]

    def vnics(self):
        return [self._connection.follow_link(nic.vnic_profile).id
                for nic in self._nics_obj()]

    def disks(self):
        disk_attachments = self._connection.\
            follow_link(self._info.disk_attachments)
        disks_list = []
        if disk_attachments:
            for attachment in disk_attachments:
                disk = self._connection.follow_link(attachment.disk)
                disks_list.append(disk.name)
        return disks_list
