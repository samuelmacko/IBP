import os
from back.suplementary.build_classes import BuildClasses
from back.low.vm import *
from back.low.disk import *
from back.low.host import *
from back.low.storage_domain import *
from back.low.cluster import *
from back.low.data_center import *
from back.low.template import *
from back.low.nic import *
from back.low.network import *


USER_LOGIN = ''
FQDN = ''
ROOT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))

# try:
#     with open(ROOT_FILE_PATH + '/config2', 'r') as config_file:
#         USER_LOGIN = config_file.readline()[:-1]
#         FQDN = config_file.readline()[:-1]
#
# except Exception as e:
#     print(e)

build_classes_dict = {
    'VM': BuildClasses(entity_class=Vm, list_class=VmList),
    'Disk': BuildClasses(entity_class=Disk, list_class=DisksList),
    'Host': BuildClasses(entity_class=Host, list_class=HostList),
    'StorageDomains': BuildClasses(
        entity_class=Storage, list_class=StorageList
    ),
    'Clusters': BuildClasses(entity_class=Cluster, list_class=ClusterList),
    'DataCenters': BuildClasses(
        entity_class=DataCenter, list_class=DataCenterList
    ),
    'Templates': BuildClasses(entity_class=Template, list_class=TemplateList),
    'NICs': BuildClasses(entity_class=NIC, list_class=NICsList),
    'Networks': BuildClasses(entity_class=Network, list_class=NetworkList),
}