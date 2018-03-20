

import os

USER_LOGIN = ''
FQDN = ''
ROOT_FILE_PATH = os.path.dirname(os.path.abspath(__file__))

try:
    with open(ROOT_FILE_PATH + '/config', 'r') as config_file:
        USER_LOGIN = config_file.readline()[:-1]
        FQDN = config_file.readline()[:-1]

except Exception as e:
    print(e)