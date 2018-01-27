import ovirtsdk4 as sdk
# from connection import Connection
from back.low.vm import Vm


def main():

    try:

        connection = sdk.Connection(
            username='admin@internal', password='qum5net', insecure=True,
            url='https://10-37-137-222.rhev.lab.eng.brq.redhat.com/ovirt-engine/api'
        )

        # vms = VM(connection=connection).get_vm_list()
        # for vm in vms:
        #     print("%s: %s" % (vm.name, vm.id))

        # vms = Vm(connection=connection)



        connection.close()
    except sdk.Error as err:
        print err

main()