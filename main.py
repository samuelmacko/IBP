import ovirtsdk4 as sdk
import sys
# from PyQt4 import QtGui
# from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from back.high.vm import Vm
from front.first_draft_2 import Ui_MainWindow as mw2


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
    list_headers, data_list = \
        Vm(connection=connection, flags=flags).construct_table()
    # table = Table(data_list=data_list, list_headers=list_headers)

    # test_table = Ui_MainWindow()


    window = QMainWindow()

    # slots = Slots(data_list=data_list, headers_list=list_headers, parent=window)

    # ui = win()
    ui = mw2(data_list=data_list, headers_list=list_headers, parent=window,
             flags=flags, connection=connection)
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