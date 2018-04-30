

import os
import sys
import time

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from back.suplementary.config_file import ConfigFile
from front.input_dialog import InputDialog
from front.main_window import Ui_MainWindow
from global_variables import table_blueprints


def main():
    app = QApplication(sys.argv)

    dir_name = os.path.dirname(__file__)
    splash_picture = QtGui.QPixmap(
        dir_name + '/front/suplementary/images/splash_screen.png')
    splash_screen = QtWidgets.QSplashScreen()
    splash_screen.setPixmap(splash_picture)
    splash_screen.setWindowFlags(
        QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint
    )
    splash_screen.setEnabled(False)

    prog_bar = QtWidgets.QProgressBar(splash_screen)
    prog_bar.setGeometry(
        0, splash_screen.height() - 50, splash_screen.width(), 35
    )
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

    flags = ConfigFile()

    tables_list = []
    for i, table_blueprint in enumerate(table_blueprints):
        prog_bar.setValue(i)

        tables_list.append(
            table_blueprint[0](
                connection=connection, col_flags=flags.tab_flags[i],
                build_classes=table_blueprint[1]
            )
        )
        for _ in tables_list[i].construct_table():
            pass

    window = QMainWindow()

    ui = Ui_MainWindow(
        parent=window, connection=connection, tables_list=tables_list
    )
    ui.setupUi(MainWindow=window)

    window.show()

    splash_screen.finish(window)

    app.exec()

    connection.close()


if __name__ == '__main__':
    main()
