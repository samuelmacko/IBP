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
        status = self._info.status
        if status is types.TemplateStatus.ILLEGAL:
            return 'illegal'
        if status is types.TemplateStatus.LOCKED:
            return 'locked'
        if status is types.TemplateStatus.OK:
            return 'ok'

    def cluster(self):
        #todo
        return None

    def data_center(self):
        #todo
        return None

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
            if vm_template and self._info.id == vm_template:
                vms.append(vm)
        if len(vms) > 0:
            return vms
        else:
            return None

    def nics(self):
        nics = self._connection.follow_link(self._info.nics)
        nics_list = []
        if nics:
            for nic in nics:
                nic = self._connection.follow_link(nic)
                nics_list.append(nic)
        if len(nics_list) > 0:
            return nics_list
        else:
            return None

    def disks(self):
        disk_attachments = self._connection.\
            follow_link(self._info.disk_attachments)
        disks_list = []
        if disk_attachments:
            for attachment in disk_attachments:
                disk = self._connection.follow_link(attachment.disk)
                disks_list.append(disk)
        # return disks_list
        if len(disks_list) > 0:
            return disks_list
        else:
            return None
