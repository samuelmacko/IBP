from back.low.bases import base, statisctics_base
from back.low.vm import Vm, VmList


class NICsList(base.ListBase):

    # def __init__(self, connection, vm_id):
    #     super(NICsList, self).__init__(connection=connection)
    #     self._service = self._service.vms_service().vm_service(id=vm_id). \
    #         nics_service()
    #     self._list = self._service.list()
    def __init__(self, connection):
        super(NICsList, self).__init__(connection=connection)
        self._service = self._service.vnic_profiles_service()
        self._list = self._service.list()


class NIC(base.SpecificBase):

    # def __init__(self, connection, nic_id, vm_id):
    #     super(NIC, self).__init__(connection=connection)
    #     self._service = self._service.vms_service().vm_service(id=vm_id).\
    #         nics_service().nic_service(id=nic_id)
    #     self._info = self._service.get()

    def __init__(self, connection, nic_id):
        super(NIC, self).__init__(connection=connection)
        self._service = self._service.vnic_profiles_service().\
            profile_service(id=nic_id)
        self._info = self._service.get()

    def data_center(self):
        return self._connection.follow_link(self._info.network).\
            data_center.name

    def network(self):
        return self._connection.follow_link(self._info.network).name

    def _vms_obj(self):
        # from back.low.vm import Vm, VmList
        vms = []
        vms_list = VmList(connection=self._connection).list()
        for vm in vms_list:
            vm_vnics = Vm(connection=self._connection, vm_id=vm.id).vnics()
            for vnic in vm_vnics:
                if vnic and vnic == self.id():
                    vms.append(vm)
        return vms

    def vms(self):
        return [vm.name for vm in self._vms_obj()]


    def templates(self):
        from back.low.template import Template, TemplateList
        templates = []
        templates_list = TemplateList(connection=self._connection).list()
        for template in templates_list:
            templates_vnics = Template(
                connection=self._connection, tplt_id=template.id).vnics()
            for vnic in templates_vnics:
                if vnic and vnic == self.id():
                    templates.append(template.name)
        return templates

    def _vm_nic(self):
        # from back.low.vm import Vm
        for vm in self._vms_obj():
            for nic in Vm(connection=self._connection, vm_id=vm.id).nics_obj():
                if self._connection.follow_link(nic.vnic_profile).id == \
                        self.id():
                    return nic

    def mac_address(self):
        return self._vm_nic().mac.address

    def interface(self):
        return self._vm_nic().interface.name

class NICStatisticsList(statisctics_base.StatisticsListBase):

    def __init__(self, connection, nic_id, vm_id):
        super(NICStatisticsList, self).__init__(
            connection=connection, id=nic_id)
        self._service = self._service.vms_service().vm_service(id=vm_id).\
            nics_service().nic_service(id=nic_id).statistics_service()
        self._list = self._service.list()
        self._vm_id = vm_id

    def statistic_objects_list(self):
        statistic_objects = []
        for i in range(8):
        # for i, flag_val in enumerate(flags):
        #     if flag_val:
            statistic_objects.append(
                NICStatistic(connection=self._connection, nic_id=self._id,
                            st_id=self._list[i].id, vm_id=self._vm_id)
            )
        return statistic_objects


class NICStatistic(statisctics_base.StatisticBase):

    def __init__(self, connection, nic_id, st_id, vm_id):
        super(NICStatistic, self).__init__(connection=connection)
        self._service = self._service.vms_service().vm_service(id=vm_id).\
            nics_service().nic_service(id=nic_id).statistics_service().\
            statistic_service(id=st_id)
        self._info = self._service.get()
