

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
        self.tab_flags = [None] * 9
        self.load_flags()

    def load_flags(self):
        try:
            with open(global_variables.ROOT_FILE_PATH + '/config', 'r')\
                    as config_file:
                for tab in self.tab_flags:

                    for line_number, line in enumerate(config_file):
                        if line_number < 2:
                            continue
                        flag_list = []
                        for flag in line:
                            if flag != '\n':
                                flag_list.append(int(flag))
                        if len(flag_list) > 0:
                            tab = flag_list

                    # for line_number, line in enumerate(config_file):
                    #     if line_number < 2:
                    #         continue
                    #     flag_list = []
                    #     for flag in line:
                    #         if flag != '\n':
                    #             flag_list.append(int(flag))
        except Exception as e:
            print(e)
