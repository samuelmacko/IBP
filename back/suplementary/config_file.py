

import global_variables


def create_config_file(vm_tab, disk_tab, host_tab):
    try:
        tab_list = [vm_tab, disk_tab, host_tab]
        with open(global_variables.ROOT_FILE_PATH + '/config', 'w+')\
                as config_file:
            config_file.write(global_variables.USER_LOGIN + '\n')
            config_file.write(global_variables.FQDN + '\n')
            for tab in tab_list:
                for chb in tab.table.col_flags:
                    config_file.write(str(chb))
                config_file.write('\n')
    except Exception as e:
        print(e)


class ConfigFile(object):

    def __init__(self):
        self.vm_tab = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                       1, 1, 1]
        self.disk_tab = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.host_tab = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                         1, 1, 1, 1, 1, 1, 1]
        self.load_flags()

    def load_flags(self):
        try:
            with open(global_variables.ROOT_FILE_PATH + '/config', 'r')\
                    as config_file:
                for line_number, line in enumerate(config_file):
                    if line_number < 2:
                        continue
                    flag_list = []
                    for flag in line:
                        if flag != '\n':
                            flag_list.append(int(flag))
                    if line_number == 2:
                        self.vm_tab = flag_list
                    elif line_number == 3:
                        self.disk_tab = flag_list
                    elif line_number == 4:
                        self.host_tab = flag_list
        except Exception as e:
            print(e)
