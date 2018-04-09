from back.low.bases import base
from back.low.data_center import DataCenterList, DataCenter
from back.suplementary.cell_item import CellItem


class StorageList(base.ListBase):

    def __init__(self, connection):
        super(StorageList, self).__init__(connection=connection)
        self._service = connection.system_service().storage_domains_service()
        self._list = self._service.list()


class Storage(base.SpecificBase):

    def __init__(self, connection, id):
        super(Storage, self).__init__(connection=connection, id=id)
        self._service = connection.system_service(). \
            storage_domains_service().storage_domain_service(id=id)
        self._info = self._service.get()

    def status(self):
        name = 'Status'
        return CellItem(name=name, value=self._info.external_status.name)

    def type(self):
        name = 'Type'
        return CellItem(name=name, value=self._info.type.name)

    def storage_type(self):
        name = 'Storage type'
        return CellItem(name=name, value=self._info.storage.type.name)

    def storage_address(self):
        name = 'Storage address'
        # return self._info.storage._address
        return CellItem(
            name=name,
            value=self._info.storage._address + self._info.storage.path
        )

    def format(self):
        name = 'Format'
        return CellItem(name=name, value=self._info.storage_format)

    def available_space(self):
        name = 'Available space'
        return CellItem(name=name, value=self._info.available)

    def used_space(self):
        name = 'Used space'
        return CellItem(name=name, value=self._info.used)

    def data_center(self):
        name = 'Data center'
        from back.low.data_center import DataCenter
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
        return CellItem(
            name=name,
            value=[DataCenter(
                connection=self._connection, id=dc.id).name().value
                   for dc in data_centers_list]
        )

    def vms_obj(self):
        return [vm for vm in self._connection.follow_link(self._info.vms)]

    def vms(self):
        name = 'VMs'
        return CellItem(name=name, value=[vm for vm in self.vms_obj()])

    def disks(self):
        name = 'Disks'
        disks = self._connection.follow_link(self._info._disks)
        return CellItem(name=name, value=[disk.name for disk in disks])

    def templates_obj(self):
        templates = self._connection.follow_link(self._info.templates)
        return [template for template in templates]

    def templates(self):
        name = 'Templates'
        return CellItem(
            name=name,
            value=[template.name for template in self.templates_obj()]
        )

    def methods_list(self):
        return [
            self.name, self.id, self.status, self.type, self.storage_type,
            self.storage_address, self.format, self.available_space,
            self.used_space, self.data_center, self.vms, self.disks,
            self.templates
        ]
