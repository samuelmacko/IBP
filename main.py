import ovirtsdk4 as sdk
import sys
# from PyQt4 import QtGui
# from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from back.high import vm, disk
from front.main_window import Ui_MainWindow


def main():

    connection = sdk.Connection(
        username='admin@internal', password='qum5net', insecure=True,
        url='https://10-37-137-222.rhev.lab.eng.brq.redhat.com' +
            '/ovirt-engine/api',
        # ca_file=ca_file,
    )

    app = QApplication(sys.argv)
    vm_table = vm.Vm(connection=connection)
    disk_table = disk.Disk(connection=connection)


    window = QMainWindow()

    ui = Ui_MainWindow(
        parent=window, connection=connection, vm_table=vm_table,
        disk_table=disk_table)
    ui.setupUi(MainWindow=window)

    window.show()


    connection.close()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()