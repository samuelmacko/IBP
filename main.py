import ovirtsdk4 as sdk
from front.base_window import BaseWindow
from front.table import Table
import sys
from PyQt4 import QtGui
from back.high.vm import Vm


def main():

    connection = sdk.Connection(
        username='admin@internal', password='qum5net', insecure=True,
        url='https://10-37-137-222.rhev.lab.eng.brq.redhat.com' +
            '/ovirt-engine/api',
        # ca_file=ca_file,
    )


    app = QtGui.QApplication(sys.argv)
    # window = BaseWindow()

    flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    list_headers, data_list = \
        Vm(connection=connection, flags=flags).construct_table()
    table = Table(data_list=data_list, list_headers=list_headers)

    connection.close()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()