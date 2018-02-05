import ovirtsdk4 as sdk
import sys
# from PyQt4 import QtGui
# from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from back.high.vm import Vm
from front.main_window import Ui_MainWindow


def main():

    connection = sdk.Connection(
        username='admin@internal', password='qum5net', insecure=True,
        url='https://10-37-137-222.rhev.lab.eng.brq.redhat.com' +
            '/ovirt-engine/api',
        # ca_file=ca_file,
    )

    app = QApplication(sys.argv)
    # window = BaseWindow()

    flags = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # flags = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #          1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    #          1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # headers_list, data_list = \
    #     Vm(connection=connection, flags=flags).construct_table()
    # vm_table = Vm(connection=connection, flags=flags)
    vm_table = Vm(connection=connection)
    vm_table.construct_table()

    # table = Table(data_list=data_list, list_headers=list_headers)

    # test_table = Ui_MainWindow()


    window = QMainWindow()

    # slots = Slots(data_list=data_list, headers_list=list_headers, parent=window)

    # ui = win()
    # ui = Ui_MainWindow(data_list=data_list, headers_list=headers_list,
    #                    parent=window, flags=flags, connection=connection)
    # ui = Ui_MainWindow(data_list=vm_table.data_list,
    #                    headers_list=vm_table.headers_list,parent=window,
    #                    flags=flags, connection=connection)
    ui = Ui_MainWindow(
        parent=window, flags=flags, connection=connection, vm_table=vm_table)
    ui.setupUi(MainWindow=window)
    # ui = Ui_MainWindow(
    #     MainWindow=window, data_list=data_list, list_headers=list_headers)
    # ui.setup_tab_2(MainWindow=window, data_list=data_list, list_headers=list_headers)
    # ui.setup_tab_1(MainWindow=window, data_list=data_list, list_headers=list_headers)

    window.show()


    # test_table = Ui_MainWindow(data_list=data_list, list_headers=list_headers)
    # test_table = BaseWindow(data_list=data_list, list_headers=list_headers)
    # test_table.show()

    connection.close()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()