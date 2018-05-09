

import csv
import os
from back.suplementary.config_file import create_config_file
from front.suplementary.decorators import header_signal
from front.suplementary.tab_sockets import *
import global_variables
from front.suplementary.compute_shift import compute_shift

from PyQt5 import QtWidgets, QtGui, Qt, QtCore


class Ui_MainWindow(object):

    def __init__(self, parent, connection, tables_list):
        self.parent = parent
        self.connection = connection
        self.dir_name = os.path.dirname(__file__)

        self.tabs_list = [
            VMsTab(table=tables_list[0], parent=parent),
            DisksTab(table=tables_list[1], parent=parent),
            HostsTab(table=tables_list[2], parent=parent),
            StorageDomainsTab(table=tables_list[3], parent=parent),
            ClustersTab(table=tables_list[4], parent=parent),
            DataCentersTab(table=tables_list[5], parent=parent),
            TemplatesTab(table=tables_list[6], parent=parent),
            NICsTab(table=tables_list[7], parent=parent),
            NetworksTab(table=tables_list[8], parent=parent)
        ]

        self.current_tab = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)


        for tab in self.tabs_list:

            tab.tab_widget = QtWidgets.QWidget()
            tab.horizontal_layouts[0] = QtWidgets.QHBoxLayout(tab.tab_widget)
            tab.vertical_layouts = QtWidgets.QVBoxLayout()
            tab.horizontal_layouts[1] = QtWidgets.QHBoxLayout()
            tab.tool_btn = QtWidgets.QToolButton(self.centralwidget)
            tab.tool_btn.setText('Select Column ')
            tab.tool_menu = QtWidgets.QMenu(self.centralwidget)
            for i in range(len(tab.values_table.col_flags)):
                action = tab.tool_menu.addAction(
                    tab.values_table.headers_list[i]
                )
                action.setCheckable(True)
                action.setChecked(tab.values_table.col_flags[i])
                action.changed.connect(self.checkbox_clicked)
                tab.chbox_list.append(action)
            tab.tool_btn.setMenu(tab.tool_menu)
            tab.tool_btn.setPopupMode(QtWidgets.QToolButton.InstantPopup)
            tab.horizontal_layouts[1].addWidget(tab.tool_btn)
            tab.line_edit = QtWidgets.QLineEdit(tab.tab_widget)
            tab.line_edit.returnPressed.connect(self.line_edit_changed)
            tab.refresh_btn = QtWidgets.QPushButton(tab.tab_widget)
            tab.refresh_btn.clicked['bool'].connect(self.refresh)

            tab.refresh_btn.setIcon(
                QtGui.QIcon(self.dir_name + '/suplementary/images/refresh.gif')
            )
            tab.refresh_btn.setIconSize(QtCore.QSize(20, 20))

            tab.horizontal_layouts[1].addWidget(tab.refresh_btn)
            tab.horizontal_layouts[1].addWidget(tab.line_edit)
            tab.horizontal_layouts[0].addLayout(tab.vertical_layouts)
            tab.vertical_layouts.addLayout(tab.horizontal_layouts[1])

            self.tabWidget.addTab(tab.tab_widget, "")


        self.tab_changed(tab_number=0)


        self.horizontalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.triggered['bool'].connect(self.menu_item_clicked)

        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionExport.triggered['bool'].connect(self.export)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExport)
        self.menubar.addAction(self.menuFile.menuAction())

        self.tabWidget.tabBarClicked['int'].connect(self.tab_changed)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[0].tab_widget), _translate("MainWindow", "Virtual Machines"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[1].tab_widget), _translate("MainWindow", "Disks"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[2].tab_widget), _translate("MainWindow", "Hosts"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[3].tab_widget), _translate("MainWindow", "Storage Domains"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[4].tab_widget), _translate("MainWindow", "Clusters"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[5].tab_widget), _translate("MainWindow", "Data Centers"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[6].tab_widget), _translate("MainWindow", "Templates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[7].tab_widget), _translate("MainWindow", "NICs"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs_list[8].tab_widget), _translate("MainWindow", "Networks"))

        self.menuFile.setTitle(_translate("MainWindow", "file"))
        self.actionSave.setText(_translate("MainWindow", "save"))
        self.actionExport.setText(_translate("MainWindow", "export"))

    def tab_changed(self, tab_number):
        self.current_tab = tab_number

        self.tabs_list[self.current_tab].print_table()
        self.tabs_list[self.current_tab].printed_table.\
            header.sectionClicked['int'].connect(self.header_clicked)
        self.tabs_list[self.current_tab].printed_table.\
            cellDoubleClicked['int', 'int'].connect(self.redirect)

    @header_signal
    def checkbox_clicked(self):
        sender = self.centralwidget.sender()

        self.tabs_list[self.current_tab].checkbox_handle(sender=sender)

    @header_signal
    def line_edit_changed(self):
        sender = self.centralwidget.sender()

        self.tabs_list[self.current_tab].line_edit_handle(text=sender.text())

    @header_signal
    def header_clicked(self, col):
        self.tabs_list[self.current_tab].sort_column(col=col)

    def menu_item_clicked(self, bool):
        sender = self.centralwidget.sender()
        if sender.objectName() == 'actionSave':
            create_config_file(tabs_list=self.tabs_list)

    @header_signal
    def refresh(self, clicked=None):
        # sender = self.centralwidget.sender()
        self.parent.setDisabled(True)


        message_box = QtWidgets.QMessageBox(self.parent)
        message_box.setWindowTitle('Refreshing')
        message_box.setStandardButtons(Qt.QMessageBox.NoButton)

        message_box.addButton('Please wait...', QtWidgets.QMessageBox.YesRole)

        prog_bar = QtWidgets.QProgressBar(message_box)
        prog_bar.setStyleSheet('QProgressBar::chunk {background: #9ACD32;}')
        prog_bar.setGeometry(0, 10, message_box.width() + 35, 20)
        prog_bar.setTextVisible(False)
        prog_bar.setMaximum(
            len(self.tabs_list[self.current_tab].values_table.data_list)
        )
        prog_bar.setValue(0)

        message_box.open()

        import time
        t = time.time()
        while time.time() < t + 0.5:
            QtWidgets.QApplication.processEvents()

        self.tabs_list[self.current_tab].values_table = \
            global_variables.table_blueprints[self.current_tab][0](
                connection=self.connection,
                build_classes=global_variables.table_blueprints[
                    self.current_tab][1]
            )

        for i in self.tabs_list[self.current_tab].\
                values_table.construct_table():
            prog_bar.setValue(i)
        self.tabs_list[self.current_tab].print_table()

        self.parent.setDisabled(False)

        message_box.close()


    def export(self):
        file_name = QtWidgets.QFileDialog.getSaveFileName(
            self.parent, 'Open file', '/home')
        if file_name[0]:
            with open(file_name[0], 'w') as file:
                writer = csv.writer(file)
                self.tabs_list[self.current_tab].values_table.\
                    table_from_flags()
                writer.writerow(
                    self.tabs_list[self.current_tab].values_table.
                        current_headers_list)
                writer.writerows(
                    self.tabs_list[self.current_tab].values_table.
                        current_data_list)

    @header_signal
    def redirect(self, row, col):
        sender = self.centralwidget.sender()
        print("sender:", sender, "row:", row, "col:", col)

        col = compute_shift(
            col_flags=self.tabs_list[self.current_tab].values_table.col_flags,
            current_col=col
        )

        # print('shifted col:', col)

        if col in self.tabs_list[self.current_tab].redirect_dict:
            target_tab = self.tabs_list[self.current_tab].redirect_dict[col][0]
            source_tab =self.tabs_list[self.current_tab].redirect_dict[col][1]
            cell_text = self.tabs_list[self.current_tab].values_table.\
                current_data_list[row][0]

            self.tab_changed(tab_number=target_tab)
            self.tabWidget.setCurrentIndex(target_tab)

            search_string = \
                self.tabs_list[self.current_tab].values_table.\
                    headers_list[source_tab] + ' = ' + cell_text

            self.tabs_list[self.current_tab].line_edit.setText(search_string)
            self.tabs_list[target_tab].line_edit_handle(text=search_string)

