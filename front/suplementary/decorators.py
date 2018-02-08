

def header_signal(func):
    def wrap(self, *args):
        sender = self.centralwidget.sender()
        if len(args) > 0:
            func(self, args[0])
        else:
            func(self)
        if sender.objectName() == 'header' or \
                sender.objectName() == 'lineEdit':
            self.vm_tab.printed_table.header.setObjectName("header")
            self.vm_tab.printed_table.header.sectionClicked['int']. \
                connect(self.header_clicked)
        if sender.objectName() == 'header_2' or \
                sender in self.disk_tab.chbox_list or \
                sender.objectName() == 'lineEdit_2':
            self.disk_tab.printed_table.header.setObjectName("header_2")
            self.disk_tab.printed_table.header.sectionClicked['int']. \
                connect(self.header_clicked)
    return wrap
