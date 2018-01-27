from . import vm as vm_module


class HostList(object):

    def __init__(self, connection):
        self.connection = connection
        self.service = connection.system_service().hosts_service()
        self.list = self.service.list()

    def hosts_name(self):
        return self.list.name

    def hosts_vms(self):
        hosts_vms ={}
        for host in self.list:
            host = Host(connection=self.connection, id=host.id)
            hosts_vms[host.host_name()] = host.host_vms()
        return hosts_vms


class Host(object):

    def __init__(self, connection, id):
        self.connection = connection
        self.service = connection.system_service().hosts_service().host_service(id=id)
        self.info = self.service.get()

    def host_name(self):
        return self.info.name

    def host_vms(self):
        vms_list = []
        vms_host_dict = vm_module.VmList(connection=self.connection).vms_host()
        for vm, host in vms_host_dict.iteritems():
            if host == self.info.name:
                vms_list.append(vm)
        return vms_list
