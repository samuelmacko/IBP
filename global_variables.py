

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
from back.high import (
    vms, disks, hosts, storage_domains, clusters, data_centers, templates,
    nics, networks
)


USER_LOGIN = ''
FQDN = ''
ROOT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))

try:
    with open(ROOT_FILE_PATH + '/config', 'r') as config_file:
        USER_LOGIN = config_file.readline()[:-1]
        FQDN = config_file.readline()[:-1]

except Exception as e:
    print(e)

table_blueprints = [
    (vms.Vm, BuildClasses(entity_class=Vm, list_class=VmList)),
    (disks.Disk, BuildClasses(entity_class=Disk, list_class=DisksList)),
    (hosts.Host, BuildClasses(entity_class=Host, list_class=HostList)),
    (storage_domains.StorageDomains, BuildClasses(
        entity_class=Storage, list_class=StorageList
    )),
    (clusters.Cluster, BuildClasses(
        entity_class=Cluster, list_class=ClusterList
    )),
    (data_centers.DataCenter, BuildClasses(
        entity_class=DataCenter, list_class=DataCenterList
    )),
    (templates.Templates, BuildClasses(
        entity_class=Template, list_class=TemplateList
    )),
    (nics.NICs, BuildClasses(entity_class=NIC, list_class=NICsList)),
    (networks.Networks, BuildClasses(
        entity_class=Network, list_class=NetworkList
    ))
]