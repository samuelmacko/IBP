import ovirtsdk4 as sdk
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from back.high import vm, disk, host
from front.main_window import Ui_MainWindow
from front.suplementary.config_file import ConfigFile

from front.input_dialog import InputDialog

# app = QApplication(sys.argv)

def main():
    app = QApplication(sys.argv)


    input_dialog = InputDialog()
    # inp.show()
    # inp.hide()

    connection = input_dialog.get_connection()


    # connection = sdk.Connection(
    #     username='admin@internal', password='qum5net', insecure=True,
    #     url='https://10-37-137-222.rhev.lab.eng.brq.redhat.com' +
    #         '/ovirt-engine/api',
    #     # ca_file=ca_file,
    # )

    flags = ConfigFile()

    # app = QApplication(sys.argv)
    vm_table = vm.Vm(connection=connection, col_flags=flags.vm_tab)
    disk_table = disk.Disk(connection=connection, col_flags=flags.disk_tab)
    host_table = host.Host(connection=connection, col_flags=flags.host_tab)
    # tplt_table =

    # connection.close()

    window = QMainWindow()

    ui = Ui_MainWindow(
        parent=window, connection=connection, vm_table=vm_table,
        disk_table=disk_table, host_table=host_table)
    ui.setupUi(MainWindow=window)

    input_dialog.hide()

    window.show()


    # connection.close()

    # sys.exit(app.exec_())
    app.exec()

    connection.close()


if __name__ == '__main__':
    main()
    # print('aaaaa')
    # sys.exit(app.exec_())