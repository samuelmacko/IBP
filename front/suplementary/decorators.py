

def header_signal(func):
    def wrap(self, *args):
        # sender = self.centralwidget.sender()
        if len(args) > 0:
            func(self, args[0])
        else:
            func(self)

        self.tabs_dict[self.current_tab].printed_table.header.sectionClicked['int'].connect(self.header_clicked)
        self.tabs_dict[self.current_tab].printed_table.cellDoubleClicked['int', 'int'].connect(self.redirect)

        # if sender.objectName() == 'header' or \
        #         sender in self.vm_tab.chbox_list or \
        #         sender.objectName() == 'lineEdit':
        #     self.vm_tab.printed_table.header.setObjectName("header")
        #     self.vm_tab.printed_table.header.sectionClicked['int']. \
        #         connect(self.header_clicked)
        # if sender.objectName() == 'header_2' or \
        #         sender in self.disk_tab.chbox_list or \
        #         sender.objectName() == 'lineEdit_2':
        #     # pass
        #     self.disk_tab.printed_table.header.setObjectName("header_2")
        #     self.disk_tab.printed_table.header.sectionClicked['int']. \
        #         connect(self.header_clicked)
        #     # self.disk_tab.printed_table.header.setSortIndicator(1, 1)
        # if sender.objectName() == 'header_3' or \
        #         sender in self.host_tab.chbox_list or \
        #         sender.objectName() == 'lineEdit_3':
        #     self.host_tab.printed_table.header.setObjectName("header_3")
        #     self.host_tab.printed_table.header.sectionClicked['int']. \
        #         connect(self.header_clicked)
    return wrap
