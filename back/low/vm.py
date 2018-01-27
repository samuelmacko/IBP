# from base import TypeBase


class VmList(object):

    def __init__(self, connection):
        self.connection = connection
        self.service = connection.system_service().vms_service()
        # super(VM, self).__init__(connection=connection)
        # self.service = self.service.vms_service()


    def _get_vm_list(self):
        return self.service.list()

    def get_vm_names(self):
        vms = self._get_vm_list()
        for vm in vms:
            print("%s" % vm.name)

    def get_vm_disks(self):
        vms = self._get_vm_list()
        for vm in vms:
            Vm(connection=self.connection, id=vm.id).get_vm_info()


class Vm(object):

    def __init__(self, connection, id):
        self.connection = connection
        self.service = connection.system_service().vms_service().vm_service(id=id)

    def get_vm_info(self):
        info = self.service.get()
        print info.name
