

def header_signal(func):
    def wrap(self, *args):
        if len(args) == 1:
            func(self, args[0])
        elif len(args) == 2:
            func(self, args[0], args[1])
        else:
            func(self)

        self.tabs_list[self.current_tab].printed_table.\
            header.sectionClicked['int'].connect(self.header_clicked)
        self.tabs_list[self.current_tab].printed_table.\
            cellDoubleClicked['int', 'int'].connect(self.redirect)
    return wrap
