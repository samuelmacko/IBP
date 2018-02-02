from back.low.base import base
from back.low.vm import VmList


class HostList(base.ListBase):

    def __init__(self, connection):
        super(HostList, self).__init__(connection=connection)
        self._service = connection.system_service().hosts_service()
        self._list = self._service.list()

    # def hosts_name(self):
    #     return self._list.name
    #
    # def hosts_vms(self):
    #     hosts_vms ={}
    #     for host in self._list:
    #         host = Host(connection=self._connection, id=host.id)
    #         hosts_vms[host.name()] = host.vms()
    #     return hosts_vms


class Host(base.SpecificBase):

    def __init__(self, connection, id):
        super(Host, self).__init__(connection=connection)
        self._service = connection.system_service().\
            hosts_service().host_service(id=id)
        self._info = self._service.get()

    def name(self):
        return self._info.name

    # def vms(self):
    #     vms_list = []
    #     vms_host_dict = VmList(connection=self._connection).vms_host()
    #     for vm, host in vms_host_dict.iteritems():
    #         if host == self._info.name:
    #             vms_list.append(vm)
    #     return vms_list
