from back.low.vm import Vm
from back.low.disks import DisksList
from back.low.disks import Disk as disk_low
from back.low.disks import DiskStatisticsList
from collections import OrderedDict
from back.high.bases.base import HighBase
import operator


class Disk(HighBase):
     def __init__(self, connection):
         super(Disk, self).__init__(connection=connection)
         self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

     def construct_table(self):
         table = []
         header = ['name']

         disks_list = DisksList(connection=self._connection).list()

         for n, disk_row in disks_list:
             self.row_flags.append(1)
             table_row = []

             disk = disk_low(connection=self._connection, dk_id=disk_row.id)

             table_row.append(disk.name())

             method_dict = OrderedDict([
                 ('status', disk.status), ('id', disk.id), ('size', disk.size),
                 ('format', disk.format), ('type', disk.type),
                 ('storage type', disk.storage_type)
             ])
             for i, method in enumerate(method_dict.items()):
                 if n == 0:
                     header.append(method[0])
                 table_row.append(method[1]())

             dk_st_list = DiskStatisticsList(
                 connection=self._connection, dk_id=disk.id()).\
                 statistic_objects_list()
             for i, value in enumerate(dk_st_list):
                 if value:
                     if n == 0:
                         header.append(dk_st_list[i].name())
                     table_row.append(
                         str(dk_st_list[i].value() + ' '
                             + str(dk_st_list[i].unit()))
                     )

