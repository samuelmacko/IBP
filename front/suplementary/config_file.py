

def create_config_file(vm_tab, disk_tab, host_tab):
    try:
        tab_list = [vm_tab, disk_tab, host_tab]
        with open('config', 'w+') as config_file:
            for tab in tab_list:
                for chb in tab.table.col_flags:
                    config_file.write(str(chb))
                config_file.write('\n')
    except Exception as e:
        print(e)


class ConfigFile(object):

    def __init__(self):
        self.vm_tab = None
        self.disk_tab = None
        self.host_tab = None
        self._load_config_file()

    def _load_config_file(self):
        try:
            with open('config', 'r') as config_file:
                for line_number, line in enumerate(config_file):
                    flag_list = []
                    for flag in line:
                        if flag != '\n':
                            flag_list.append(int(flag))
                    if line_number == 0:
                        self.vm_tab = flag_list
                    elif line_number == 1:
                        self.disk_tab = flag_list
                    elif line_number == 2:
                        self.host_tab = flag_list
        except Exception as e:
            pass
            # print(e)
