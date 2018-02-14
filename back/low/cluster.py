from back.low.bases import base
# from back.low.host import Host, HostList
# from back.low.vm import Vm, VmList
# import back.low.vm as Vm
# import back.low.host as Host


class ClusterList(base.ListBase):

    def __init__(self, connection):
        super(ClusterList, self).__init__(connection=connection)
        self._service = self._service.clusters_service()
        self._list = self._service.list()


class Cluster(base.SpecificBase):

    def __init__(self, connection, cl_id):
        super(Cluster, self).__init__(connection=connection)
        self._service = self._service.clusters_service().\
            cluster_service(id=cl_id)
        self._info = self._service.get()

    def version(self):
        whole_version = str(self._info.version.major) + '.'\
                        + str(self._info.version.minor)
        return whole_version

    def data_center(self):
        #todo vracia meno a nie objekt
        return self._connection.follow_link(self._info.datacenters).name

    def hosts(self):
        hosts = []
        host_list = Host.HostList(connection=self._connection).list()
        for host in host_list:
            host_cluster = Host.Host(
                connection=self._connection, host_id=host.id).cluster()
            if host_cluster and self._info.name == host_cluster:
                hosts.append(host)
        if len(hosts) > 0:
            return hosts
        else:
            return None

    # def vms(self):
    #     vms = []
    #     # vm_list = VmList(connection=self._connection).list()
    #     vm_list = Vm.VmList(connection=self._connection).list()
    #     for vm in vm_list:
    #         vm_cluster = Vm.Vm(connection=self._connection, vm_id=vm.id).\
    #             cluster()
    #         if vm_cluster and self._info.name == vm_cluster:
    #             vms.append(vm)
    #     if len(vms) > 0:
    #         return vms
    #     else:
    #         return None
