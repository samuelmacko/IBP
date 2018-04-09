import os
import sys
import time

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow

from back.high import (
    vms, disks, hosts, storage_domains, clusters, data_centers, templates,
    nics, networks
)
from back.suplementary.config_file import ConfigFile
from front.input_dialog import InputDialog
from front.main_window import Ui_MainWindow

# from back.low.vm import Vm
# from back.low.disk import Disk
# from back.low.host import Host

# import global_variables
from global_variables import table_blueprints


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
    prog_bar.setMaximum(9)
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

    tables_list = []
    for i, table_blueprint in enumerate(table_blueprints):
        prog_bar.setValue(i)

        tables_list.append(
            table_blueprint[0](
                connection=connection, col_flags=flags.tab_flags[0],
                build_classes=table_blueprint[1]
            )
        )
        tables_list[i].construct_table()



    # vms_table = vms.Vm(
    #     connection=connection, col_flags=flags.tab_flags[0],
    #     build_classes=table_blueprints['VM']
    # )
    # vms_table.construct_table()
    # # ).construct_table()
    # prog_bar.setValue(1)
    # disks_table = disks.Disk(
    #     connection=connection, col_flags=flags.tab_flags[1],
    #     build_classes=table_blueprints['Disk']
    # )
    # disks_table.construct_table()
    # prog_bar.setValue(2)
    # hosts_table = hosts.Host(
    #     connection=connection, col_flags=flags.tab_flags[2],
    #     build_classes=table_blueprints['Host']
    # )
    # hosts_table.construct_table()
    # prog_bar.setValue(3)
    # st_domains_table = storage_domains.StorageDomains(
    #     connection=connection, col_flags=flags.tab_flags[3],
    #     build_classes=table_blueprints['StorageDomains']
    # )
    # st_domains_table.construct_table()
    # prog_bar.setValue(4)
    # clusters_table = clusters.Cluster(
    #     connection=connection, col_flags=flags.tab_flags[4],
    #     build_classes=table_blueprints['Clusters']
    # )
    # clusters_table.construct_table()
    # prog_bar.setValue(5)
    # data_centers_table = data_centers.DataCenter(
    #     connection=connection, col_flags=flags.tab_flags[5],
    #     build_classes=table_blueprints['DataCenters']
    # )
    # data_centers_table.construct_table()
    # prog_bar.setValue(6)
    # templates_table = templates.Templates(
    #     connection=connection, col_flags=flags.tab_flags[6],
    #     build_classes=table_blueprints['Templates']
    # )
    # templates_table.construct_table()
    # prog_bar.setValue(7)
    # nics_table = nics.NICs(
    #     connection=connection, col_flags=flags.tab_flags[7],
    #     build_classes=table_blueprints['NICs']
    # )
    # nics_table.construct_table()
    # prog_bar.setValue(8)
    # networks_table = networks.Networks(
    #     connection=connection, col_flags=flags.tab_flags[8],
    #     build_classes=table_blueprints['Networks']
    # )
    # networks_table.construct_table()
    # prog_bar.setValue(9)

    window = QMainWindow()

    ui = Ui_MainWindow(
        parent=window, connection=connection, tables_list=tables_list
        # vms_table=vms_table,
        # disks_table=disks_table, hosts_table=hosts_table,
        # st_domains_table=st_domains_table, clusters_table=clusters_table,
        # data_centers_table=data_centers_table, templates_table=templates_table,
        # nics_table=nics_table, networks_table=networks_table
    )
    ui.setupUi(MainWindow=window)

    window.show()

    splash_screen.finish(window)

    # connection.close()

    # sys.exit(app.exec_())
    app.exec()

    connection.close()


if __name__ == '__main__':
    main()
