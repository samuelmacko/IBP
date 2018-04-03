from back.low.bases import base
from ovirtsdk4 import types
from back.low.data_centers import DataCenterList, DataCenter


class StorageList(base.ListBase):

    def __init__(self, connection):
        super(StorageList, self).__init__(connection=connection)
        self._service = connection.system_service().storage_domains_service()
        self._list = self._service.list()


class Storage(base.SpecificBase):

    def __init__(self, connection, sd_id):
        super(Storage, self).__init__(connection=connection)
        self._service = connection.system_service(). \
            storage_domains_service().storage_domain_service(id=sd_id)
        self._info = self._service.get()

    def status(self):
        return self._info.external_status.name
        # status = self._info.status
        # if status is types.StorageDomainStatus.ACTIVATING:
        #     return 'activating'
        # if status is types.StorageDomainStatus.ACTIVE:
        #     return 'active'
        # if status is types.StorageDomainStatus.DETACHING:
        #     return 'detaching'
        # if status is types.StorageDomainStatus.INACTIVE:
        #     return 'inactive'
        # if status is types.StorageDomainStatus.LOCKED:
        #     return 'locked'
        # if status is types.StorageDomainStatus.MAINTENANCE:
        #     return 'maintenance'
        # if status is types.StorageDomainStatus.MIXED:
        #     return 'mixed'
        # if status is types.StorageDomainStatus.PREPARING_FOR_MAINTENANCE:
        #     return 'preparing for maintenance'
        # if status is types.StorageDomainStatus.UNATTACHED:
        #     return 'unattached'
        # if status is types.StorageDomainStatus.UNKNOWN:
        #     return 'unknown'

    def type(self):
        return self._info.type.name
        # if type is types.StorageDomainType.DATA:
        #     return 'data'
        # if type is types.StorageDomainType.EXPORT:
        #     return 'export'
        # if type is types.StorageDomainType.IMAGE:
        #     return 'image'
        # if type is types.StorageDomainType.ISO:
        #     return 'iso'
        # if type is types.StorageDomainType.VOLUME:
        #     return 'volume'

    def storage_type(self):
        return self._info.storage.type.name

    def storage_address(self):
        # return self._info.storage.address
        return self._info.storage.address + self._info.storage.path

    def format(self):
        return self._info.storage_format

    def available_space(self):
        return self._info.available

    def used_space(self):
        return self._info.used

    def data_center(self):
        from back.low.data_centers import DataCenter
        data_centers_list = DataCenterList(connection=self._connection).list()
        # for data_center in data_centers_list:
        #     dc_storages = DataCenter(
        #         connection=self._connection, dc_id=data_center.id).\
        #         storage_domains()
        #     if dc_storages:
        #         for dc_storage in dc_storages:
        #             if self._info.id == dc_storage.id:
        #                 return data_center
        # return None
        return [DataCenter(connection=self._connection, dc_id=dc.id).name()
                for dc in data_centers_list]

    def vms(self):
        vms = self._connection.follow_link(self._info.vms)
        return [vm.name for vm in vms]

    def disks(self):
        disks = self._connection.follow_link(self._info.disks)
        return [disk.name for disk in disks]

    def templates(self):
        templates = self._connection.follow_link(self._info.templates)
        return [template.name for template in templates]
