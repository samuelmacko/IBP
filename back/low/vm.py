


class VmList(object):

    def __init__(self, connection):
        self.connection = connection
        self.service = connection.system_service().vms_service()
        # super(VM, self).__init__(connection=connection)
        # self.service = self.service.vms_service()
        self.list = self.service.list()

    def vms_name(self):
        return self.list.name

    def vms_disks(self):
        vms_disks = {}
        for vm in self.list:
            vm = Vm(connection=self.connection, id=vm.id)
            vms_disks[vm.vm_name()] = vm.vm_disks()
        return vms_disks

    def vms_host(self):
        vms_host = {}
        for vm in self.list:
            vm = Vm(connection=self.connection, id=vm.id)
            vms_host[vm.vm_name()] = vm.vm_host()
        return vms_host


class Vm(object):

    def __init__(self, connection, id):
        self.connection = connection
        self.service = connection.system_service().vms_service().vm_service(id=id)
        self.info = self.service.get()

    def vm_name(self):
        # print self.info.name
        return self.info.name

    def vm_disks(self):
        disk_attachments = self.connection.follow_link(self.info.disk_attachments)
        disks_list = []
        for attachment in disk_attachments:
            disk = self.connection.follow_link(attachment.disk).name
            disks_list.append(disk)
        return disks_list

    def vm_os(self):
        print self.info.os.type

    def vm_nic_name(self):
        nics = self.connection.follow_link(self.info.nics)
        for nic in nics:
            print '%s : %s' % (self.info.name, nic.name)

    def vm_host(self):
        if self.info.host == None:
            return None
        else:
            return self.connection.follow_link(self.info.host).name
