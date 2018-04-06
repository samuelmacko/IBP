import os
import sys
import time

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from back.high import vms, disks, hosts
from back.suplementary.config_file import ConfigFile
from front.input_dialog import InputDialog
from front.main_window import Ui_MainWindow

from back.low.vm import Vm
from back.low.disk import Disk
from back.low.host import Host

# import global_variables
from global_variables import build_classes_dict


# app = QApplication(sys.argv)

def main():
    app = QApplication(sys.argv)

    dir_name = os.path.dirname(__file__)

    # splash_picture = QtGui.QPixmap('/home/smacko/git/IBP/front/'
    #                                'suplementary/images/splash_screen.png')
    splash_picture = QtGui.QPixmap(
        dir_name + '/front/suplementary/images/splash_screen.png')
    # splash_picture = QtGui.QPixmap('front/suplementary/images/splash_screen.png')
    splash_screen = QtWidgets.QSplashScreen()
    splash_screen.setPixmap(splash_picture)
    splash_screen.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint |
                                 QtCore.Qt.FramelessWindowHint)
    splash_screen.setEnabled(False)

    prog_bar = QtWidgets.QProgressBar(splash_screen)
    prog_bar.setGeometry(0, splash_screen.height() - 50,
                         splash_screen.width(), 35)
    prog_bar.setStyleSheet('QProgressBar::chunk {background: #9ACD32;}')
    prog_bar.setTextVisible(False)
    prog_bar.setMaximum(3)
    prog_bar.setValue(0)




    input_dialog = InputDialog()
    input_dialog.hide()

    splash_screen.show()


    connection = input_dialog.get_connection()

    t = time.time()
    while time.time() < t + 0.5:
        app.processEvents()


    # connection = sdk.Connection(
    #     username='admin@internal', password='qum5net', insecure=True,
    #     url='https://10-37-137-222.rhev.lab.eng.brq.redhat.com' +
    #         '/ovirt-engine/api',
    #     # ca_file=ca_file,
    # )

    flags = ConfigFile()

    vm_table = vms.Vm(connection=connection, col_flags=flags.vm_tab,
                      build_classes=build_classes_dict['VM'])
    prog_bar.setValue(1)
    disk_table = disks.Disk(connection=connection, col_flags=flags.disk_tab,
                            build_classes=build_classes_dict['Disk'])
    prog_bar.setValue(2)
    host_table = hosts.Host(connection=connection, col_flags=flags.host_tab,
                            build_classes=build_classes_dict['Host'])
    prog_bar.setValue(3)
    # tplt_table =

    window = QMainWindow()

    ui = Ui_MainWindow(
        parent=window, connection=connection, vm_table=vm_table,
        disk_table=disk_table, host_table=host_table)
    ui.setupUi(MainWindow=window)

    window.show()

    splash_screen.finish(window)

    # connection.close()

    # sys.exit(app.exec_())
    app.exec()

    connection.close()


if __name__ == '__main__':
    main()
